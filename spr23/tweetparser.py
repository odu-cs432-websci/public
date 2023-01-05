# tweetparser.py
# MCW - 11/16/2021
from twarc import Twarc2, expansions
from configparser import ConfigParser

def setup_api(filename):
    '''
    filename: file where Twitter API keys are stored
    returns Twitter API object to pass into parse()
    '''

    # read Twitter API keys from twarc config file, setup twarc2 object
    config = ConfigParser(interpolation=None)
    with open(filename) as twarc_config:
        config.read_string("[TWARC]\n" + twarc_config.read())
    bearer_token = config['TWARC']['bearer_token'].strip('\'')
    t = Twarc2(bearer_token=bearer_token)
    return t

def parse(api, screen_name, num_tweets=100):
    '''
    api: Twitter API object, use setup_api() to create
    screen_name: Twitter screen_name
    num_tweets: Number of tweets to request (default: 100)
    returns dict with {'screen_name': screen_name, 'tweets': [tweet1, tweet2, ...]}
    '''

    tweet_data = []
    try:
        timeline = api.timeline(screen_name, max_results=num_tweets, exclude_replies=True, exclude_retweets=True)
        for page in timeline:
            result = expansions.flatten(page)
            for tweet in result:
               tweet_data.append(tweet["text"])
               if len(tweet_data) == num_tweets:
                    # must include this to stop after a certain # of tweets
                    timeline.close()
    except Exception as e:
        print ("Twarc Error: %s" % str(e))
  
    account_data = {'screen_name': screen_name, 'tweets': tweet_data}
    return account_data
