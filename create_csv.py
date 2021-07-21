from gather import Gather
from datetime import date

TRENDCOUNT = 5
LIMIT = 20
LAT = 41
LONG = -111

def main():
    
    g = Gather()
    df = g.newTweets(LAT,LONG, TRENDCOUNT, LIMIT )

    name = date.today().strftime("%y_%m_%d") + '.csv'

    df.to_csv(
        name,
        sep='\t')

if __name__ == "__main__":
    main()
