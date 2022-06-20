import os
import math
import pandas as pd
import random
import time

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 200)


def get_ai_model(path_dir_compile):
    model_path_list = []
    for root, dirs, files in os.walk(path_dir_compile, topdown=True):
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


def get_fileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return fsize  # MB


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


def main():

    df = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_model_path_size.csv', names=['path_model', 'model_size'])
    df['size_tag'] = df['model_size'].apply(udf_get_size_tag)
    df = df.drop_duplicates(subset=['model_size'], keep='first', inplace=False)
    df = df[(df['model_size'] <= 10) & (df['model_size'] >= 0.05)]

    df_entropy = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_modelpath_entropy.csv', names=['path_model', 'entropy'])

    df_merge = df.merge(df_entropy, left_on='path_model', right_on='path_model', how='inner')
    df_merge = df_merge[df_merge['entropy'] <= 7.5]

    local_path_model_list = get_ai_model('/Users/yinghua.li/Documents/Pycharm/data_model_performance')

    df_local = pd.DataFrame(columns=['local_path_model'])
    df_local['local_path_model'] = local_path_model_list
    df_local['id'] = df_local['local_path_model'].apply(udf_get_id)
    df_merge['id'] = df_merge['path_model'].apply(udf_get_id)

    df_merge = df_local.merge(df_merge, left_on='id', right_on='id', how='inner')

    df_merge = df_merge.sort_values(by=['model_size'], ascending=False).reset_index()

    model_path_list = list(df_merge['local_path_model'])[570+309+154+99+120:]
    model_size_list = list(df_merge['model_size'])[570+309+154+99+120:]
    print(len(model_size_list))
    model_name_list = [i.split('/')[-1] for i in model_path_list]
    model_push_command = '/Users/yinghua.li/Documents/tool/platform-tools/adb push {path_model} /data/local/tmp'
    model_push_command_list = [model_push_command.format(path_model=i) for i in model_path_list]

    model_run_command = "/Users/yinghua.li/Documents/tool/platform-tools/adb shell am start -S -n org.tensorflow.lite.benchmark/.BenchmarkModelActivity --es args \'\"--graph=/data/local/tmp/{model_name} --num_threads=4\"\'"
    model_run_command_list = [model_run_command.format(model_name=i) for i in model_name_list]

    for i in range(len(model_push_command_list)):
        os.system(model_push_command_list[i])
        os.system(model_run_command_list[i])
        time.sleep(30)
        print('model size:', model_size_list[i])

        save_result('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/performance6.txt', str(model_size_list[i]))


if __name__ == '__main__':
    main()
