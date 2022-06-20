import os
import tflite
import pandas as pd
import matplotlib.pyplot as plt


def get_ai_model(path_dir_compile):
    model_path_list = []
    for root, dirs, files in os.walk(path_dir_compile, topdown=True):
        for file in files:
            file_absolute_path = os.path.join(root, file)
            if file_absolute_path.endswith('.tflite'):
                model_path_list.append(file_absolute_path)
    return model_path_list


def get_fileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize*1.0/float(1024*1024)
    return fsize  # MB


def get_model_flops(path):
    """
    Only Conv and DepthwiseConv layers are considered but it is enough for most of the time.
    """
    try:
        with open(path, 'rb') as f:
            buf = f.read()
            model = tflite.Model.GetRootAsModel(buf, 0)
        graph = model.Subgraphs(0)
        total_flops = 0.0
        for i in range(graph.OperatorsLength()):
            op = graph.Operators(i)
            op_code = model.OperatorCodes(op.OpcodeIndex())
            op_code_builtin = op_code.BuiltinCode()
            op_opt = op.BuiltinOptions()
            flops = 0.0
            if op_code_builtin == tflite.BuiltinOperator.CONV_2D:
                # input shapes: in, weight, bias
                in_shape = graph.Tensors( op.Inputs(0)).ShapeAsNumpy()
                filter_shape = graph.Tensors(op.Inputs(1)).ShapeAsNumpy()
                bias_shape = graph.Tensors(op.Inputs(2)).ShapeAsNumpy()
                out_shape = graph.Tensors(op.Outputs(0)).ShapeAsNumpy()
                opt = tflite.Conv2DOptions()
                opt.Init(op_opt.Bytes, op_opt.Pos)
                flops = 2 * out_shape[1] * out_shape[2] * filter_shape[0] * filter_shape[1] * filter_shape[2] * filter_shape[3]

            elif op_code_builtin == tflite.BuiltinOperator.DEPTHWISE_CONV_2D:
                in_shape = graph.Tensors(op.Inputs(0)).ShapeAsNumpy()
                filter_shape = graph.Tensors(op.Inputs(1)).ShapeAsNumpy()
                out_shape = graph.Tensors(op.Outputs(0)).ShapeAsNumpy()
                flops = 2 * out_shape[1] * out_shape[2] * filter_shape[0] * filter_shape[1] * filter_shape[2] * filter_shape[3]
            total_flops += flops
        return total_flops
    except:
        return 0


def main():
    model_path_list = get_ai_model('/home/yinghua/pycharm/AIApps/data/data_tfmodels')
    model_size_list = [get_fileSize(i) for i in model_path_list]
    model_flops_list = [get_model_flops(i) for i in model_path_list]
    df = pd.DataFrame(columns=['model_path', 'model_size', 'model_flops'])
    df['model_path'] = model_path_list
    df['model_size'] = model_size_list
    df['model_flops'] = model_flops_list
    df.to_csv('df_flops_test.csv', index=False, sep=',')


if __name__ == '__main__':
    main()
