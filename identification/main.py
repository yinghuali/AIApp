import os
from identification_config import Config
from down_APK import get_sha256
from apk_single_decompile import apk_decompile, get_string_dex
from extract_so_identity import main_identify_so
from online_ai_identity import main_identify_online_ai
from deep_model_identify import ai_model_format_identity
from keywords_identity import main_keywords_identity

Cf = Config()

current_path = Cf.current_path


def main(path_sha256_list):

    sha256_list = get_sha256(path_sha256_list)
    i = 0
    for sha256_str in sha256_list:
        down_command = 'curl -O --remote-header-name -G -d apikey=8c08e1e623110c600186098a11ba882a7e323ad32b71868510c971a504eca3f9 -d sha256={sha256} https://androzoo.uni.lu/api/download'
        down_command = down_command.format(sha256=sha256_str)
        os.system(down_command)

        try:
            path_apk = current_path + '/' + sha256_str + '.apk'
            print('==apk_decompile start==')
            path_apk_decompile = apk_decompile(path_apk, current_path)
            get_string_dex(path_apk_decompile)
            print('==apk_decompile finished==')
        except:
            pass

        # model file identify
        try:
            target_model = ai_model_format_identity(path_apk_decompile)
        except:
            print('error：ai_model_format_identity')

        # so file identify
        try:
            target_so = main_identify_so(path_apk_decompile)
        except:
            print('error：main_identify_so')

        # Scan all files and content
        try:
            target_online = main_identify_online_ai(path_apk_decompile)
        except:
            print('error: main_identify_online_ai')

        try:
            target_keywords = main_keywords_identity(path_apk_decompile)
        except:
            print('error: main_keywords_identity')

        i += 1
        print('sha256_str finished:', i)
        print(sha256_str)

        rm_apk_command = 'rm ' + sha256_str + '.apk'
        # rm_apk_decompile = 'rm -rf ' + sha256_str + '_compile'

        os.system(rm_apk_command)
        # os.system(rm_apk_decompile)


if __name__ == '__main__':
    main('/Users/yinghua.li/Documents/Pycharm/data/3.pkl')