import os
import pickle


def get_sha256(path):
    ff = open(path, 'rb')
    sha256_list = pickle.load(ff)
    ff.close()
    return sha256_list


def down_apk(path_sha256_pkl):
    sha256_list = get_sha256(path_sha256_pkl)
    i = 0
    for sha256_str in sha256_list:
        down_command = 'curl -O --remote-header-name -G -d apikey=8c08e1e623110c600186098a11ba882a7e323ad32b71868510c971a504eca3f9 -d sha256={sha256} https://androzoo.uni.lu/api/download'
        down_command = down_command.format(sha256=sha256_str)
        os.system(down_command)
        i += 1
        print('finish:', i)


