import pandas as pd
from analysis_config import Config
Cf = Config()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 200)


def get_models_update_infor(df_tfmodels_information, df_latest):
    number_models = 0
    number_changed_models = 0
    df_merge = df_tfmodels_information.merge(df_latest, left_on='sha256_app', right_on='sha256', how='left')
    for key, pdf in df_merge.groupby(['pkg_name', 'model_name']):
        number_models += 1
        tmp_df = pdf.sort_values(by=['dex_date'], ascending=True)
        if len(set(tmp_df['sha256_model'])) < len(tmp_df) and len(tmp_df) > 1:
            number_changed_models += 1
    print('number of changed models:', number_changed_models)
    print('all number of models:', number_models)
    print('changed models / all number of models =', number_changed_models*1.0/number_models)


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


if __name__ == '__main__':
    main()
