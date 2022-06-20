import pandas as pd


def main():
    df_tf_models_information = pd.read_csv('../data/analysis_result/tfmodels_information.csv',
                                           names=['sha256_app', 'sha256_model', 'model_name'])
    df_tf_hub_model_information = pd.read_csv('../data/analysis_result/tf_hub_model_information.csv')
    df_merge = df_tf_models_information.merge(df_tf_hub_model_information, left_on='sha256_model',
                                              right_on='model_sha256',
                                              how='inner')
    df_google_apps_characteristic = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_google_apps_characteristic.csv')
    df_latest = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/latest.csv')
    df_merge = df_merge.merge(df_latest, left_on='sha256_app', right_on='sha256', how='left')
    df_merge = df_merge.merge(df_google_apps_characteristic, left_on='pkg_name', right_on='pkg_name', how='inner')
    df_merge = df_merge[df_merge['company'] != 'Wrong']
    df_merge = df_merge[['model_name_y', 'company', 'task', 'link']].drop_duplicates()
    df_merge = df_merge.sort_values(by=['model_name_y', 'company', 'task']).reset_index(drop=True)
    df_merge.to_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_publicmodel_comany_task.csv', index=False, sep=',')

    dic = dict(zip(df_merge['model_name_y'], df_merge['task']))
    task_list = list(dic.values())
    keys_list = list(dic.keys())
    company_list = []
    for key in keys_list:
        tmp = df_merge[df_merge['model_name_y'] == key]
        tmp_list = list(tmp['company'])
        company_list.append(tmp_list)

    df = pd.DataFrame(columns=['public_model_name', 'task', 'company'])
    df['public_model_name'] = keys_list
    df['task'] = task_list
    df['company'] = company_list
    df.to_csv("/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_publicmodel_comany_task_picture.csv",
              index=False, sep=',')


if __name__ == '__main__':
    main()
