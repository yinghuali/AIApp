import faulthandler
faulthandler.enable()
import pandas as pd
import tensorflow as tf
import os
from analysis_config import Config
Cf = Config()


class AnalysisLayer:

    def __init__(self):
        self.dic = {}
        self.number_models = 0
        self.dic_layer_count = dict(zip(Cf.layer_list, [0] * len(Cf.layer_list)))
        self.dic_layer_count_ratio = {}

    def save_result(self, path_resutl, content):
        """
        :param path_resutl: <string>, path of result.
        :param content: <string>, analysis results.
        """
        string_result = '\n' + content
        f = open(path_resutl, 'a')
        f.write('\n' + string_result)
        f.close()

    def get_model_path(self, path_models):
        path_model = []
        for root, dirs, files in os.walk(path_models, topdown=True):
            for file in files:
                file_absolute_path = os.path.join(root, file)
                if file_absolute_path.endswith('.tflite'):
                    path_model.append(file_absolute_path)
        return path_model

    def check_models(self, path):
        tflite_model = tf.lite.Interpreter(model_path=path)
        tflite_model.allocate_tensors()
        layer_details = tflite_model.get_tensor_details()
        layer_list = [i['name'] for i in layer_details if len(i['name']) > 0]
        for key in self.dic_layer_count:
            for layer in layer_list:
                if key.lower() in layer.lower():
                    self.dic_layer_count[key] += 1
                    break
        self.number_models += 1

    def main(self):
        df_modelpath_entropy = pd.read_csv('df_modelpath_entropy.csv', names=['model_path', 'entropy'])
        path_model_list = list(df_modelpath_entropy[df_modelpath_entropy['entropy'] < 7]['model_path'])
        for path in path_model_list:
            try:
                self.check_models(path)
            except:
                pass
        print(self.number_models)
        print(self.dic_layer_count)
        for key in self.dic_layer_count:
            self.dic_layer_count_ratio[key] = self.dic_layer_count[key] * 1.0 / self.number_models

        df_name_count = pd.DataFrame(columns=['layer_name', 'count'])
        df_name_ratio = pd.DataFrame(columns=['layer_name', 'ratio'])
        df_name_count['layer_name'] = list(self.dic_layer_count.keys())
        df_name_count['count'] = list(self.dic_layer_count.values())
        df_name_ratio['layer_name'] = list(self.dic_layer_count_ratio.keys())
        df_name_ratio['ratio'] = list(self.dic_layer_count_ratio.values())
        df_merge = df_name_count.merge(df_name_ratio, left_on='layer_name', right_on='layer_name', how='inner')

        self.save_result('./analysis_models_layers_count.csv', 'number of models: ' + str(self.number_models))
        df_merge = df_merge.sort_values(by=['count'], ascending=False)
        df_merge.to_csv('./analysis_models_layers.csv', index=False, sep=',')
        print('========all finished=========')


if __name__ == '__main__':
    AL = AnalysisLayer()
    AL.main()
