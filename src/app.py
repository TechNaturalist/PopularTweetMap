from flask import Flask, render_template, abort, Response
from flask.helpers import url_for

from sentiment_analysis.gather import Gather
from sentiment_analysis.sentiment_analyzer import SentimentAnalyzer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html"
    )

@app.route("/trends", methods=["GET"])
def get_trends(latitude, longitude, trend_count = 1, limit = 50):
  if latitude == None:
    abort(Response("Latitude is required, but wasn't provided."))
  if longitude == None:
    abort(Response("Longitude is required, but wasn't provided."))

  gatherer = Gather()
  sentiment_analyzer = SentimentAnalyzer()
  tweets = gatherer.newTweets(latitude, longitude, trend_count, limit)
  tweets = sentiment_analyzer.add_sentiment_scores(tweets)

  ## do some logic to get a list of TweetSentiment out of tweets
  sentiments = []
  return sentiments


if __name__ == '__main__':
    # app.run(debug = True)
    with app.test_request_context():
      print(url_for('get_trends', latitude=20.20202, longitude=15.0203))