import pandas as pd
import re
from text_rank import TextRank4Keyword

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import TextCollection
list_stopWords = list(set(stopwords.words('english')))

path_df_aiapp_review = '/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_aiapp_review.csv'


def is_valid(word):
    if re.match("[()\-:;,.0-9]+", word):
        return False
    elif len(word) < 4 or word in list_stopWords or len(word) > 14:
        return False
    else:
        return True


def udf_strlist_to_list(s_list):
    return eval(str(s_list))


def udf_len_reviews(reviews_list):
    return len(reviews_list)


def get_textrank(df):
    review_list = list(df['review_list'])
    all_review_list = []
    for i in review_list:
        all_review_list += i

    all_review_list = [i.lower() for i in all_review_list]

    list_words = [word_tokenize(review) for review in all_review_list]
    text = ''
    for wordtoken_list in list_words:
        tmp = [w for w in wordtoken_list if is_valid(w)]
        s = " ".join(tmp)
        text += s
    return text


def pic_wordcloud(dic, save_path):
    import matplotlib.pyplot as plt
    import matplotlib
    from wordcloud import WordCloud
    matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
    wordcloud = WordCloud(font_path="SimHei.ttf", background_color="white", max_font_size=80)
    wordcloud = wordcloud.fit_words(dic)
    plt.imshow(wordcloud)
    plt.savefig(save_path, format="pdf")


def main():
    df = pd.read_csv(path_df_aiapp_review,
                     names=['pkg_name', 'link', 'tag_metadata', 'score', 'installs', 'category', 'company', 'link_review', 'review_list'])

    df = df[df['review_list'] != '[]']

    df['review_list'] = df['review_list'].apply(udf_strlist_to_list)
    df['Number_review'] = df['review_list'].apply(udf_len_reviews)
    print('Number of AI apps:', len(df))

    top5_category_list = ['Finance', 'Tools', 'Photography', 'Business', 'Education']
    for category in top5_category_list:
        df_category = df[df['category'] == category]
        text = get_textrank(df_category)

        tr4w = TextRank4Keyword()
        tr4w.analyze(text, candidate_pos=['NOUN', 'PROPN'], window_size=4, lower=False)
        dic_word_rank = tr4w.get_keywords()
        pic_wordcloud(dic_word_rank, '/Users/yinghua.li/Documents/Pycharm/AIApps/data/picture/wordcloud'+category+'_textrank.pdf')
        print('=====finished=====', category)


if __name__ == '__main__':
    main()
