import os
import pickle
from identification_config import Config
Cf = Config()


def get_ai_sha256_id(path_result):
    f = open(path_result, "r")
    lines = f.readlines()
    lines = [line for line in lines if len(line) > 20]
    res = []
    for line in lines:
        sha256_id = line.strip().split('_compile')[0].split('/')[-1]
        if len(sha256_id) == 64 and sha256_id not in res:
            res.append(sha256_id)
    return res


if __name__ == '__main__':
    sha256_id_list = get_ai_sha256_id('./result/google_sha256_list_1.txt')
    # output = open('./result/google_sha256_list_25_unique_id.pkl', 'wb')
    # pickle.dump(sha256_id_list, output)
    print(len(sha256_id_list))
    print('finish')
    # for ai_sha256 in sha256_id_list:
    #     cmd = 'echo {ai_sha256} >> ./result/result_google_sha256_list_1.txt'
    #     cmd = cmd.format(ai_sha256=ai_sha256)
    #     os.system(cmd)
