import pandas as pd
from analysis_config import Config
Cf = Config()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 200)


def get_models_update_infor(df_tfmodels_information, df_latest):
    df_merge = df_tfmodels_information.merge(df_latest, left_on='sha256_app', right_on='sha256', how='left')
    df_merge = df_merge.dropna(subset=['pkg_name', 'model_name'])

    res_change_model = 0
    for key, pdf in df_merge.groupby(['pkg_name']):
        tmp_pdf = pdf.sort_values(by=['dex_date'], ascending=True)
        tmp_time_list = list(tmp_pdf['dex_date'])
        if len(tmp_time_list) > 1:
            for i in range(1, len(tmp_time_list)):
                old_df = tmp_pdf[tmp_pdf['dex_date'] == tmp_time_list[i - 1]]
                old_model_inf = list(sorted(old_df['sha256_model']))

                new_df = tmp_pdf[tmp_pdf['dex_date'] == tmp_time_list[i]]
                new_model_inf = list(sorted(new_df['sha256_model']))

                if old_model_inf != new_model_inf:
                    res_change_model += 1

    print(len(set(df_merge['dex_date'])))
    print('number of apks including history versions:', len(set(df_merge['sha256_app'])))
    print('number of ai apps:', len(set(df_merge['pkg_name'])))
    print('number of changed models:', res_change_model)
    print('changed models / number of apks including history versions =', res_change_model*1.0/len(set(df_merge['sha256_app'])))



# Analyzing model changes during AI app updating
def get_ratio_model_update():
    df = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_all.csv')
    key_words = ['.tflite', '.lite', '.pt', '.ptl', '.param', '.mlmodel', '.model', '.caffemodel',
                 '.feathermodel', '.chainermodel', 'PaddlePredictor.jar', 'libpaddle_lite_jni.so',
                 '.nnet', 'libtvm_rumtime.so', '.moa', 'model.prof',
                 '.mallet', '.classifier', '.inferencer', '.cntk']

    def udf_flag_tflite(s):
        if '.tflite' in s or '.lite' in s:
            return 1
        else:
            return 0

    def udf_flag_model(s):
        for key in key_words:
            if key in s:
                return 1
        return 0

    df['tflite'] = df['information'].apply(udf_flag_tflite)
    df['flag_model'] = df['information'].apply(udf_flag_model)

    ratio = len(df[df['tflite'] == 1]) / len(df[df['flag_model'] == 1])
    print(ratio)


def get_models_public_infor(df_tfmodels_information, df_latest):
    df_merge = df_tfmodels_information.merge(df_latest, left_on='sha256_app', right_on='sha256', how='left')
    df_merge_single = df_merge.sort_values(by=['dex_date'], ascending=False).drop_duplicates(
                                                                         subset=['pkg_name', 'model_name'],
                                                                         keep='first',
                                                                         inplace=False).reset_index(drop=True)
    tf_hub_model_information = pd.read_csv('../data/analysis_result/tf_hub_model_information.csv')
    df_merge_hub = df_merge_single.merge(tf_hub_model_information, left_on='sha256_model',
                                         right_on='model_sha256',
                                         how='inner')
    print('Number of tflite models:', len(tf_hub_model_information))
    print('Number of ai apps that clone ai models from tflite hub: ', len(df_merge_hub))
    print('Task of clone models:', list(set(df_merge_hub['task'])))


def main():
    df_tfmodels_information = pd.read_csv('../data/analysis_result/tfmodels_information.csv',
                                          names=['sha256_app', 'sha256_model', 'model_name'])
    df_latest = pd.read_csv(Cf.path_latest)
    get_models_update_infor(df_tfmodels_information, df_latest)
    print('================')
    get_models_public_infor(df_tfmodels_information, df_latest)
    get_ratio_model_update()


if __name__ == '__main__':
    main()
