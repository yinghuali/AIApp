import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib

from analysis_config import Config
Cf = Config()


def udf_get_text_list(text):
    text = str(text)
    res = []
    tmp_sentence = ''
    for i in text:
        tmp_sentence += i
        if i == '\n':
            if len(tmp_sentence.strip()) > 20:
                res.append(tmp_sentence.strip())

            tmp_sentence = ''
    return res


def pic_wordcloud(dic, save_path):
    df = pd.DataFrame({
        'word': list(dic.keys()),
        'count': list(dic.values())})
    matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)

    wordcloud = WordCloud(font_path="SimHei.ttf", background_color="white", max_font_size=80)
    word_frequence = {x[0]: x[1] for x in df.values}
    wordcloud = wordcloud.fit_words(word_frequence)
    plt.savefig(save_path)
    plt.imshow(wordcloud)
    plt.savefig(save_path, format="pdf")


def main():
    df = pd.read_csv('/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_google_privacy.csv',
                     names=['pkg_name', 'link', 'tag_metadata', 'score', 'installs', 'category', 'company', 'privacy_url', 'privacy_data'])
    df = df[df['privacy_data'] != 'Wrong']

    df['privacy_data_list'] = df['privacy_data'].apply(udf_get_text_list)
    print('Number of AI apps:', len(df))
    print('Number of AI apps(success to catefory and privacy):', len(df[df['category']!='Wrong']))

    print(Cf.privacy_concerns_keywords)
    dic = dict(zip(Cf.privacy_concerns_keywords, [0] * len(Cf.privacy_concerns_keywords)))
    print(dic)

    category_list = list(set(df['category']))
    print(len(category_list))

    category_list.remove('Wrong')
    category_list_number = [len(df[df['category'] == category]) for category in category_list]
    dic_ = dict(zip(category_list, category_list_number))
    top10_list = sorted(dic_.items(), key=lambda item: item[1], reverse=True)[:10]

    print('number of AI apps of Top10 categories')
    print(top10_list)

    for category_tuple in top10_list:

        print(category_tuple)
        tmp_df = df[df['category'] == category_tuple[0]]

        dic = dict(zip(Cf.privacy_concerns_keywords, [0] * len(Cf.privacy_concerns_keywords)))

        def count_dic(text_list):
            for key in dic:
                for sentence in text_list:
                    if key in sentence:
                        dic[key] += 1
                        break

        privacy_data_list = list(tmp_df['privacy_data_list'])

        for text_list in privacy_data_list:
            count_dic(text_list)

        keywords_list = list(dic.keys())
        number_aiapps = list(dic.values())
        df_re = pd.DataFrame(columns=['privacy', 'number_aiapps'])
        df_re['privacy'] = keywords_list
        df_re['number_aiapps'] = number_aiapps
        df_re['ratio'] = df_re['number_aiapps'] * 1.0 / category_tuple[1]
        df_re = df_re.sort_values(by=['number_aiapps'], ascending=False).reset_index(drop=True)
        print(df_re)
        print('=================')


if __name__ == '__main__':
    main()

