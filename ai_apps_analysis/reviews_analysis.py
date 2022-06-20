import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 2000)

path_df_aiapp_review = '/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/df_aiapp_review.csv'

# dic_review_label = {'Great application': ['great', 'excellent', 'perfect'],
#                     'Good application': ['good', 'well'],
#                     'Love the application': ['love'],
#                     'Nice application': ['nice'],
#                     'Cool application': ['cool'],
#                     'Fun application': ['fun'],
#                     'Easy to use': ['easy'],
#                     'Awesome application': ['awesome'],
#                     'Friendly application': ['friendly'],
#                     'Application works great/ Application does not work': ['work'],
#                     'Voice issues': ['voice'],
#                     'Bad application': ['bad', 'hate'],
#                     'Helpful application': ['help'],
#                     'Update-related issue': ['update'],
#                     'Convenient application': ['convenient']}


new_review_label = ['machine learning',
                    'deep learning',
                    'audio command detection',
                    'audio embedding',
                    'audio event classification',
                    'audio pitch extraction',
                    'audio speech synthesis',
                    'audio synthesis',
                    'speech to text',
                    'image augmentation',
                    'image classification',
                    'image classifier',
                    'image depth estimation',
                    'image extrapolation',
                    'image feature vector',
                    'image generator',
                    'image object detection',
                    'image pose detection',
                    'image rnn agent',
                    'image segmentation',
                    'image style transfer',
                    'image super resolution',
                    'image text detection',
                    'image text recognition',
                    'text classification',
                    'text embedding',
                    'text generation',
                    'text language model',
                    'text preprocessing',
                    'text question answering',
                    'text segmentation',
                    'text to MEL',
                    'video audio text',
                    'video classification',
                    'video generation',
                    'video text',

                    'command detection',
                    'event classification',
                    'pitch extraction',
                    'speech synthesis',
                    'object detection',
                    'pose detection',
                    'rnn agent',
                    'style transfer',
                    'super resolution',
                    'text detection',
                    'text recognition',
                    'language model',
                    'classification',
                    'language model',

                    'TensorFlow',
                    'TfLite',
                    'Pytorch',
                    'OpenCV',
                    'Google AI',
                    'Amazon AI',
                    'Alexa AI',
                    'Azure AI',
                    'Baidu NLP',
                    'Baidu synthesizer',
                    'Baidu OCR',
                    'Caffe2'
                    ]

dic = {'cc.nextlabs.scikitlearn': 'Books & Reference',
       'ch.icoaching.typewise': 'Personalisation',
       'com.aex.aexApp': 'Finance',
       'com.aikeral.gallery': 'Tools',
       'com.amit.bhashadarshak': 'Productivity',
       'com.andreyaleev.opencvfilters': 'Video Players & Editors',
       'com.app.android.dentulu': 'Medical',
       'com.appxy.tinyscanner': 'Business',
       'com.chessbaseindia.app': 'Sports',
       'com.dpthinker.astyletransfer': 'Tools',
       'com.google.android.apps.cultural': 'Education',
       'com.google.android.apps.village.boond': 'Tools',
       'com.handled.home': 'House & Home',
       'com.hierlsoftware.picsort': 'Photography',
       'com.idealmatch.idma': 'Dating',
       'com.iugulus.scanongo': 'Productivity',
       'com.pobeda.ivan.opencvdetect': 'Tools',
       'com.smtools.textrecognition': 'Tools',
       'com.telestra.art.painting.artistic.photography': 'Photography',
       'com.toucan.speak': 'Tools',
       'com.trestle.labs.kibo': 'Productivity',
       'com.zepplaud.slate': 'Education',
       'easy.text.recognizer.ocr': 'Tools',
       'freelearn.python.datascience': 'Education',
       'lifegoal.helpinghands.machinelearningwithpython': 'Education',
       'me.guyca.kippi': 'Productivity',
       'net.kajos.realairesizer': 'Photography',
       'org.fossasia.phimpme': 'Social',
       'org.mozilla.screenshot.go': 'Tools'}


def get_transform_df(df):
    pkg_name_list = list(df['pkg_name'])
    score_list = list(df['score'])
    installs_list = list(df['installs'])
    category_list = list(df['category'])
    company_list = list(df['company'])

    review_list = list(df['review_list'])

    new_pkg_name_list = []
    new_score_list = []
    new_installs_list = []
    new_category_list = []
    new_company_list = []
    new_review_list = []
    for i in range(len(df)):
        number_reviews = len(review_list[i])
        new_pkg_name_list += [pkg_name_list[i]] * number_reviews
        new_score_list += [score_list[i]] * number_reviews
        new_installs_list += [installs_list[i]] * number_reviews
        new_category_list += [category_list[i]] * number_reviews
        new_company_list += [company_list[i]] * number_reviews
        new_review_list += review_list[i]
    df_re = pd.DataFrame(columns=['pkg_name'])
    df_re['pkg_name'] = new_pkg_name_list
    df_re['new_score'] = new_score_list
    df_re['installs'] = new_installs_list
    df_re['category'] = new_category_list
    df_re['company'] = new_company_list
    df_re['review'] = new_review_list
    return df_re


def udf_strlist_to_list(s_list):
    return eval(str(s_list))


if __name__ == '__main__':

    df = pd.read_csv(path_df_aiapp_review,
                     names=['pkg_name', 'link', 'tag_metadata', 'score', 'installs', 'category', 'company',
                            'link_review', 'review_list'])

    df = df[df['review_list'] != '[]']

    df['review_list'] = df['review_list'].apply(udf_strlist_to_list)
    df_re = get_transform_df(df)


    def udf_review_tag(review):
        res = []
        for label in new_review_label:
            if label.lower() in review.lower():
                res.append(label)
        return str(res)


    df_re['label'] = df_re['review'].apply(udf_review_tag)
    df_re = df_re[df_re['label'] != '[]'].reset_index(drop=True)


    def get_category(df_re, dic):
        res_category = []
        pkg_name_list = list(df_re['pkg_name'])
        category_list = list(df_re['category'])
        for i in range(len(df_re)):
            if pkg_name_list[i] in dic:
                res_category.append(dic[pkg_name_list[i]])
            else:
                res_category.append(category_list[i])
        df_re['category'] = res_category
        return df_re


    df_re = get_category(df_re, dic)
    df_re = df_re[df_re['category'] != 'Wrong']
    print('Number of reviews of AI:', len(df_re))
    print('Number of AI Apps:', len(set(df_re['pkg_name'])))

    df_re['number_of_reviews'] = 1
    df_number_reviews = df_re.groupby('category').agg('sum')['number_of_reviews'].reset_index().sort_values(
        by=['number_of_reviews'], ascending=False).reset_index(drop=True)
    print(df_number_reviews)

    df_re['number_of_reviews'] = 1
    df_number_reviews_category = df_re.groupby(['category', 'label']).agg('sum')[
        'number_of_reviews'].reset_index().sort_values(by=['category', 'label', 'number_of_reviews'],
                                                       ascending=False).reset_index(drop=True)

    print(df_number_reviews_category)