import os
from identification_config import Config
Cf = Config()


def ai_model_format_identity(path_dir_compile):
    """
    return True(AI) or False(none-AI)

    :param path_dir_compile: <string>, path of dir_compile.
    :return: True or False.
    """
    if os.path.isdir(path_dir_compile):
        for root, dirs, files in os.walk(path_dir_compile, topdown=True):
            for file in files:
                file_absolute_path = os.path.join(root, file)
                for mode_format in Cf.end_model_format:
                    if file.endswith(mode_format):
                        string_result = '\n' + file_absolute_path + '->function_ai_model_format_identity, key_word->' + mode_format
                        f = open(Cf.path_result, 'a')
                        f.write('\n' + string_result)
                        f.close()
                        return True
    return False