import nltk
import pandas

nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        self._analyzer = SentimentIntensityAnalyzer()



    def add_sentiment_scores(self, dataframe):
        if(self.__check_text(dataframe)):
            added_scores = self.__add_scores(dataframe)
            return added_scores

        else:
            print("DataFrame Does not include text")
            return pandas.DataFrame()



    def __check_text(self, dataframe):
        if 'text' in dataframe.columns:
            return True
        else:
            return False


    def __add_scores(self, dataframe):
        dataframe['neg'] = dataframe['text'].apply(
            lambda x:self._analyzer.polarity_scores(x)['neg'])
        dataframe['neu'] = dataframe['text'].apply(
            lambda x:self._analyzer.polarity_scores(x)['neu'])
        dataframe['pos'] = dataframe['text'].apply(
            lambda x:self._analyzer.polarity_scores(x)['pos'])
        
        dataframe['compound'] = dataframe['text'].apply(
            lambda x:self._analyzer.polarity_scores(x)['compound'])
        return dataframe
