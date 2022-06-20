import os
import pandas as pd

from analysis_config import Config
from utils import udf_get_framework_name, udf_number_framework

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 200)

Cf = Config()


def get_path_result(path_dir):
    """
    return path list
    :param path_dir: <string>, path of results directory.
    :return: <list>
    """
    path_list = []
    if os.path.isdir(path_dir):
        for root, dirs, files in os.walk(path_dir, topdown=True):
            for file in files:
                file_absolute_path = os.path.join(root, file)
                if file_absolute_path.endswith('.txt'):
                    path_list.append(file_absolute_path)
    return path_list


def get_ai_sha256_id(path_result):
    """
    return ai apps id.

    :param path_result: <string>, path of ai apps result.
    :return: <list>, ai apps id.
    """
    f = open(path_result, "r")
    lines = f.readlines()
    lines = [line for line in lines if len(line) > 20]
    res = []
    for line in lines:
        sha256_id = line.strip().split('_compile')[0].split('/')[-1]
        if len(sha256_id) == 64 and sha256_id not in res:
            res.append(sha256_id)
    return res


def get_ai_apps_information(ai_sha256_list, path_result_directory):
    """
    return dataframe.

    :param ai_sha256_list: <list>
    :param path_result_directory: <string>
    :param save_path: <string>
    :return: <dataframe>, columns=['ai_sha256_id', 'information']
    """
    information_list = []
    information_all_list = []
    path_list = get_path_result(path_result_directory)

    for file_path in path_list:
        f = open(file_path, "r")
        lines = f.readlines()
        lines = [line for line in lines if len(line) > 20]
        information_all_list += lines

    information_all_list = list(set(information_all_list))

    for sha256_id in ai_sha256_list:
        tmp = ''
        for info in information_all_list:
            if sha256_id in info:
                keywords_information = info.strip().split('_compile->')[-1]
                if '_compile' in keywords_information:
                    keywords_information = keywords_information.split('_compile')[-1]
                tmp += keywords_information
        information_list.append(tmp)

    df = pd.DataFrame(columns=['ai_sha256_id', 'information'])
    df['ai_sha256_id'] = ai_sha256_list
    df['information'] = information_list

    return df


def main():
    """
    save csv.
    """
    path_list = get_path_result(Cf.path_result_directory)

    sha256_list = []
    for path_result in path_list:
        sha256_list += get_ai_sha256_id(path_result)
    df = get_ai_apps_information(sha256_list, Cf.path_result_directory)

    df['framework_list'] = df['information'].apply(udf_get_framework_name)
    df['number_framework'] = df['framework_list'].apply(udf_number_framework)

    df_latest = pd.read_csv(Cf.path_latest)
    df_all = df.merge(df_latest, left_on='ai_sha256_id', right_on='sha256', how='left')
    df_all.to_csv(Cf.path_save_df_all, index=False, sep=',')

    df_all_latest = df.merge(df_latest, left_on='ai_sha256_id', right_on='sha256', how='right')
    df_all_latest.to_csv(Cf.path_save_df_all_latest, index=False, sep=',')


if __name__ == '__main__':
    main()


