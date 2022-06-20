import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import TextCollection
import gensim
from gensim import corpora

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 200)


path_df_aiapp_review = '/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_aiapp_review.csv'
list_stopWords = list(set(stopwords.words('english')))


def udf_strlist_to_list(s_list):
    return eval(str(s_list))


def udf_len_reviews(reviews_list):
    return len(reviews_list)


def is_valid(word):
    if re.match("[()\-:;,.0-9]+", word):
        return False
    elif len(word) < 4 or word in list_stopWords or len(word) > 14:
        return False
    else:
        return True


def pic_wordcloud(dic, save_path):
    import matplotlib.pyplot as plt
    import matplotlib
    from wordcloud import WordCloud
    matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
    wordcloud = WordCloud(font_path="SimHei.ttf", background_color="white", max_font_size=80)
    wordcloud = wordcloud.fit_words(dic)
    plt.imshow(wordcloud)
    plt.savefig(save_path, format="pdf")


def get_lda_text(df):
    review_list = list(df['review_list'])
    all_review_list = []
    for i in review_list:
        all_review_list += i

    all_review_list = [i.lower() for i in all_review_list]

    list_words = [word_tokenize(review) for review in all_review_list]
    list_words_new = []
    for wordtoken_list in list_words:
        tmp = [w for w in wordtoken_list if is_valid(w)]
        list_words_new.append(tmp)

    return list_words_new


def main():
    df = pd.read_csv(path_df_aiapp_review,
                     names=['pkg_name', 'link', 'tag_metadata', 'score', 'installs', 'category', 'company', 'link_review', 'review_list'])

    df = df[df['review_list'] != '[]']

    df['review_list'] = df['review_list'].apply(udf_strlist_to_list)
    df['Number_review'] = df['review_list'].apply(udf_len_reviews)
    print('Number of AI apps:', len(df))



    top5_category_list = ['Education', 'Tools', 'Productivity', 'Photography', 'Libraries & Demo']
    for category in top5_category_list:
        df_category = df[df['category'] == category]
        doc_clean = get_lda_text(df_category)
        dictionary = corpora.Dictionary(doc_clean)
        doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
        Lda = gensim.models.ldamodel.LdaModel

        num_topics = 100
        ldamodel = Lda(doc_term_matrix, num_topics=num_topics, id2word=dictionary, passes=50)
        top_topics = ldamodel.top_topics(doc_term_matrix)
        dic = {}
        for i in range(num_topics):
            for value, key in top_topics[i][0]:
                if key not in dic:
                    dic[key] = value
                else:
                    dic[key] += value

        pic_wordcloud(dic, '/Users/yinghua.li/Documents/Pycharm/AIApps/data/picture/wordcloud'+category+'_lda.pdf')
        print('=====finished=====', category)


if __name__ == '__main__':
    main()
