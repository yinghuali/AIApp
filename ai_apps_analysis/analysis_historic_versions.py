import pandas as pd


def main():
    df_history_ai_sha256_list = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_history_ai_sha256_list.csv')
    df_latest = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/latest.csv')
    df_merge = df_history_ai_sha256_list.merge(df_latest, left_on='ai_sha256_id', right_on='sha256', how='left')
    df_merge = df_merge.dropna(subset=['sha256'])
    df_merge['count'] = 1
    df_groupby = df_merge.groupby('pkg_name').agg({'count': 'sum'}).reset_index()
    pkg_name_list = list(df_groupby[df_groupby['count'] >= 2]['pkg_name'])

    def udf_tag_pkg_name(s):
        if s in pkg_name_list:
            return 1
        return 0

    def udf_split(s):
        return s.split('key_word->')[-1]

    df_merge['tag'] = df_merge['pkg_name'].apply(udf_tag_pkg_name)
    df_merge = df_merge[df_merge['tag'] == 1]
    df_merge['information_split'] = df_merge['information'].apply(udf_split)

    dic_all = {}
    dic_empty = {}
    for pkg_name, pdf in df_merge.groupby('pkg_name'):
        tmp_df = pdf.sort_values(by=['dex_date'], ascending=True).copy()
        framework_list = list(tmp_df['framework_list'])
        if len(set(framework_list)) > 1 and len(set(framework_list)) < len(framework_list):
            dic_all[pkg_name] = framework_list
        elif '[]' in framework_list:
            dic_empty[pkg_name] = framework_list


    print('Number of AI Apps that have different AI frameworks in different versions:', len(dic_all))
    print('No frameworks with information:', set(df_merge[df_merge['framework_list'] == '[]']['information_split']))


if __name__ == '__main__':
    main()
