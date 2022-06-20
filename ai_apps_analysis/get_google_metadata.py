import os
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
from analysis_config import Config

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 200)
Cf = Config()


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


def udf_get_google_link(s):
    return 'https://play.google.com/store/apps/details?id={}'.format(s)


def udf_get_google_metadata(link):
    try:
        resp = requests.get(url=link)
        html = resp.text
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        return text
    except:
        return '*******************'


def get_split_pdf(path_save_df_all):
    """
    return [df, df, df].

    :param path_save_df_all: <string>, path of df_all.
    :return: <list>, [df, df, df]
    """
    df = pd.read_csv(path_save_df_all)
    df = get_markets_cols(df, Cf.markets)
    df_google = df[df['play.google.com'] == 1]
    df_google['link'] = df_google['pkg_name'].apply(udf_get_google_link)
    pdf = df_google[['pkg_name', 'link']].reset_index(drop=True).copy()
    number_samples = len(pdf)
    number_group_samples = number_samples // 90
    df_list = []
    left = 0
    right = number_group_samples

    for i in range(90):
        df_tmp = pdf.iloc[left:right, :]
        df_list.append(df_tmp)
        left = right
        right += number_group_samples

    if left < number_samples:
        df_list.append(pdf.iloc[left:, :])

    return df_list


def main_single(pdf):
    pdf['metadata'] = pdf['link'].apply(udf_get_google_metadata)
    pdf.to_csv('../data/analysis_result/df_google_metadata.csv', mode='a', header=False, index=False)


def main():
    starttime = datetime.datetime.now()
    cmd = 'echo start {start} >> time.txt'
    cmd = cmd.format(start=starttime)
    os.system(cmd)

    df_list = get_split_pdf(Cf.path_save_df_all)

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

    cmd = 'echo all finished >> time.txt'
    os.system(cmd)


if __name__ == '__main__':
    main()

