import pandas as pd
import os
import tensorflow as tf
import datetime
from multiprocessing import Pool

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 200)


def get_model_path(path_models):
    path_model = []
    for root, dirs, files in os.walk(path_models, topdown=True):
        for file in files:
            file_absolute_path = os.path.join(root, file)
            if file_absolute_path.endswith('.tflite'):
                path_model.append(file_absolute_path)
    return path_model


def get_sha256(s):
    return s.split('_YY_')[0].split('/')[-1].strip()


def get_model_name(s):
    return s.split('_YY_')[-1].strip()


def get_model_shape(path_model):
    try:
        # Load TFLite model and allocate tensors.
        interpreter = tf.lite.Interpreter(model_path=path_model)
        interpreter.allocate_tensors()
        # Get input and output tensors.
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        return str(input_details[0]['shape']) + '_YY_' + str(output_details[0]['shape'])
    except:
        return 'Wrong'


def main_single(pdf):
    pdf['shape'] = pdf['path_model'].apply(get_model_shape)
    pdf.to_csv('./data_feed_aiapps.csv', mode='a', header=False, index=False)
    # Index(['ai_sha256_id', 'information', 'framework_list', 'number_framework',
    #        'sha256', 'sha1', 'md5', 'dex_date', 'apk_size', 'pkg_name', 'vercode',
    #        'vt_detection', 'vt_scan_date', 'dex_size', 'markets', 'model_name',
    #        'path_model'],
    #       dtype='object')


def main():

    starttime = datetime.datetime.now()
    cmd = 'echo start {start} >> time.txt'
    cmd = cmd.format(start=starttime)
    os.system(cmd)

    path_model_list = get_model_path('/home/yinghua/pycharm/AIApps/data/data_tfmodels')
    sha256_list = [get_sha256(i) for i in path_model_list]
    model_name_list = [get_model_name(i) for i in path_model_list]

    df = pd.DataFrame(columns=['sha256', 'model_name', 'path_model'])
    df['sha256'] = sha256_list
    df['model_name'] = model_name_list
    df['path_model'] = path_model_list

    df_all = pd.read_csv('../data/analysis_result/df_all.csv')

    df_merge = df_all.merge(df, left_on='sha256', right_on='sha256', how='inner').reset_index(drop=True)

    number_samples = len(df_merge)
    single_samples = int(number_samples * 1.0 / 90) + 1
    left = 0
    right = single_samples

    df_list = []
    while left < len(df_merge):
        tmp_df = df.iloc[range(left, right), :].copy()
        df_list.append(tmp_df)
        left = right
        right += single_samples
        if right > len(df_merge):
            right = len(df_merge)

    with Pool(90) as p:
        p.map(main_single, df_list)

    endtime = datetime.datetime.now()
    diff_time = endtime - starttime
    cmd = 'echo end {end} >> time.txt'
    cmd = cmd.format(end=endtime)
    os.system(cmd)
    cmd = 'echo diff {diff} >> time.txt'
    cmd = cmd.format(diff=diff_time)
    os.system(cmd)


if __name__ == '__main__':
    main()
