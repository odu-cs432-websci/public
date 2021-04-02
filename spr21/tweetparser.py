# tweetparser.py
# MCW - 4/1/2021
import json
import tweepy

def setup_api(filename):
    '''
    filename: file where Twitter API keys are stored
    returns Twitter API object to pass into parse()
    '''

    # load Twitter API keys from a file so they're not hard-coded
    with open(filename, "r") as secretsFile:
        secrets = json.load(secretsFile)

    # set up Twitter API with OAuth2 procedure
    consumer_key = secrets['consumer_key']
    consumer_secret = secrets['consumer_secret']
    try:
        auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
        api = tweepy.API(auth)
        return api
    except tweepy.TweepError as e:
        print ("Tweepy Error: %s" % str(e))

def parse(api, screen_name, num_tweets=200):
    '''
    api: Twitter API object, use setup_api() to create
    screen_name: Twitter screen_name
    num_tweets: Number of tweets to request (default: 200)
    returns dict with {'screen_name': screen_name, 'tweets': [tweet1, tweet2, ...]}
    '''

    tweet_data = []
    try:
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=screen_name, count=num_tweets, lang='en', 
                                tweet_mode='extended', exclude_replies=True, include_rts=False).items():
            tweet_data.append(tweet.full_text)
    except tweepy.TweepError as e:
        print ("Tweepy Error: %s" % str(e))
  
    account_data = {'screen_name': screen_name, 'tweets': tweet_data}
    return account_data
