import pandas as pd
from analysis_config import Config
Cf = Config()


def udf_tflite_model(s):
    if '.tflite' in s:
        return 1
    else:
        return 0


def udf_google_play(s):
    if 'play.google.com' in s:
        return 1
    else:
        return 0


def main():
    df_latest = pd.read_csv(Cf.path_latest)
    df_latest['google_play'] = df_latest['markets'].apply(udf_google_play)
    df_latest_google = df_latest[df_latest['google_play'] == 1].reset_index(drop=True)
    df_all = pd.read_csv('../data/analysis_result/df_all.csv')
    df_all['tflite'] = df_all['information'].apply(udf_tflite_model)
    df_all['google_play'] = df_all['markets'].apply(udf_google_play)
    df_all = df_all[(df_all['tflite'] == 1) & (df_all['google_play'] == 1)][['pkg_name']].reset_index(drop=True)
    df_merge = df_all.merge(df_latest_google, left_on='pkg_name', right_on='pkg_name', how='left')[['sha256', 'pkg_name']]
    df_merge.to_csv("../data/analysis_result/df_google_tflite_sha256_pkgname.csv", index=False, sep=',')


if __name__ == '__main__':
    main()
