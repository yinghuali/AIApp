import pandas as pd
import matplotlib.pyplot as plt


def udf_get_sha256(s):
    return s.split('_YY_')[0].split('/')[-1].strip()


def udf_get_modelname(s):
    return s.split('_YY_')[-1].strip()


def plot_pic(df_merge, save_path):
    y = list(sorted(list(df_merge['entropy'])))
    x = list(range(len(df_merge['entropy'])))
    plt.plot(x, y, color="black")
    plt.xlabel("204,830 Models Collected from AndroZoo")
    plt.ylabel("Entropy")
    plt.grid(True)
    plt.rcParams['figure.figsize'] = (20, 5)
    plt.savefig(save_path)


def main():
    df = pd.read_csv('../data/analysis_result/df_modelpath_entropy.csv', names=['model_path', 'entropy'])
    df_latest = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/latest.csv')
    df['sha256_app'] = df['model_path'].apply(udf_get_sha256)
    df['model_name'] = df['model_path'].apply(udf_get_modelname)
    df_merge = df.merge(df_latest, left_on='sha256_app', right_on='sha256', how='left')
    df_merge.to_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_modelpath_entropy_latest.csv', index=False, sep=',')
    plot_pic(df_merge, '/Users/yinghua.li/Documents/Pycharm/AIApps/data/picture/model_entropy.pdf')
    print('entropy>=7.99:', len(df_merge[df_merge['entropy'] >= 7.99]))

    df_google_apps_characteristic = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_google_apps_characteristic.csv')
    df_merge = df_merge.merge(df_google_apps_characteristic, left_on='pkg_name', right_on='pkg_name', how='left')
    df_merge_encrypted = df_merge[df_merge['entropy'] >= 7.99]
    dic_pkgname_company = dict(zip(list(df_merge_encrypted['pkg_name']), list(df_merge_encrypted['company'])))
    dic_pkgname_category = dict(zip(list(df_merge_encrypted['pkg_name']), list(df_merge_encrypted['category'])))
    print(dic_pkgname_category)
    print(dic_pkgname_category)


if __name__ == '__main__':
    main()
