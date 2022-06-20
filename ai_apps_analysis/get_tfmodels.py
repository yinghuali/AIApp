import os
import pickle
import datetime
import pandas as pd
import hashlib
from multiprocessing import Pool

current_path = '/home/yinghua/pycharm/AIApps/data/data_tfmodels'


def get_sha256(path_file):
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


def apk_decompile(path_apk, path_save_directory):
    """
    return path of apk decompile

    :param path_apk: <string>, path of apk.
    :param path_save_directory: <string>, path of saved directory.
    :return: <string>, path_save_file
    """
    # apktool_command = 'apktool d -s -f {path_apk} -o {path_save_file}'
    apktool_command = 'java -jar apktool_2.5.0.jar d -s -f {path_apk} -o {path_save_file}'
    # apktool_command = '/home/users/yili/tool/usr/java/jdk1.8.0_301/bin/java -jar apktool_2.5.0.jar d -f {path_apk} -o {path_save_file}'
    name_apk = path_apk.split('/')[-1].split('.')[0]
    name_apk_compile = name_apk + '_compile'
    path_save_file = path_save_directory + '/' + name_apk_compile
    apktool_command = apktool_command.format(path_apk=path_apk, path_save_file=path_save_file)
    os.system(apktool_command)

    return path_save_file


def get_single_decompile(path_sha256_list):
    finished = 0
    for sha256_str in path_sha256_list:
        down_command = 'curl -O --remote-header-name -G -d apikey=8c08e1e623110c600186098a11ba882a7e323ad32b71868510c971a504eca3f9 -d sha256={sha256} https://androzoo.uni.lu/api/download'
        down_command = down_command.format(sha256=sha256_str)
        os.system(down_command)
        try:
            path_apk = current_path + '/' + sha256_str + '.apk'
            print('==apk_decompile start==')
            path_apk_decompile = apk_decompile(path_apk, current_path)  # path of apk decompile
            print('==apk_decompile finished==')

            path_model_list = get_model_path(path_apk_decompile)
            if len(path_model_list) > 0:
                for path_model in path_model_list:
                    model_name = path_model.split('/')[-1]
                    cp_command = 'cp {path_model} {new_path}'.format(path_model=path_model, new_path='./'+sha256_str+'_YY_' + model_name)
                    os.system(cp_command)

            rm_apk_command = 'rm ' + current_path + '/' + sha256_str + '.apk'
            rm_decompile_command = 'rm -rf ' + current_path + '/' + sha256_str + '_compile'

            os.system(rm_apk_command)
            os.system(rm_decompile_command)

            cmd = 'echo finished {finished} >> finished.log'
            cmd = cmd.format(finished=finished)
            finished += 1
            os.system(cmd)

        except:
            error_log = 'echo error sha256 {sha256_str} >> error.log'
            cmd_error_log = error_log.format(sha256_str=sha256_str)
            os.system(cmd_error_log)


def main(sha256_list, number_single_sha256, number_pool):
    starttime = datetime.datetime.now()
    cmd = 'echo start {start} >> time.txt'
    cmd = cmd.format(start=starttime)
    os.system(cmd)

    number_group = len(sha256_list) // number_single_sha256 + 1

    start = 0
    end = number_group
    data_list = []
    if start < len(sha256_list):
        for i in range(number_group):
            tmp = sha256_list[start:end]
            data_list.append(tmp)
            start = end
            end = end + number_single_sha256

    with Pool(number_pool) as p:
        p.map(get_single_decompile, data_list)

    endtime = datetime.datetime.now()
    diff_time = endtime - starttime
    cmd = 'echo end {end} >> time.txt'
    cmd = cmd.format(end=endtime)
    os.system(cmd)
    cmd = 'echo diff {diff} >> time.txt'
    cmd = cmd.format(diff=diff_time)
    os.system(cmd)


if __name__ == '__main__':
    df_google_tflite_sha256_pkgname = pd.read_csv('../data/analysis_result/df_google_tflite_sha256_pkgname.csv')
    sha256_list = list(df_google_tflite_sha256_pkgname['sha256'])
    main(sha256_list, 1200, 80)
