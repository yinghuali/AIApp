import pandas as pd
from analysis_config import Config
Cf = Config()


def save_result(path_resutl, content):
    """
    :param path_resutl: <string>, path of result.
    :param content: <string>, analysis results.
    """
    string_result = '\n' + content
    f = open(path_resutl, 'a')
    f.write('\n' + string_result)
    f.close()


def get_markets_cols(df, markets):
    """
    add cols of markets.

    :param df: <dataframe>, df_all.
    :param markets: <list> makets list.
    :return: <dataframe>, new df.
    """
    markets_list = list(df['markets'])
    for col_market in markets:
        col_tmp = []
        for str_markets in markets_list:
            if col_market in str_markets:
                col_tmp.append(1)
            else:
                col_tmp.append(0)
        df[col_market] = col_tmp
    return df


def get_framework_cols(df):
    """
    add cols of framework.

    :param df: <dataframe>, df_all.
    :return: <dataframe>, new df.
    """
    frameworks = Cf.list_dl_framework + Cf.list_ml_framework + Cf.list_ai_service_framework
    framework_list = list(df['framework_list'])
    for col_framework in frameworks:
        col_tmp = []
        for str_framework in framework_list:
            if col_framework in str_framework:
                col_tmp.append(1)
            else:
                col_tmp.append(0)
        df[col_framework] = col_tmp
    return df


def get_df_ml_service_cols(df):
    """
    get ai cols of framework.

    :param df: <dataframe>, df_all
    :return: <dataframe>, new df
    """
    df['dl'] = 0
    df['ml'] = 0
    df['service'] = 0
    for col in Cf.list_dl_framework:
        df['dl'] += df[col]
    for col in Cf.list_ml_framework:
        df['ml'] += df[col]
    for col in Cf.list_ai_service_framework:
        df['service'] += df[col]
    return df


