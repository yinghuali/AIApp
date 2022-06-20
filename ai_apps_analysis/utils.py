import os
import re
import hashlib
import requests
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from bs4 import BeautifulSoup
from analysis_config import Config
from wordcloud import WordCloud
Cf = Config()


def udf_get_framework_name(s):
    dic_ml = Cf.dic_ml_framework_keywords
    dic_dl = Cf.dic_dl_framework_keywords
    dic_ai_service = Cf.dic_ai_service_framework_keywords
    dic_tmp = dict(dic_ml, **dic_dl)
    dic_all = dict(dic_tmp, **dic_ai_service)

    frame_work_list = []

    for framework in dic_all:
        keywords_list = dic_all[framework]
        for keyword in keywords_list:
            if keyword in s:
                frame_work_list.append(framework)
    return list(set(frame_work_list))


def udf_number_framework(s):
    return len(s)


def udf_get_google_metadata(link):
    resp = requests.get(url=link)
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    return text


def get_metadata_score(s):
    """
    return apps score.

    :param s: <string>, metadata.
    :return: <float>, score.
    """
    result = re.finditer('info', s)
    for i in result:
        span = list(i.span())
        judge = s[span[-1]]
        if judge.isdigit():
            start = span[-1]
            end = span[-1]+3
            return float(s[start: end])
    return 0


def rename_market(pdf):
    new_markets = []
    list_markets = list(pdf['markets'])
    for market in list_markets:
        if 'play.google.com' in market and '|' in market and 'appchina' not in market:
            new_markets.append('play.google.com')
        elif 'appchina' in market and '|' in market and 'play.google.com' not in market:
            new_markets.append('appchina')
        else:
            new_markets.append(market)
    pdf['new_markets'] = new_markets
    return pdf


def get_model_path(path_models):
    path_model = []
    for root, dirs, files in os.walk(path_models, topdown=True):
        for file in files:
            file_absolute_path = os.path.join(root, file)
            if file_absolute_path.endswith('.tflite'):
                path_model.append(file_absolute_path)
    return path_model


def get_sha256(path_file):
    f = open(path_file, "rb")
    sha256 = hashlib.sha256()
    sha256.update(f.read())
    return sha256.hexdigest()
    f.close()


def save_result(path_resutl, content):
    """
    :param path_resutl: <string>, path of result.
    :param content: <string>, analysis results.
    """
    string_result = '\n' + content
    f = open(path_resutl, 'a')
    f.write('\n' + string_result)
    f.close()


def pic_wordcloud(dic, save_path):
    matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
    wordcloud = WordCloud(font_path="SimHei.ttf", background_color="white", max_font_size=80)
    wordcloud = wordcloud.fit_words(dic)
    plt.savefig(save_path)
    plt.imshow(wordcloud)
    plt.savefig(save_path, format="pdf")