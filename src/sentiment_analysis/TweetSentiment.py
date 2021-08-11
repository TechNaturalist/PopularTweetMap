class TweetSentiment:
  def __init__(self) -> None:
    self.num_positive_tweets = 0
    self.num_negative_tweets = 0
    self.num_neutral_tweets = 0
    self.trending_keyword = ''
    self.major_topics = []
    self.lemmas = []

  def get_data(self):
    return {
      'num_positive_tweets': self.num_positive_tweets,
      'num_negative_tweets': self.num_negative_tweets,
      'num_neutral_tweets': self.num_neutral_tweets,
      'trending_keyword': self.trending_keyword,
      'major_topics': self.major_topics
    }
