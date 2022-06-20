import pandas as pd
import os
import datetime
import hashlib
import tensorflow as tf
from multiprocessing import Pool


path_tfmodel = '/home/yinghua/pycharm/AIApps/data/data_tfmodels'
path_save = '/home/yinghua/pycharm/AIApps/data/analysis_result/tfmodels_information.csv'


def get_model_sha256(path_file):
    f = open(path_file, "rb")
    sha256 = hashlib.sha256()
    sha256.update(f.read())
    return sha256.hexdigest()
    f.close()


def get_model_path(path_models):
    path_model = []
    if os.path.isdir(path_models):
        for root, dirs, files in os.walk(path_models, topdown=True):
            for file in files:
                file_absolute_path = os.path.join(root, file)
                if file_absolute_path.endswith('.tflite'):
                    path_model.append(file_absolute_path)
    return path_model


def udf_get_model_name(s):
    return s.split('/')[-1].split('_YY_')[-1]


def udf_apk_get_sha256(s):
    return s.split('/')[-1].split('_YY_')[0]


def main_single(path_tf_models_list):
    sha256_list = [udf_apk_get_sha256(i) for i in path_tf_models_list]
    model_name_list = [udf_get_model_name(i) for i in path_tf_models_list]
    sha256_model_list = [get_model_sha256(i) for i in path_tf_models_list]
    df = pd.DataFrame(columns=['sha256_app', 'sha256_model', 'model_name'])
    df['sha256_app'] = sha256_list
    df['sha256_model'] = sha256_model_list
    df['model_name'] = model_name_list
    df.to_csv(path_save, mode='a', header=False, index=False)


def main():
    starttime = datetime.datetime.now()
    cmd = 'echo start {start} >> time.txt'
    cmd = cmd.format(start=starttime)
    os.system(cmd)

    path_tf_models_list = get_model_path(path_tfmodel)
    path_tf_models_list_list = []
    left = 0
    right = 3300
    for i in range(80):
        tmp_list = path_tf_models_list[left:right]
        path_tf_models_list_list.append(tmp_list)
        left = right
        right += 3300

    with Pool(80) as p:
        p.map(main_single, path_tf_models_list_list)

    endtime = datetime.datetime.now()
    diff_time = endtime - starttime
    cmd = 'echo end {end} >> time.txt'
    cmd = cmd.format(end=endtime)
    os.system(cmd)
    cmd = 'echo diff {diff} >> time.txt'
    cmd = cmd.format(diff=diff_time)
    os.system(cmd)

    cmd = 'echo all finished >> time.txt'
    os.system(cmd)


if __name__ == '__main__':
    main()
