from flask import Flask, render_template, abort, Response
from flask.helpers import url_for
from flask import request
from flask import jsonify

from sentiment_analysis.gather import Gather
from sentiment_analysis.sentiment_analyzer import SentimentAnalyzer
from sentiment_analysis.TweetSentiment import TweetSentiment
from topic_model import process_topics

app = Flask(__name__)

@app.route("/")
def home():
  return render_template(
    "index.html"
  )

@app.route("/trends", methods=["GET"])
def get_trends(trend_count = 1, limit = 50):
  latitude = request.args.get('latitude')
  longitude = request.args.get('longitude')
  if latitude == None:
    abort(Response("Latitude is required, but wasn't provided."))
  if longitude == None:
    abort(Response("Longitude is required, but wasn't provided."))

  #gatherer = Gather()
  #sentiment_analyzer = SentimentAnalyzer()

  #tweets = gatherer.newTweets(latitude, longitude, trend_count, limit)
  #tweets = sentiment_analyzer.add_sentiment_scores(tweets)
  #topics = process_topics(tweets)

  ## do some logic to get a list of TweetSentiment out of tweets
  test_sentiment = TweetSentiment()
  test_sentiment.trending_keyword = 'olympics'
  test_sentiment.major_topics = [ 'gold', 'silver', 'bronze' ]
  test_sentiment.num_positive_tweets = 100
  test_sentiment.num_negative_tweets = 10
  sentiment = test_sentiment.get_data()
  return jsonify(sentiment)


if __name__ == '__main__':
    # app.run(debug = True)
    with app.test_request_context():
      print(url_for('get_trends', latitude=20.20202, longitude=15.0203))