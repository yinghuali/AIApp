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


def main_keywords_identity(path_apk_decompile):
    """
    main_keywords_identity.

    :param path_apk_decompile: <string>
    """
    for keyword in Cf.ai_code_key_words:
        shell_cmd = "ag %s -i -l --silent -m2 %s" % (keyword, path_apk_decompile)
        match = run_w(shell_cmd)
        if match:
            re = open(Cf.path_result, 'a')
            re.write('\n' + path_apk_decompile + '->' + 'keywords:' + keyword)
            re.close()
