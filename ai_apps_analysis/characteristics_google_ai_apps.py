import pandas as pd
from analysis_config import Config
import re
Cf = Config()


def udf_google_category(s):
    text = s[s.find('Everyone')-25:s.find('Everyone')]
    category_list = Cf.google_category.copy()
    value = [text.count(i) for i in category_list]
    dic_category_value = dict(zip(category_list, value))

    res = []
    for i in dic_category_value:
        if dic_category_value[i] > 0:
            res.append(i)

    if len(res) == 1:
        return res[0]

    elif len(res) > 1:
        value = []
        if len(res) > 1:
            for category in res:
                value.append(text.find(category))
            dic = dict(zip(res, value))
        return max(dic, key=dic.get)

    elif len(res) == 0:
        app_name = s.split('-')[0].strip()
        text = s[len(app_name):]
        text = text[text.find(app_name):]
        text = text[len(app_name):len(app_name)+120]
        for i in category_list:
            if i in text:
                res.append(i)

        if len(res) == 0:
            print(text)
            print(app_name)
            print('==========')
            return 'Wrong'

        if len(res) == 1:
            return res[0]

        if len(res) > 1:
            value = []
            for category in res:
                value.append(text.find(category))
            dic = dict(zip(res, value))

            return min(dic, key=dic.get)


def get_company(text, category):
    if category == 'Wrong':
        return 'Wrong'
    else:
        try:
            str_tag = "window['_wjdc'] = function (d) {window['_wjdd'] = d};"
            idx = text.find(str_tag)
            n_str = len(str_tag)
            text = text[idx + n_str:].strip()

            app_name = text.split('- Apps')[0].strip()
            text = text.split('- Apps')[1]
            text = text[text.find(app_name):]
            text = text[:text.find(category)]
            company = text.split(app_name)[-1].strip()
            if len(company) == 0:
                return app_name
            return company
        except:
            return 'Wrong'


def udf_get_number_install(text):
    try:
        text = text[text.find('Installs') + 8:]
        n = text[: text.find('+')]
        n = n.replace(',', '')
        n = int(n)
        return n
    except:
        return 0


def get_metadata_score(s):
    try:
        result = re.finditer('info', s)
        for i in result:
            span = list(i.span())
            judge = s[span[-1]]
            if judge.isdigit():
                start = span[-1]
                end = span[-1] + 3
                return s[start: end]
    except:
        return '0'


def udf_tag(s):
    if 'Not Found' in s:
        return 0
    else:
        return 1


def main():
    df_google = pd.read_csv('../data/analysis_result/df_google_metadata.csv', names=['pkg_name', 'link', 'metadata'])
    print('len(df_google):', len(df_google))
    df_google['tag_metadata'] = df_google['metadata'].apply(udf_tag)
    df_google_tag = df_google[df_google['tag_metadata'] == 1].reset_index(drop=True)
    print('len(df_google_tag):', len(df_google_tag))

    df_google_tag['score'] = df_google_tag['metadata'].apply(get_metadata_score)
    df_google_tag['installs'] = df_google_tag['metadata'].apply(udf_get_number_install)
    df_google_tag['category'] = df_google_tag['metadata'].apply(udf_google_category)

    list_metadata = list(df_google_tag['metadata'])
    list_category = list(df_google_tag['category'])
    list_company = []
    for i in range(len(list_metadata)):
        text = list_metadata[i]
        category = list_category[i]
        company = get_company(text, category)
        list_company.append(company)

    df_google_tag['company'] = list_company

    df_google_tag[['pkg_name', 'link', 'tag_metadata', 'score', 'installs', 'category', 'company']].to_csv(
                                                            "../data/analysis_result/df_google_apps_characteristic.csv",
                                                            index=False, sep=',')


if __name__ == '__main__':
    main()
