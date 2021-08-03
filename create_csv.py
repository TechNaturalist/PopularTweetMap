from gather import Gather
from datetime import date
from sentiment_analyzer import SentimentAnalyzer

TRENDCOUNT = 5
LIMIT = 100
LAT = 41
LONG = -111

def main():
    
    g = Gather()
    s = SentimentAnalyzer()

    print("getting tweets")
    df = g.newTweets(LAT,LONG, TRENDCOUNT, LIMIT )
    print("adding sentiment scores")
    df = s.add_sentiment_scores(df)


    

    name = date.today().strftime("%y_%m_%d") + '.csv'
    df.to_csv(
        name,
        sep='\t')

if __name__ == "__main__":
    main()
