import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 200)

path_model_size = '/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_model_path_size.csv'
path_lightweight_model = '/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_lightweight_model.csv'


def count_int8_value(pdf):
    return sum(pdf['label_int8'])


def main():
    df_modelpath_size = pd.read_csv(path_model_size, names=['model_path', 'size'])
    df_lightweight_model = pd.read_csv(path_lightweight_model)
    df = df_lightweight_model.merge(df_modelpath_size, left_on='path', right_on='model_path', how='left')
    count_int8 = count_int8_value(df[df['size'] <= 2])
    print("len(df[df['size'] <= 2])", len(df[df['size'] <= 2]), count_int8)
    count_int8 = count_int8_value(df[(df['size'] > 2) & (df['size'] <= 4)])
    print("len(df[(df['size'] > 2) & (df['size'] <= 4)])", len(df[(df['size'] > 2) & (df['size'] <= 4)]), count_int8)
    count_int8 = count_int8_value(df[(df['size'] > 4) & (df['size'] <= 6)])
    print("len(df[(df['size'] > 4) & (df['size'] <= 6)])", len(df[(df['size'] > 4) & (df['size'] <= 6)]), count_int8)
    count_int8 = count_int8_value(df[(df['size'] > 6) & (df['size'] <= 8)])
    print("len(df[(df['size'] > 6) & (df['size'] <= 8)])", len(df[(df['size'] > 6) & (df['size'] <= 8)]), count_int8)
    count_int8 = count_int8_value(df[(df['size'] > 8) & (df['size'] <= 10)])
    print("len(df[(df['size'] > 8) & (df['size'] <= 10)])", len(df[(df['size'] > 8) & (df['size'] <= 10)]), count_int8)

    count_int8 = count_int8_value(df[(df['size'] > 10) & (df['size'] <= 20)])
    print("len(df[(df['size'] > 10) & (df['size'] <= 20)])", len(df[(df['size'] > 10) & (df['size'] <= 20)]), count_int8)

    count_int8 = count_int8_value(df[(df['size'] > 20) & (df['size'] <= 30)])
    print("len(df[(df['size'] > 20) & (df['size'] <= 30)])", len(df[(df['size'] > 20) & (df['size'] <= 30)]), count_int8)

    count_int8 = count_int8_value(df[(df['size'] > 30) & (df['size'] <= 40)])
    print("len(df[(df['size'] > 30) & (df['size'] <= 40)])", len(df[(df['size'] > 30) & (df['size'] <= 40)]), count_int8)

    count_int8 = count_int8_value(df[(df['size'] > 40) & (df['size'] <= 50)])
    print("len(df[(df['size'] > 40) & (df['size'] <= 50)])", len(df[(df['size'] > 40) & (df['size'] <= 50)]), count_int8)

    count_int8 = count_int8_value(df[df['size'] > 50])
    print("len(df[df['size'] > 50])", len(df[df['size'] > 50]), count_int8)






if __name__ == '__main__':
    main()

