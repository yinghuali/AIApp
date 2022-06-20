import os
import math
import pandas as pd
import tflite
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 200)


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


def get_ai_model(path_dir_compile):
    model_path_list = []
    for root, dirs, files in os.walk(path_dir_compile, topdown=True):
        for file in files:
            file_absolute_path = os.path.join(root, file)
            if file_absolute_path.endswith('.tflite'):
                model_path_list.append(file_absolute_path)
    return model_path_list


def udf_get_size_tag(s):
    return math.ceil(s)


def save_result(path_resutl, content):
    """
    :param path_resutl: <string>, path of result.
    :param content: <string>, analysis results.
    """
    string_result = '\n' + content
    f = open(path_resutl, 'a')
    f.write('\n' + string_result)
    f.close()


def udf_get_id(s):
    return s.split('/')[-1]


def plot(x, y):
    plt.tick_params(labelsize=8)
    plt.rcParams['figure.figsize'] = (8.0, 6.0)
    plt.ylabel('FLOPs', fontsize=14)
    plt.xlabel('AI Models Size (MB)', fontsize=14)
    plt.scatter(x, y, s=[1] * len(x),  c='black')
    plt.savefig('../data/picture/flops.pdf')



def main():
    # df = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_model_path_size.csv', names=['path_model', 'model_size'])
    # df['size_tag'] = df['model_size'].apply(udf_get_size_tag)
    # df = df.drop_duplicates(subset=['model_size'], keep='first', inplace=False)
    # df = df[(df['model_size'] <= 10) & (df['model_size'] >= 0.05)]
    #
    # df_entropy = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_modelpath_entropy.csv', names=['path_model', 'entropy'])
    #
    # df_merge = df.merge(df_entropy, left_on='path_model', right_on='path_model', how='inner')
    # df_merge = df_merge[df_merge['entropy'] <= 7.5]
    #
    # local_path_model_list = get_ai_model('/Users/yinghua.li/Documents/Pycharm/data_model_performance')
    #
    # df_local = pd.DataFrame(columns=['local_path_model'])
    # df_local['local_path_model'] = local_path_model_list
    # df_local['id'] = df_local['local_path_model'].apply(udf_get_id)
    # df_merge['id'] = df_merge['path_model'].apply(udf_get_id)
    #
    # df_merge = df_local.merge(df_merge, left_on='id', right_on='id', how='inner')
    #
    # df_merge = df_merge.sort_values(by=['model_size'], ascending=False).reset_index()
    #
    # df_merge['flops'] = df_merge['local_path_model'].apply(get_model_flops)
    #
    # high = df_merge['flops'].quantile(0.9)
    # low = df_merge['flops'].quantile(0.1)
    # df_merge = df_merge[(df_merge['flops'] < high) & (df_merge['flops'] > low)]
    #
    # print(len(df_merge))
    #
    # print(df_merge.head())
    #
    # df_merge[['size_tag', 'model_size', 'flops']].to_csv("/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/flops_analysis.csv", index=False, sep=',')

    df = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/flops_analysis.csv')
    x = []
    y = []
    for size, pdf in df.groupby('size_tag'):
        pdf = pdf.sort_values(by=['flops'], ascending=True)
        n = len(pdf)
        tmp_y = list(pdf['flops'])
        tmp_x = list(pdf['model_size'])
        tmp_y = tmp_y[int(n*0.2): int(n*0.8)]
        tmp_x = tmp_x[int(n*0.2): int(n*0.8)]
        x += tmp_x
        y += tmp_y

    print(len(x))
    plot(x, y)


if __name__ == '__main__':
    main()
