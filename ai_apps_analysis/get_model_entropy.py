import os
import datetime
import math
import pandas as pd
from multiprocessing import Pool


def get_path_ai_model(path_dir):
    model_path_list = []
    if os.path.isdir(path_dir):
        for root, dirs, files in os.walk(path_dir, topdown=True):
            for file in files:
                file_absolute_path = os.path.join(root, file)
                if file_absolute_path.endswith('.tflite'):
                    model_path_list.append(file_absolute_path)
    return model_path_list


def get_entropy(path_file):
    with open(path_file, "rb") as file:
        counters = {byte: 0 for byte in range(2 ** 8)}
        for byte in file.read():
            counters[byte] += 1
        filesize = file.tell()
        probabilities = [counter / filesize for counter in counters.values()]
        entropy = -sum(probability * math.log2(probability) for probability in probabilities if probability > 0)

    return entropy


def main_single(model_path_list):
    entropy_list = [get_entropy(i) for i in model_path_list]
    df = pd.DataFrame(columns=['model_path', 'entropy'])
    df['model_path'] = model_path_list
    df['entropy'] = entropy_list
    df.to_csv('df_modelpath_entropy.csv', mode='a', header=False, index=False)


def main(path_models_list, number_single_models, number_pool):
    """
    main function.

    :param path_model_list: <string>, path of model list.
    :param number_single_models: <int>, The number of models processed by each core.
    :param number_pool: <int>, Number of cores.
    """
    starttime = datetime.datetime.now()
    cmd = 'echo start {start} >> time.txt'
    cmd = cmd.format(start=starttime)
    os.system(cmd)

    model_list = get_path_ai_model(path_models_list)
    number_group = len(model_list) // number_single_models + 1

    start = 0
    end = number_group
    data_list = []
    if start < len(model_list):
        for i in range(number_group):
            tmp = model_list[start:end]
            data_list.append(tmp)
            start = end
            end = end+number_single_models

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
    main('/home/yinghua/pycharm/AIApps/data/data_tfmodels', 3250, 80)

