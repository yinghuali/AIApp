import pandas as pd
import re
import datetime
import os
from urllib import request
from multiprocessing import Pool


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 200)

path_df_google_apps_characteristic = './df_google_apps_characteristic.csv'


def udf_get_link_reviews(s):
    return s+'&showAllReviews=true'


def get_reviews(link):
    try:
        html = request.urlopen(link).read()
        s_html = str(html)

        idx_list_1 = [substr.start() for substr in re.finditer('https://play-lh.googleusercontent.com/a-/', s_html)]
        idx_list_2 = [substr.start() for substr in re.finditer('https://play-lh.googleusercontent.com/a/', s_html)]
        idx_list = idx_list_1 + idx_list_2
        idx_list = sorted(idx_list)

        res_list = []
        if len(idx_list) > 1:
            for i in range(1, len(idx_list)):
                left = idx_list[i-1]
                right = idx_list[i]
                tmp_str = s_html[left: right]

                left_new = tmp_str.find(',"')
                right_new = tmp_str.find('",')
                s = tmp_str[left_new+2: right_new]
                s = s.replace("\\", "")
                if 'http' not in s:
                    res_list.append(s)
        return res_list
    except:
        return []


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
    pdf['link_review'] = pdf['link'].apply(udf_get_link_reviews)
    pdf['review_list'] = pdf['link_review'].apply(get_reviews)
    pdf.to_csv('./df_aiapp_review.csv', mode='a', header=False, index=False)
    # ['pkg_name', 'link', 'tag_metadata', 'score', 'installs', 'category','company', 'link_review', 'review_list']


def main(df):
    starttime = datetime.datetime.now()
    cmd = 'echo start {start} >> time.txt'
    cmd = cmd.format(start=starttime)
    os.system(cmd)

    df_list = get_split_pdf(df)

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
    df = pd.read_csv(path_df_google_apps_characteristic)
    main(df)

