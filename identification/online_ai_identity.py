import os
import logging
from identification_config import Config
Cf = Config()


def run_w(shell_cmd):
    """
    run shell cmds with result returned
    """
    #logging.debug("executing shell cmd : " + shell_cmd)
    try:
        res = os.popen(shell_cmd).read().strip()
    except:
        logging.error("error in executing : " + shell_cmd)
        res = ""
    return res


# ag "firebase/ml/vision/cloud" smali*/ -l
def get_Google_AI(decpath):
    """
    return None or string(path which file content contain keywords).

    :param decpath: <string>, path of dir_compile.
    :return: None or string.
    """
    shell_cmd = "ag %s -i -l --silent -m2 %s" % ("firebase/ml/vision/cloud", decpath)
    match = run_w(shell_cmd)
    return match


# ag "com.amplifyframework.predictions" smali*/ -l
def get_Amazon_AI(decpath):
    shell_cmd = "ag %s -i -l --silent -m2 %s" % ("com.amplifyframework.predictions", decpath)
    match = run_w(shell_cmd)
    return match


# ag "alexaDeepLink" smali*/ -l
def get_Alexa_AI(decpath):
    shell_cmd = "ag %s -i -l --silent -m2 %s" % ("alexaDeepLink", decpath)
    match = run_w(shell_cmd)
    return match


# ag "alexaDeepLink" smali*/ -l
# compile group: 'com.azure', name: 'azure-ai-textanalytics', version: '5.1.0-beta.1'
def get_Azure_AI(decpath):
    shell_cmd = "ag %s -i -l --silent -m2 %s" % ("azure-ai", decpath)
    match = run_w(shell_cmd)
    return match


def is_Baidu_NLP(libs):
    if 'BaiduSpeechSDK' in libs:
        return True
    else:
        return False


def is_Baidu_synthesizer(libs):
    if 'BDSpeechDecoder' in libs:
        return True
    else:
        return False


def is_Baidu_OCR(libs):
    if 'ocr-sdk' in libs:
        return True
    else:
        return False


def get_libs_so_name(apk_decompile_path):
    """
    return "a.so b.so "
    :param path_lib: <string>, apk_decompile_path.
    :return: <string>, "a.so b.so "
    """
    path_lib = apk_decompile_path + '/lib'
    libs = ''
    for subdir, dirs, files in os.walk(path_lib):
        for file in files:
            libs += os.path.basename(file) + ' '
    return libs


def main_identify_online_ai(path_apk_decompile):
    """
    True or False

    :param path_apk_decompile: <string>
    :param dic_so_identify: <dict>, self.so_identify
    :return: True or False
    """
    libs = get_libs_so_name(path_apk_decompile)
    if is_Baidu_NLP(libs):
        re = open(Cf.path_result, 'a')
        re.write('\n' + path_apk_decompile + '->' + 'Baidu_NLP')
        re.close()
        return True
    elif is_Baidu_synthesizer(libs):
        re = open(Cf.path_result, 'a')
        re.write('\n' + path_apk_decompile + '->' + 'Baidu_synthesizer')
        re.close()
        return True
    elif is_Baidu_OCR(libs):
        re = open(Cf.path_result, 'a')
        re.write('\n' + path_apk_decompile + '->' + 'Baidu_OCR')
        re.close()
        return True

    else:
        if get_Google_AI(path_apk_decompile):
            re = open(Cf.path_result, 'a')
            re.write('\n' + path_apk_decompile + '->' + 'Google_AI')
            re.close()
            return True
        elif get_Amazon_AI(path_apk_decompile):
            re = open(Cf.path_result, 'a')
            re.write('\n' + path_apk_decompile + '->' + 'Amazon_AI')
            re.close()
            return True
        elif get_Alexa_AI(path_apk_decompile):
            re = open(Cf.path_result, 'a')
            re.write('\n' + path_apk_decompile + '->' + 'Alexa_AI')
            re.close()
            return True
        elif get_Azure_AI(path_apk_decompile):
            re = open(Cf.path_result, 'a')
            re.write('\n' + path_apk_decompile + '->' + 'Azure_AI')
            re.close()
            return True
    return False


# if __name__ == '__main__':
#
#     target = main_identify_online_ai('/home/yinghua/pycharm/MobileModelIdentif/Test/apk_decompile')
#     print(target)




