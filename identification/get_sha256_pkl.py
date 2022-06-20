import pickle


def get_sha256_pkl(df, market, start_time, end_time, save_path):
    """
    :param df: <dataframe>, dataframe of latest.csv.
    :param market: <string>, 'appchina'、'play.google.com'
    :param start_time: <string>, '2020-00-00 00:00:00'.
    :param end_time: <string>, '2021-00-00 00:00:00'.
    :param save_path: <string>, save path of list of pkl.
    """

    df_market = df[(df['markets']==market)]
    df_market_time = df_market[(df_market['dex_date'] > start_time) & (df_market['dex_date'] < end_time)]
    sha256_list = list(df_market_time['sha256'])
    print('len(sha256_list)=', len(sha256_list))
    output = open(save_path, 'wb')
    pickle.dump(sha256_list, output)


