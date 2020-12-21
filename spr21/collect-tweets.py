# collect-tweets.py
# MCW - 12/21/2020
import sys
import tweepy
import json
from datetime import datetime

# use coronavirus as default search term unless one provided
search_term = "coronavirus"
if len(sys.argv) > 1:
     search_term = str(sys.argv[1])

# INSERT YOUR KEYS HERE
consumer_key = ""
consumer_secret = ""
key = ""
secret = ""

# OAuth1 procedure
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(key, secret)
#api = tweepy.API(auth)

# OAuth2 procedure
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

tweet_data = []

tweets = api.search(search_term, lang="en", count=20)

# See for info on tweet object
# https://www.geeksforgeeks.org/python-user-object-in-tweepy/
# https://www.geeksforgeeks.org/python-status-object-in-tweepy/

# collect dictionary of tweets
for tweet in tweets:
     tweet_dict = {}
     tweet_dict["tweet_id"] = tweet.id_str
     tweet_dict["screen_name"] = tweet.user.screen_name
     tweet_dict["time"] = tweet.created_at.strftime("%Y%m%d%H%M%S")
     if (len(tweet.entities["urls"]) > 0):
         tweet_dict["link"] = tweet.entities["urls"][0]["expanded_url"]
     tweet_dict["text"] = tweet.text
     tweet_data.append(tweet_dict)

# write out tweets in JSON format to stdout
json.dump(tweet_data, sys.stdout, indent=2)
