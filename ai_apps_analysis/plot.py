import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from data import *


def get_dic_list_high_low(dic):
    """
    return [key1, key2], [value1, value2], high->low.

    :param dic: <dict>
    :return: <list>, [key1, key2], [value1, value2], high->low.
    """
    L = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    key_list = [i[0] for i in L]
    value_list = [i[1] for i in L]
    return key_list, value_list


def get_dic_list_low_high(dic):
    """
    return [key1, key2], [value1, value2], low->high.

    :param dic: <dict>
    :return: <list>, [key1, key2], [value1, value2], high->low.
    """
    L = sorted(dic.items(), key=lambda item: item[1], reverse=False)
    key_list = [i[0] for i in L]
    value_list = [i[1] for i in L]
    return key_list, value_list


def get_dic_list_low_high_key(dic):
    """
    return [key1, key2], [value1, value2], low->high.

    :param dic: <dict>
    :return: <list>, [key1, key2], [value1, value2], low->high.
    """
    L = sorted(dic.items(), key=lambda item: item[0], reverse=False)
    key_list = [i[0] for i in L]
    value_list = [i[1] for i in L]
    return key_list, value_list


def plot_size_ml_dl_service(dic_size_ml_dl_service):
    number_ml = len(dic_size_ml_dl_service['size_ml'])
    number_dl = len(dic_size_ml_dl_service['size_dl'])
    number_service = len(dic_size_ml_dl_service['size_service'])

    size_ml_list = sorted(list(dic_size_ml_dl_service['size_ml']))[int(number_ml*0.1): int(number_ml*0.9)]
    size_dl_list = sorted(list(dic_size_ml_dl_service['size_dl']))[int(number_dl*0.1): int(number_dl*0.9)]
    size_service_list = sorted(list(dic_size_ml_dl_service['size_service']))[int(number_service*0.1): int(number_service*0.9)]

    labels = ['ML', 'DL', 'AI Service']
    fig, ax = plt.subplots()
    ax.set_ylabel('AI Apps Size (MB)')
    plt.boxplot([size_ml_list, size_dl_list, size_service_list], labels=labels, notch=True)
    plt.savefig('../data/picture/size_ml_dl_service.pdf')


def plot_size_framework():
    number_tflite = len(dic_tflite['TfLite'])
    number_opencv = len(dic_opencv['OpenCV'])
    number_tensorflow = len(dic_tensorflow['TensorFlow'])
    number_googleai = len(dic_google_ai['Google AI'])
    number_caffe = len(dic_caffe['Caffe'])
    number_baidusyn = len(dic_baidu_synthesizer['Baidu synthesizer'])
    number_ncnn = len(dic_ncnn['NCNN'])
    number_baiduocr = len(dic_baidu_ocr['Baidu OCR'])
    number_amazonai = len(dic_amazon_ai['Amazon AI'])
    number_baidunlp = len(dic_baidu_nlp['Baidu NLP'])

    size_tflite_list = sorted(list(dic_tflite['TfLite']))[int(number_tflite*0.1): int(number_tflite*0.9)]
    size_opencv_list = sorted(list(dic_opencv['OpenCV']))[int(number_opencv * 0.1): int(number_opencv * 0.9)]
    size_tensorflow_list = sorted(list(dic_tensorflow['TensorFlow']))[int(number_tensorflow * 0.1): int(number_tensorflow * 0.9)]
    size_googleai_list = sorted(list(dic_google_ai['Google AI']))[int(number_googleai * 0.1): int(number_googleai * 0.9)]
    size_caffe_list = sorted(list(dic_caffe['Caffe']))[int(number_caffe * 0.1): int(number_caffe * 0.9)]
    size_baidusyn_list = sorted(list(dic_baidu_synthesizer['Baidu synthesizer']))[int(number_baidusyn * 0.1): int(number_baidusyn * 0.9)]
    size_ncnn_list = sorted(list(dic_ncnn['NCNN']))[int(number_ncnn * 0.1): int(number_ncnn * 0.9)]
    size_baiduocr_list = sorted(list(dic_baidu_ocr['Baidu OCR']))[int(number_baiduocr * 0.1): int(number_baiduocr * 0.9)]
    size_amazonai_list = sorted(list(dic_amazon_ai['Amazon AI']))[int(number_amazonai * 0.1): int(number_amazonai * 0.9)]
    size_baidunlp_list = sorted(list(dic_baidu_nlp['Baidu NLP']))[int(number_baidunlp * 0.1): int(number_baidunlp * 0.9)]

    labels = ['TFLite', 'OpenCV', 'TensorFlow', 'Google AI', 'Caffe', 'Baidu synthesizer', 'NCNN', 'Baidu OCR', 'Amazon AI', 'Baidu NLP']

    plt.figure(figsize=(11, 5))
    plt.ylabel('AI Apps Size (MB)')
    plt.boxplot([size_tflite_list, size_opencv_list, size_tensorflow_list, size_googleai_list, size_caffe_list, size_baidusyn_list, size_ncnn_list, size_baiduocr_list, size_amazonai_list, size_baidunlp_list], labels=labels, notch=True)
    plt.savefig('../data/picture/size_framework.pdf')


