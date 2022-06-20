import os
import pandas as pd
import datetime
from multiprocessing import Pool


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
    fsize = fsize/float(1024*1024)
    return fsize # MB


def main_single(model_path_list):
    model_filesize_list = [get_fileSize(i) for i in model_path_list]
    df = pd.DataFrame(columns=['model_path', 'model_filesize'])
    df['model_path'] = model_path_list
    df['model_filesize'] = model_filesize_list
    df.to_csv('./df_model_path_size.csv', mode='a', header=False, index=False)


def main(number_single_sha256, number_pool):
    """
    main function.

    :param path_sha256_list: <string>, path of list of pkl.
    :param number_single_sha256: <int>, The number of Apks processed by each core.
    :param number_pool: <int>, Number of cores. note: len(path_sha256_list) <= number_single_sha256*number_pool
    """
    starttime = datetime.datetime.now()
    cmd = 'echo start {start} >> time.txt'
    cmd = cmd.format(start=starttime)
    os.system(cmd)

    model_path_list = get_ai_model('/home/yinghua/pycharm/AIApps/data/data_tfmodels')  # 259543
    number_group = len(model_path_list) // number_single_sha256 + 1

    start = 0
    end = number_group
    data_list = []
    if start < len(model_path_list):
        for i in range(number_group):
            tmp = model_path_list[start:end]
            data_list.append(tmp)
            start = end
            end = end+number_single_sha256

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
    main(2900, 90)
