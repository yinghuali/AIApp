import pandas as pd
import os
import datetime
import hashlib
import tensorflow as tf
from multiprocessing import Pool

path_models = '/Users/yinghua.li/Documents/Pycharm/data_model_performance'

# quantization,
keywords_list = ['int16', 'int8']


def get_model_path(path_models):
    path_model = []
    if os.path.isdir(path_models):
        for root, dirs, files in os.walk(path_models, topdown=True):
            for file in files:
                file_absolute_path = os.path.join(root, file)
                if file_absolute_path.endswith('.tflite'):
                    path_model.append(file_absolute_path)
    return path_model


def check_models(path):
    tflite_model = tf.lite.Interpreter(model_path=path)
    tflite_model.allocate_tensors()
    layer_details = tflite_model.get_tensor_details()
    return layer_details


def main_single(path_model_list):
    label_int8 = []
    label_int16 = []
    for path in path_model_list:
        tag_int8 = 0
        tag_int16 = 0
        try:
            layer_details = check_models(path)
            for layer in layer_details:
                if 'int8' in str(layer):
                    tag_int8 = 1
                if 'int16' in str(layer):
                    tag_int16 = 1
        except:
            pass

        label_int8.append(tag_int8)
        label_int16.append(tag_int16)

    df = pd.DataFrame(columns=['path'])
    df['path'] = path_model_list
    df['label_int8'] = label_int8
    df['label_int16'] = label_int16
    df.to_csv('df_lightweight_model_multiple.csv', mode='a', header=False, index=False)


def main(number_single_sha256, number_pool):
    """
    main function.

    :param number_single_sha256: <int>, The number of Apks processed by each core.
    :param number_pool: <int>, Number of cores. note: len(path_sha256_list) <= number_single_sha256*number_pool
    """
    starttime = datetime.datetime.now()
    cmd = 'echo start {start} >> time.txt'
    cmd = cmd.format(start=starttime)
    os.system(cmd)

    df_modelpath_entropy = pd.read_csv('df_modelpath_entropy.csv', names=['model_path', 'entropy'])
    path_model_list = list(df_modelpath_entropy[df_modelpath_entropy['entropy'] < 7]['model_path'])

    number_group = len(path_model_list) // number_single_sha256 + 1

    start = 0
    end = number_group
    data_list = []
    if start < len(path_model_list):
        for i in range(number_group):
            tmp = path_model_list[start:end]
            data_list.append(tmp)
            start = end
            end = end + number_single_sha256

    with Pool(number_pool) as p:
        p.map(main_single, data_list)

    endtime = datetime.datetime.now()
    diff_time = endtime - starttime
    cmd = 'echo end {end} >> time.txt'
    cmd = cmd.format(end=endtime)
    os.system(cmd)
    cmd = 'echo diff {diff} >> time.txt'
    cmd = cmd.format(diff=diff_time)
    os.system(cmd)


if __name__ == '__main__':
    main(1944, 90)






