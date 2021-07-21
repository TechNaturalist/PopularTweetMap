from twarc import Twarc
from copy import copy
import pandas

class gather():
    def __init__(self, csv_path = None):
        self._twarc = twarc.Twarc()
        self.columns = [
            'id',
            'text',
            'latitude',
            'longitue', 
            'trend']
        if csv_path != None:
            self._training_set = pandas.read_csv(
                csv_path, 
                delimiter=',')
        else:
            self._training_set = pandas.DataFame()



    def newTweets(self, lat, lng, trend_count = 1, limit = 50):
        woeid = self._twarc.trends_closest(lat,lng)
        trends = self.__trends(woeid, trend_count)
        tweets = self.__search(trends, lat, lng, limit)
        return tweets



    def training_tweets(self):
        return self._training_set



    def __trends(woeid, trend_count):
        trends = []
        json_trends = self.twarc_place(woeid)
        for i in range(trend_count):
            trends.append(
                    json_trends[0]['trends'][i]['name'])
        return trends



    def __search(self, trends, lat, lng, limit):
        tweets = pandas.DataFrame(
            columns = self.columns)
        for trend in trends:
            count = 0;
            for tweet in self._twarc.search(trend):
                if count < limit:
                    tweets.append(self.__entry(tweet, trend, lat, lng))
                else
                    break
        return tweets



    def __entry(self, tweet, trend, lat, lng):
        a_series = [
            tweet['id_str'],
            tweet['full_text']
            str(lat),
            str(lng),
            trend]
        return pandas.Series(a_series, index=self.columns)
