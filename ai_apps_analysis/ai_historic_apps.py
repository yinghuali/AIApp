import pandas as pd
from utils import udf_get_framework_name, udf_number_framework


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


def get_ai_apps_information(ai_sha256_list, file_path):
    """
    return dataframe.

    :param ai_sha256_list: <list>
    :param path_result_directory: <string>
    :param save_path: <string>
    :return: <dataframe>, columns=['ai_sha256_id', 'information']
    """
    information_list = []

    f = open(file_path, "r")
    lines = f.readlines()
    information_all_list = [line for line in lines if len(line) > 20]
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
    path = '../data/analysis_result/history_ai_sha256_list.txt'
    sha256_list = get_ai_sha256_id(path)

    df = get_ai_apps_information(sha256_list, path)

    df['framework_list'] = df['information'].apply(udf_get_framework_name)
    df['number_framework'] = df['framework_list'].apply(udf_number_framework)
    df.to_csv('df_history_ai_sha256_list.csv', index=False, sep=',')


if __name__ == '__main__':
    main()
