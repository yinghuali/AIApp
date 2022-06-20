import pandas as pd
from google_play_scraper import app, Sort, reviews_all
from multiprocessing import Pool


def write_result(content, file_name):
    re = open(file_name, 'a')
    re.write('\n' + content)
    re.close()


def udf_google_play(s):
    if 'play.google.com' in s:
        return 'yes'
    else:
        return 'no'


def get_reviews(pkg_name):
    try:
        result = reviews_all(
                        pkg_name,
                        sleep_milliseconds=0, # defaults to 0
                        lang='en', # defaults to 'en'
                        country='us', # defaults to 'us'
                        sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
                        # filter_score_with=5 # defaults to None(means all score)
        )
    except:
        result = 'App not found'
    return result


def main_single(pkg_name_list):
    for pkg_name in pkg_name_list:
        result = pkg_name + '->'+str(get_reviews(pkg_name))
        write_result(result, 'ai_app_reviews.txt')


def main(number_single, number_pool):
    df = pd.read_csv('/mnt/irisgpfs/users/yili/pycharm/bug_detection_ai/data/df_all.csv')
    df['tag_google_play'] = df['markets'].apply(udf_google_play)
    df = df[df['tag_google_play'] == 'yes']
    pkg_name_list = list(df['pkg_name'])
    print(len(pkg_name_list)) # 50268

    number_group = len(pkg_name_list) // number_single + 1
    start = 0
    end = number_group
    data_list = []

    for i in range(number_group):
        tmp = pkg_name_list[start:end]
        data_list.append(tmp)
        start = end
        end = end+number_single

    with Pool(number_pool) as p:
        p.map(main_single, data_list)


if __name__ == '__main__':
    main(2011, 25)


