import pandas as pd
import re
import json
import nltk

from nltk import word_tokenize
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.cluster import KMeans

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# For testing from assigment
tweets = pd.read_pickle('new_4.pkl')

# This needs work since it still lets through some garbage input
def tokenize(s):
  #re_url = re.compile(re.compile(r'(https?:\/\/[www\.]?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-z]{2,6}\b[-a-zA-Z0-9@:%_\+.~#?&//=]*)'))
  re_url = re.compile(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')
  re_hashtag = re.compile(r'\B#\w*[a-zA-Z]+\w*')
  re_emoji = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)
  re_punctuation = re.compile(r'[,.!?@\'\"`]')

  urls = re_url.findall(s)
  hashtags = re_hashtag.findall(s)
  emojis = re_emoji.findall(s)

  s = re.sub(re_url,'',s)
  s = re.sub(re_hashtag,'',s)
  s = re.sub(re_emoji,'',s)
  s = re.sub(re_punctuation, '', s)
  s = s.lower()

  return word_tokenize(s)

  def lemmatize(s):
  lemmas = []
  wordnet_lemmatizer = WordNetLemmatizer()
  for word in s:
    if word not in stop_words:
      lemmatized = wordnet_lemmatizer.lemmatize(word)
      lemmas.append(lemmatized)
      return lemmas

def topics(l):
  tfidf = TfidfVectorizer()
  tfs = tfidf.fit_transform(l)
  feature_names = tfidf.get_feature_names()

  km = KMeans(n_clusters=2)
  km.fit(tfs)
  order_centroids = km.cluster_centers_.argsort()[:, ::-1]

  for i in range(len(order_centroids)):
    print("Cluster %d:" % i, end='')
    for ind in order_centroids[i, :15]:
      print(' %s' % feature_names[ind], end=',')
      print()

def process(df):
  df = df.sort_values(by='id')
  df = df.drop_duplicates(['id'])

  agg = []
  for index, row in df.iterrows():
    lemmas = lemmatize(tokenize(row.full_text))
    for lemma in lemmas:
      agg.append(lemma)

  topics(agg)

process(tweets)
