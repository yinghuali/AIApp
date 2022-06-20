import pandas as pd
import pickle


def main():
    df_latest = pd.read_csv('/home/yinghua/pycharm/AIApps/data/latest.csv')
    df_latest_new = df_latest[['sha256', 'pkg_name', 'markets']].copy()
    df_all = pd.read_csv('/home/yinghua/pycharm/AIApps/data/analysis_result/df_all.csv')
    pkg_name_list = list(df_all['pkg_name'])

    def udf_pkgname_tag(s):
        if s in pkg_name_list:
            return 1
        return 0

    df_latest_new['history_tag'] = df_latest_new['pkg_name'].apply(udf_pkgname_tag)

    df_latest_new = df_latest_new[df_latest_new['history_tag'] == 1].reset_index(drop=True)

    df_latest_new.to_csv('df_latest_new.csv', index=False, sep=',')

    pkgname_list = list(df_all['pkg_name'])
    markets_list = list(df_all['markets'])

    def udf_pkgname_tag(s):
        pkg_name = s[0]
        market = s[1]

        for i in range(len(pkgname_list)):
            if pkg_name == pkgname_list[i] and market == markets_list[i]:
                return 1
        return 0

    df_latest_new['history_tag_new'] = df_latest_new[['pkg_name', 'markets']].apply(udf_pkgname_tag, axis=1)
    df_latest_new_tag = df_latest_new[df_latest_new['history_tag_new'] == 1]
    df_latest_new_tag.to_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_latest_new_tag.csv', index=False, sep=',')

    history_ai_sha256_list = list(df_latest_new_tag['sha256'])

    output = open('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/history_ai_sha256_list.pkl', 'wb')
    pickle.dump(history_ai_sha256_list, output)


if __name__ == '__main__':
    main()



