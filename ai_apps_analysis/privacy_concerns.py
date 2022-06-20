import pandas as pd
import requests
import urllib.request
import datetime
import os
from multiprocessing import Pool
from analysis_config import Config

from bs4 import BeautifulSoup

Cf = Config()
path_df_google_apps_characteristic = './df_google_apps_characteristic.csv'


def udf_get_privacy_url(app_link):
    try:
        html = urllib.request.urlopen(app_link).read().decode("utf-8")
        soup = BeautifulSoup(html, features='html.parser')
        tags = soup.find_all('a')
        res = []
        for tag in tags:
            tmp_url = str(tag.get('href')).strip()
            if 'http' in tmp_url and 'privacy' in tmp_url:
                res.append(tmp_url)
        if len(res) == 3:
            return res[0]
        else:
            return 'Wrong'
    except:
        return 'Wrong'


def udf_get_google_metadata(link):
    try:
        resp = requests.get(url=link)
        html = resp.text
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        return text
    except:
        return 'Wrong'


def get_split_pdf(df):
    """
    return [df, df, df].

    :param df: <dataframe>, df.
    :return: <list>, [df, df, df]
    """
    pdf = df.copy()
    number_samples = len(pdf)
    number_group_samples = number_samples // 90 + 1
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
    pdf['privacy_url'] = pdf['link'].apply(udf_get_privacy_url)
    pdf['privacy_data'] = pdf['privacy_url'].apply(udf_get_google_metadata)
    pdf.to_csv('./df_google_privacy.csv', mode='a', header=False, index=False)
    # ['pkg_name', 'link', 'tag_metadata', 'score', 'installs', 'category', 'company', 'privacy_url', 'privacy_data']


def main():
    df_google_apps_characteristic = pd.read_csv(path_df_google_apps_characteristic)
    df_list = get_split_pdf(df_google_apps_characteristic)

    starttime = datetime.datetime.now()
    cmd = 'echo start {start} >> time.txt'
    cmd = cmd.format(start=starttime)
    os.system(cmd)

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
