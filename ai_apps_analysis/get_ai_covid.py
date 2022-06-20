import pandas as pd

import hashlib


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 200)


def main():

    df_all = pd.read_csv('../data/analysis_result/df_all.csv')
    print(df_all.columns)

    f = open('../data/apkcovid.txt', 'r')
    lines = f.readlines()
    lines = [i.strip() for i in lines if i]
    df_apkcovid = pd.DataFrame(columns=['apkcovid'])
    df_apkcovid['apkcovid'] = lines
    df = df_apkcovid.merge(df_all, left_on='apkcovid', right_on='pkg_name', how='inner')
    df.to_csv('../data/analysis_result/df_ai_covid.csv', index=False, sep=',')

    print('Number of AI apps of covid-19:', len(df))
    print(df.columns)
    print(df)


if __name__ == '__main__':
    main()





