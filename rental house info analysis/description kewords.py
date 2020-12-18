import pandas as pd
import string
import nltk
import numpy
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt

'''
pre processing: https://www.kaggle.com/sudalairajkumar/getting-started-with-text-preprocessing
tf idf :https://kavita-ganesan.com/extracting-keywords-from-text-tfidf/#.X9re3FUzbt9


'''

df = pd.read_json("train.json")
# find key words from description
# find most popular region rent out
    # first preprocessing
des = df['description']
des = des.astype(str)
# 1. lowercase
des = des.str.lower()

# 2. remove punctualtion
def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text
des = des.apply(remove_punctuations)

#3. remove stop words
", ".join(stopwords.words('english'))
STOPWORDS = set(stopwords.words('english'))
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

des = des.apply(lambda text: remove_stopwords(text))

#4 lemmatization
lemmatizer = WordNetLemmatizer()
def lemmatize_words(text):
    return " ".join([lemmatizer.lemmatize(word) for word in text.split()])

des = des.apply(lambda text: lemmatize_words(text))

def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)


def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)


def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """get the feature names and tf-idf score of top n items"""

    # use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []

    # word index and corresponding tf-idf score
    for idx, score in sorted_items:
        # keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    # create a tuples of feature,score
    # results = zip(feature_vals,score_vals)
    results = {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]] = score_vals[idx]

    return results

docs = des.tolist()

cv=CountVectorizer(max_df=0.85,max_features=10000)
word_count_vector=cv.fit_transform(docs)
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)
feature_names=cv.get_feature_names()

docs = " ".join(docs)
docs = remove_html(docs)
docs = docs.replace('br','')

tf_idf_vector = tfidf_transformer.transform(cv.transform([docs]))
sorted_items = sort_coo(tf_idf_vector.tocoo())
keywords = extract_topn_from_vector(feature_names, sorted_items, 10)

plt.bar(*zip(*keywords.items()))
plt.xticks(rotation=60)
plt.savefig("des_keywords.jpg")
plt.show()