def plot_year_trend_framework():
    year_list = list(range(2008, 2022))
    def get_new_dic(dic):
        new_dic = {}
        for year in dic:
            if year in year_list:
                new_dic[year] = dic[year]
        return new_dic

    def plot(dic, title_name, path_save):
        key_list, value_list = get_dic_list_low_high_key(dic)
        plt.rcParams['figure.figsize'] = (8.0, 4.0)
        plt.plot(key_list, value_list, marker="*", linewidth=1, linestyle="--", color="gray")
        plt.title(title_name)
        plt.ylabel("Number of AI Apps")
        plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))
        plt.savefig(path_save)

    dic_year_tflite_new = get_new_dic(dic_year_tflite)
    dic_year_opencv_new = get_new_dic(dic_year_opencv)
    dic_year_tensorflow_new = get_new_dic(dic_year_tensorflow)
    dic_year_google_ai_new = get_new_dic(dic_year_google_ai)
    dic_year_caffe_new = get_new_dic(dic_year_caffe)
    dic_year_baidu_syn_new = get_new_dic(dic_year_baidu_syn)
    dic_year_ncnn_new = get_new_dic(dic_year_ncnn)
    dic_year_baidu_ocr_new = get_new_dic(dic_year_baidu_ocr)
    dic_year_amazon_ai_new = get_new_dic(dic_year_amazon_ai)
    dic_year_baidu_nlp_new = get_new_dic(dic_year_baidu_nlp)

    # plot(dic_year_tflite_new, 'TFlite', '../data/picture/trends_tflite.pdf')
    # plot(dic_year_opencv_new, 'OpenCV', '../data/picture/trends_opencv.pdf')
    # plot(dic_year_tensorflow_new, 'TensorFlow', '../data/picture/trends_tensorflow.pdf')
    # plot(dic_year_google_ai_new, 'Google AI', '../data/picture/trends_google_ai.pdf')
    # plot(dic_year_caffe_new, 'Caffe', '../data/picture/trends_caffe.pdf')
    # plot(dic_year_baidu_syn_new, 'Baidu synthesizer', '../data/picture/trends_baidu_syn.pdf')
    # plot(dic_year_ncnn_new, 'NCNN', '../data/picture/trends_ncnn.pdf')
    # plot(dic_year_baidu_ocr_new, 'Baidu OCR', '../data/picture/trends_baidu_ocr.pdf')
    # plot(dic_year_amazon_ai_new, 'Amazon AI', '../data/picture/trends_amazon_ai.pdf')
    # plot(dic_year_baidu_nlp_new, 'Baidu NLP', '../data/picture/trends_baidu_nlp.pdf')


def main():
    # plot_size_ml_dl_service(dic_size_ml_dl_service)
    # plot_size_framework()
    plot_year_trend_framework()


if __name__ == '__main__':
    main()



