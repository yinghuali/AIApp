import pandas as pd
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 200)


def udf_get_input_shape(s):
    return s.split('_YY_')[0].strip()


def udf_get_output_shape(s):
    return s.split('_YY_')[-1].strip()


def main():
    df_all = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_all.csv')
    df = pd.read_csv('../data/analysis_result/data_feed_aiapps.csv',
                     names=['sha256', 'model_name', 'path_model', 'shape'])
    df_merge = df.merge(df_all, left_on='sha256', right_on='sha256', how='inner')
    df_merge = df_merge[df_merge['shape'] != 'Wrong']

    print('Number of AI app:', len(set(df_merge['pkg_name'])))
    print('Number of AI models:', len(df_merge))

    df_merge['input_shape'] = df_merge['shape'].apply(udf_get_input_shape)
    df_merge['output_shape'] = df_merge['shape'].apply(udf_get_output_shape)
    df_merge = df_merge[df_merge['input_shape'] != '[]']
    df_merge = df_merge[df_merge['output_shape'] != '[]']

    df_merge['input_count'] = 1
    df_input = df_merge.groupby('input_shape').agg({'input_count': 'sum'}).reset_index().sort_values(by=['input_count'], ascending=False).reset_index(drop=True)
    df_input['ratio'] = df_input['input_count'] * 1.0 / len(df_merge)
    print('df_input.head(10)')
    print(df_input.head(10))
    print('==========================================')

    df_merge['output_count'] = 1
    df_output = df_merge.groupby('output_shape').agg({'output_count': 'sum'}).reset_index().sort_values(by=['output_count'], ascending=False).reset_index(drop=True)
    df_output['ratio'] = df_output['output_count'] * 1.0 / len(df_merge)
    print('df_output.head(10)')
    print(df_output.head(10))
    print('==========================================')

    df_merge['count'] = 1
    df_input_model = df_merge[df_merge['input_shape'] == '[  1 320 320   1]'].groupby('model_name').agg({'input_count': 'sum'}).reset_index()
    df_input_model['ratio'] = df_input_model['input_count'] / len(df_merge)
    df_input_model = df_input_model.sort_values(by=['input_count'], ascending=False).reset_index(drop=True)
    print('df_input_model')
    print(df_input_model)
    print('==========================================')

    df_merge['count'] = 1
    df_input_model = df_merge[df_merge['input_shape'] == '[  1 320 320   3]'].groupby('model_name').agg({'input_count': 'sum'}).reset_index()
    df_input_model['ratio'] = df_input_model['input_count'] / len(df_merge)
    df_input_model = df_input_model.sort_values(by=['input_count'], ascending=False).reset_index(drop=True)
    print('df_input_model.head(10)')
    print(df_input_model.head(10))
    print('==========================================')

    df_merge['count'] = 1
    df_output_model = df_merge[df_merge['output_shape'] == '[ 1 20 20 48]'].groupby('model_name').agg({'output_count': 'sum'}).reset_index()
    df_output_model['ratio'] = df_output_model['output_count'] / len(df_merge)
    df_output_model = df_output_model.sort_values(by=['output_count'], ascending=False).reset_index(drop=True)
    print('df_output_model.head(10)')
    print(df_output_model.head(10))
    print('==========================================')

    df_merge['count'] = 1
    df_re = df_merge.groupby('model_name').agg({'count': 'sum'}).reset_index()
    df_re = df_re.sort_values(by=['count'], ascending=False).reset_index(drop=True)
    df_re['ratio'] = df_re['count'] / len(df_merge)
    print("df_re[['model_name', 'count', 'ratio']].head()")
    print(df_re[['model_name', 'count', 'ratio']].head())
    print('==========================================')


if __name__ == '__main__':
    main()
