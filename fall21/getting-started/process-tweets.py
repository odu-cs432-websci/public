# process-tweets.py
# MCW - 7/1/2021

import sys
import json
from datetime import datetime

# read in lines of JSON from stdin
lines = sys.stdin.readlines()  # read in all the lines

# For tweet object format, see
# https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet
# and look at the file that was created by collect-tweets.py
for line in lines:
    tweet_data = json.loads(line)  # each line is JSON

    # gather some information about the tweet
    author = tweet_data['author']['username']  # author's username
    created_at = tweet_data['created_at']      # time tweet created
    retweets = tweet_data['public_metrics']['retweet_count']  # num retweets
    replies = tweet_data['public_metrics']['reply_count']  # num replies
    likes = tweet_data['public_metrics']['like_count']  # num likes
    followers = tweet_data['author']['public_metrics']['followers_count'] # author's followers
    verified = tweet_data['author']['verified']  # author verified?
    text = tweet_data['text']  # text of the tweet
    id = tweet_data['id']  # tweet id

    # collect links 
    links = []
    if 'urls' in tweet_data['entities']:
        for link in tweet_data['entities']['urls']:
            links.append(link['expanded_url'])
    
    # collect entities added by Twitter
    entities = []
    if 'context_annotations' in tweet_data:
        for context in tweet_data['context_annotations']:
            entities.append(context['domain']['name'] + ": " + context['entity']['name'])

    # print information about the tweet
    print (id + "\t" + created_at + "\t" + author + "\t" + str(followers))
    for term in entities:
        print("  " + term)
    for link in links:
        print("  " + link)
    print ()    