def main():
    df = pd.read_csv(Cf.path_save_df_all)
    df = get_markets_cols(df, Cf.markets)
    df = get_framework_cols(df)
    df = get_df_ml_service_cols(df)
    df['apk_size_MB'] = df['apk_size'] / (1024 * 1024)
    df['dex_date'] = pd.to_datetime(df['dex_date'])
    df['year'] = df['dex_date'].apply(lambda x: x.year)

    print(df.columns)
    print(len(df))
    print(len(set(df['pkg_name'])))

    # number of ai apps
    print('number of ai apps')
    number_ai_apps = len(set(df['pkg_name']))
    save_result(Cf.path_characteristics_ai_apps_result, 'number of ai apps: ' + str(number_ai_apps))

    # historic ai apps analysis
    print('historic ai apps analysis')
    df_all_latest = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_all_latest.csv')
    df_tmp = df_all_latest.dropna(subset=['ai_sha256_id'])[['ai_sha256_id', 'pkg_name']]
    df_all_latest['count_version'] = 1
    df_versions = df_all_latest.groupby('pkg_name').agg({'count_version': 'sum'}).reset_index()
    df_versions = df_tmp.merge(df_versions, left_on='pkg_name', right_on='pkg_name', how='left')
    dic = {}
    number_versions_1_5 = len(df_versions[df_versions['count_version'] < 5])
    number_versions_5_10 = len(df_versions[(df_versions['count_version'] >= 5) & (df_versions['count_version'] < 10)])
    number_versions_10_15 = len(df_versions[(df_versions['count_version'] >= 10) & (df_versions['count_version'] < 15)])
    number_versions_15_20 = len(df_versions[(df_versions['count_version'] >= 15) & (df_versions['count_version'] < 20)])
    number_versions_20_ = len(df_versions[df_versions['count_version'] >= 20])
    dic['number_versions_1_5'] = number_versions_1_5
    dic['number_versions_5_10'] = number_versions_5_10
    dic['number_versions_10_15'] = number_versions_10_15
    dic['number_versions_15_20'] = number_versions_15_20
    dic['number_versions_20_'] = number_versions_20_
    save_result(Cf.path_characteristics_ai_apps_result, 'historic ai apps analysis')
    save_result(Cf.path_characteristics_ai_apps_result, str(dic))
    save_result(Cf.path_characteristics_ai_apps_result, '======================================')

    # number of AI apps in each market
    print('markets analysis')
    number_markets = len(Cf.markets)
    save_result(Cf.path_characteristics_ai_apps_result, 'number_markets: ' + str(number_markets))
    save_result(Cf.path_characteristics_ai_apps_result, '======================================')

    dic = {}
    for col in Cf.markets:
        number_col_markets = len(df[df[col] == 1])
        dic[col] = number_col_markets
    save_result(Cf.path_characteristics_ai_apps_result, 'number of AI apps in each market')
    save_result(Cf.path_characteristics_ai_apps_result, str(dic))
    save_result(Cf.path_characteristics_ai_apps_result, '======================================')

    # number of AI apps in framework combination
    number_framework_list = list(set(df['number_framework']))
    dic = {}
    for number in number_framework_list:
        dic[number] = len(df[df['number_framework'] == number])
    save_result(Cf.path_characteristics_ai_apps_result, 'number of AI apps in framework combination')
    save_result(Cf.path_characteristics_ai_apps_result, str(dic))
    save_result(Cf.path_characteristics_ai_apps_result, '======================================')

    # popularity of combination framework
    number_framework_list = list(set(df['number_framework']))
    for number in number_framework_list:
        if number > 1:
            df_tmp = df[df['number_framework'] == number].copy()
            df_tmp['count'] = 1
            df_group = df_tmp.groupby('framework_list').agg({'count': 'sum'}).reset_index()
            dic = dict(zip(list(df_group['framework_list']), list(df_group['count'])))
            save_result(Cf.path_characteristics_ai_apps_result, 'popularity of combination framework: ' + str(number))
            save_result(Cf.path_characteristics_ai_apps_result, str(dic))
            save_result(Cf.path_characteristics_ai_apps_result, '======================================')

    # number of AI apps in each framework
    frameworks = Cf.list_dl_framework + Cf.list_ml_framework + Cf.list_ai_service_framework
    dic = {}
    for framework in frameworks:
        dic[framework] = len(df[df[framework]==1])
    save_result(Cf.path_characteristics_ai_apps_result, 'number of AI apps in each framework')
    save_result(Cf.path_characteristics_ai_apps_result, str(dic))
    save_result(Cf.path_characteristics_ai_apps_result, '======================================')

    # number of AI apps in DL、ML、AI service framework
    dic = {}
    number_dl = len(df[df['dl'] >= 1])
    number_ml = len(df[df['ml'] >= 1])
    number_service = len(df[df['service'] >= 1])
    dic['dl'] = number_dl
    dic['ml'] = number_ml
    dic['service'] = number_service
    save_result(Cf.path_characteristics_ai_apps_result, 'number of AI apps in DL、ML、AI service framework')
    save_result(Cf.path_characteristics_ai_apps_result, str(dic))
    save_result(Cf.path_characteristics_ai_apps_result, '======================================')

    # size of DL、ML、service framework
    dic = {}
    dic['size_ml'] = list(df[df['ml'] >= 1]['apk_size_MB'])
    dic['size_dl'] = list(df[df['dl'] >= 1]['apk_size_MB'])
    dic['size_service'] = list(df[df['service'] >= 1]['apk_size_MB'])
    save_result(Cf.path_characteristics_ai_apps_result, 'size of DL、ML、service framework')
    save_result(Cf.path_characteristics_ai_apps_result, str(dic))
    save_result(Cf.path_characteristics_ai_apps_result, '======================================')

    # size of app in each framework
    frameworks = Cf.list_dl_framework + Cf.list_ml_framework + Cf.list_ai_service_framework
    for framework in frameworks:
        dic = {}
        df_tmp = df[df[framework] == 1]
        dic[framework] = list(df_tmp['apk_size_MB'])
        save_result(Cf.path_characteristics_ai_apps_result, 'size of app in each framework: ' + framework)
        save_result(Cf.path_characteristics_ai_apps_result, str(dic))
        save_result(Cf.path_characteristics_ai_apps_result, '======================================')

    # ai apps in each year
    dic = {}
    year_list = list(set(df['year']))
    for year in year_list:
        dic[year] = len(df[df['year'] == year])
    save_result(Cf.path_characteristics_ai_apps_result, 'ai apps in each year')
    save_result(Cf.path_characteristics_ai_apps_result, str(dic))
    save_result(Cf.path_characteristics_ai_apps_result, '======================================')

    # Frameworks usage per year
    frameworks = Cf.list_dl_framework + Cf.list_ml_framework + Cf.list_ai_service_framework
    for framework in frameworks:
        df_tmp = df[df[framework] == 1].copy()
        df_tmp['count_year'] = 1
        df_tmp_re = df_tmp.groupby('year').agg({'count_year': 'sum'}).reset_index()
        dic = dict(zip(list(df_tmp_re['year']), list(df_tmp_re['count_year'])))
        save_result(Cf.path_characteristics_ai_apps_result, 'Frameworks usage per year: ' + framework)
        save_result(Cf.path_characteristics_ai_apps_result, str(dic))
        save_result(Cf.path_characteristics_ai_apps_result, '======================================')


if __name__ == '__main__':
    main()



