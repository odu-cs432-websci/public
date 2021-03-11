# collect-links-cursor.py
# MCW - 2/11/2021 / mperry - 3/10/2021
import sys
import json
import tweepy

# use coronavirus as default search term unless one provided
search_term = "coronavirus"
if len(sys.argv) > 1:
     search_term = str(sys.argv[1])

# number of links to collect
MAX_COUNT = 1200
count = 0

# load Twitter API keys from a file so they're not hard-coded
with open("secrets.json", "r") as secretsFile:
    secrets = json.load(secretsFile)
# print(secrets['consumer_key'])
# print(secrets['consumer_secret'])

# setup Twitter API with OAuth2 procedure
consumer_key = secrets['consumer_key']
consumer_secret = secrets['consumer_secret']
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

try:
  for page in tweepy.Cursor(api.search, q=search_term, tweet_mode='extended', lang='en').pages():
    for tweet in page:
         for link in tweet.entities["urls"]:
             print("%s" % link['expanded_url'])
             count = count + 1
    if count > MAX_COUNT:
         break
except tweepy.TweepError as e:
  print ("Tweepy Error: %s" % str(e))
