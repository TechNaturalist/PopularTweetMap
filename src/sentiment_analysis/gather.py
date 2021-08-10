from twarc import Twarc
from copy import copy
import pandas

class Gather():
    def __init__(self, csv_path = None):
        self._twarc = Twarc()
        self.columns = [
            'id',
            'text',
            'latitude',
            'longitude', 
            'trend']
        if csv_path != None:
            self._training_set = pandas.read_csv(
                csv_path, 
                delimiter='\t',
                index_col=False)
        else:
            self._training_set = pandas.DataFrame()



    def newTweets(self, lat, lng, trend_count = 1, limit = 50):
        woeid = self.__closest_woeid(lat,lng)
        trends = self.__trends(woeid, trend_count)
        tweets = self.__search(trends, lat, lng, limit)
        return tweets



    def training_tweets(self):
        return copy(self._training_set)


    def __closest_woeid(self,lat,lng):
        closest = self._twarc.trends_closest(lat, lng)
        woeid = closest[0]['woeid']
        return woeid



    def __trends(self, woeid, trend_count):
        trends = []
        json_trends = self._twarc.trends_place(woeid)
        for i in range(trend_count):
            trends.append(
                    json_trends[0]['trends'][i]['name'])
        return trends



    def __search(self, trends, lat, lng, limit):
        tweets = pandas.DataFrame(columns = self.columns)
        for trend in trends:
            count = 0;
            for tweet in self._twarc.search(
                    trend, 
                    geocode = self.__geocode(lat,lng)):
                if count < limit:
                    tweets = tweets.append(self.__entry(tweet, trend, lat, lng), ignore_index=True)
                else:
                    break
                count += 1
        return tweets


    def __geocode(self,lat, lng):
        return str(lat)+','+str(lng)+','+'100mi'



    def __entry(self, tweet, trend, lat, lng):
        a_series = {
            'id': str(tweet['id_str']),
            'text': str(tweet['full_text']),
            'latitude': str(lat),
            'longitude': str(lng),
            'trend': str(trend)}
        return a_series
