import os
import sys
import subprocess
from identification_config import Config
Cf = Config()


def get_so_libs(path_dir_compile):
    """
    return .so file of armeabi.

    :param path_dir_compile: <string>, path of dir_compile.
    :return: <list>, so file of armeabi.
    """
    ret = []
    if os.path.isdir(path_dir_compile):
        for root, dirs, files in os.walk(path_dir_compile, topdown=True):
            for file in files:
                file_absolute_path = os.path.join(root, file)
                if file_absolute_path.endswith('.so') and 'armeabi' in file_absolute_path:
                    ret.append(file_absolute_path)
    return ret


def decompile_so(ret, path_dir_compile):
    """

    :param path_dir_compile: <string>, path of dir_compile.
    :param ret: <list>, so file of armeabi.
    """
    for path_so in ret:
        so_command = 'readelf -p .rodata {path_so} >> {path_decompile}'
        so_command = so_command.format(path_so=path_so, path_decompile=path_dir_compile+'/'+'so.txt')
        subprocess.Popen(so_command, shell=True).wait()


def main_identify_so(path_apk_decompile):
    """
    True or False

    :param path_apk_decompile: <string>
    :param dic_so_identify: <dict>, self.so_identify
    :return: True or False
    """
    ret = get_so_libs(path_apk_decompile)
    # so file -> so.txt
    decompile_so(ret, path_apk_decompile)

    path_so_txt = path_apk_decompile+'/so.txt'

    with open(path_so_txt, 'rb') as f:
        for line in f:
            for mode_name in Cf.so_identify:
                for keyword in Cf.so_identify[mode_name]:
                    if keyword in line:
                        re = open(Cf.path_result, 'a')
                        re.write('\n' + path_apk_decompile + '->' + mode_name + ' ' + str(keyword))
                        re.close()
                        return True
    return False

