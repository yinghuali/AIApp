import pandas as pd
import os
import hashlib


path_tfmodel = '/Users/yinghua.li/Documents/Server/Models/tflite_hub'
path_save = '/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/tfmodels_hub_information.csv'


def get_model_sha256(path_file):
    f = open(path_file, "rb")
    sha256 = hashlib.sha256()
    sha256.update(f.read())
    return sha256.hexdigest()
    f.close()


def get_model_path(path_models):
    path_model = []
    if os.path.isdir(path_models):
        for root, dirs, files in os.walk(path_models, topdown=True):
            for file in files:
                file_absolute_path = os.path.join(root, file)
                if file_absolute_path.endswith('.tflite'):
                    path_model.append(file_absolute_path)
    return path_model


def main():
    path_model_list = get_model_path(path_tfmodel)
    model_sha256_list = [get_model_sha256(i) for i in path_model_list]
    model_name_list = [i.split('/')[-1] for i in path_model_list]
    task_list = [i.split('/')[-2] for i in path_model_list]
    df = pd.DataFrame(columns=['model_sha256', 'model_name', 'task'])
    df['model_sha256'] = model_sha256_list
    df['model_name'] = model_name_list
    df['task'] = task_list
    df.to_csv('../data/analysis_result/tf_hub_model_information.csv', index=False, sep=',')


if __name__ == '__main__':
    main()
