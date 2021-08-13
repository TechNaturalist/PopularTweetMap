from typing import List
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

from sentiment_analysis.TweetSentiment import TweetSentiment

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# This needs work since it still lets through some garbage input
def tokenize(s):
  re_url = re.compile(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')
  re_hashtag = re.compile(r'\B#\w*[a-zA-Z]+\w*')
  re_emoji = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)
  re_punctuation = re.compile(r'[,.!?@\'\"`]')
  re_handles = re.compile(r'@[\w]*')

  urls = re_url.findall(s)
  hashtags = re_hashtag.findall(s)
  emojis = re_emoji.findall(s)

  s = re.sub(re_url,'',s)
  s = re.sub(re_hashtag,'',s)
  s = re.sub(re_emoji,'',s)
  s = re.sub(re_handles, '', s)
  s = re.sub(re_punctuation, '', s)
  s = s.lower()

  return word_tokenize(s)

def lemmatize(s):
  if s == None:
    return None

  lemmas = []
  wordnet_lemmatizer = WordNetLemmatizer()
  for word in s:
    if word not in stop_words:
      lemmatized = wordnet_lemmatizer.lemmatize(word)
      lemmas.append(lemmatized)
  return lemmas

def topics(l):
  if l == None:
    return None

  tfidf = TfidfVectorizer()
  tfs = tfidf.fit_transform(l)
  feature_names = tfidf.get_feature_names()

  km = KMeans(n_clusters=2)
  km.fit(tfs)
  order_centroids = km.cluster_centers_.argsort()[:, ::-1]

  for i in range(len(order_centroids)):
    for ind in order_centroids[i, :5]:
      print(' %s' % feature_names[ind], end=',')
      print()

  if len(feature_names) > 5:
    feature_names = feature_names[:5]

  return feature_names

def get_sentiments_from_tweets(df):
  df = df.sort_values(by='id')
  df = df.drop_duplicates(['id'])

  sentiments = dict()
  for index, row in df.iterrows():
    row_lemmas = lemmatize(tokenize(row['text']))
    if row['trend'] not in sentiments:
      sentiments[row['trend']] = TweetSentiment()
      sentiments[row['trend']].trending_keyword = row['trend']

    if row_lemmas != None:
      sentiments[row['trend']].lemmas.extend(row_lemmas)

    neg = row['neg']
    pos = row['pos']

    if pos > 0.5:
      sentiments[row['trend']].num_positive_tweets = sentiments[row['trend']].num_positive_tweets + 1
    elif neg > 0.5:
      sentiments[row['trend']].num_negative_tweets = sentiments[row['trend']].num_negative_tweets + 1
    else:
      sentiments[row['trend']].num_neutral_tweets = sentiments[row['trend']].num_neutral_tweets + 1

  for trend, sentiment in sentiments.items():
    sentiment.major_topics = topics(sentiment.lemmas)

  return list(sentiments.values())
