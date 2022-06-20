import pandas as pd
import numpy as np
from analysis_config import Config

Cf = Config()
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 200)


def save_result(path_resutl, content):
    """
    :param path_resutl: <string>, path of result.
    :param content: <string>, analysis results.
    """
    string_result = '\n' + content
    f = open(path_resutl, 'a')
    f.write('\n' + string_result)
    f.close()


def udf_float(s):
    try:
        res = float(s)
        return res
    except:
        res = float(s[0])
        return res


def get_dic_list_high_low(dic):
    """
    return [key1, key2], [value1, value2], high->low.

    :param dic: <dict>
    :return: <list>, [key1, key2], [value1, value2], high->low.
    """
    L = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    key_list = [i[0] for i in L]
    value_list = [i[1] for i in L]
    return key_list, value_list


def main():
    df = pd.read_csv('../data/analysis_result/df_google_apps_characteristic.csv')
    print(df.columns)
    print('=================================================')
    print('Number of AI apps in google play: ', len(df))

    print('Number of AI app in google play with category：', len(df[df['category'] != 'Wrong']))

    # category of ai apps
    pdf = df[df['category'] != 'Wrong'].copy()
    pdf['count_app'] = 1
    pdf = pdf.groupby('category').agg({'count_app': 'sum'}).reset_index()
    dic = dict(zip(pdf['category'], pdf['count_app']))
    save_result('../data/analysis_result/google_play_result.txt', 'category of ai apps')
    save_result('../data/analysis_result/google_play_result.txt', str(dic))

    # average score
    pdf = df.dropna(subset=['score']).copy()
    pdf = pdf[pdf['category'] != 'Wrong'].copy()
    pdf['score'] = pdf['score'].apply(udf_float)
    pdf = pdf[pdf['score'] <= 5]
    pdf = pdf.groupby('category').agg({'score': 'mean'}).reset_index()
    dic = dict(zip(pdf['category'], pdf['score']))
    save_result('../data/analysis_result/google_play_result.txt', 'average score')
    save_result('../data/analysis_result/google_play_result.txt', str(dic))

    # average installs
    pdf = df[df['category'] != 'Wrong'].copy()
    pdf = pdf.groupby('category').agg({'installs': 'mean'}).reset_index()
    dic = dict(zip(pdf['category'], pdf['installs']))
    save_result('../data/analysis_result/google_play_result.txt', 'average installs')
    save_result('../data/analysis_result/google_play_result.txt', str(dic))

    # Number of AI apps in company
    df['filter'] = df['company'].apply(lambda x: len(x))
    pdf = df[(df['category'] != 'Wrong') & (df['company'] != 'Wrong') & (df['filter'] < 100) * (df['filter'] > 3)].copy()
    pdf['count_app'] = 1
    df_company = pdf.groupby('company').agg({'count_app': 'sum'}).reset_index().copy()
    dic = dict(zip(df_company['company'], df_company['count_app']))
    # save_result('../data/analysis_result/google_play_result.txt', 'Number of AI apps in company')
    # save_result('../data/analysis_result/google_play_result.txt', str(dic))

    # Number of AI apps in Top10 company
    L = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    key_list = [i[0] for i in L][:10]
    value_list = [i[1] for i in L][:10]
    dic = dict(zip(key_list, value_list))
    save_result('../data/analysis_result/google_play_result.txt', 'Number of AI apps in Top10 company')
    save_result('../data/analysis_result/google_play_result.txt', str(dic))

    # categories of AI apps in Top10 company
    dic = {}
    for company in key_list:
        category_list = list(set(pdf[pdf['company'] == company]['category']))
        dic[company] = category_list
    save_result('../data/analysis_result/google_play_result.txt', 'categories of AI apps in Top10 company')
    save_result('../data/analysis_result/google_play_result.txt', str(dic))



if __name__ == '__main__':
    main()
