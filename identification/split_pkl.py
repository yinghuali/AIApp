import os
import pickle


def get_sha256(path):
    ff = open(path, 'rb')
    sha256_list = pickle.load(ff)
    ff.close()
    return sha256_list


def split_two(path_pkl, save_path_0, save_path_1):
    sha256_list = get_sha256(path_pkl)
    idx = len(sha256_list) // 2
    sha256_list_0 = sha256_list[: idx]
    sha256_list_1 = sha256_list[idx: ]

    output = open(save_path_0, 'wb')
    pickle.dump(sha256_list_0, output)

    output = open(save_path_1, 'wb')
    pickle.dump(sha256_list_1, output)



