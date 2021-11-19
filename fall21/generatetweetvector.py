# generatetweetvector.py
# Based on generatefeedvector.py from 
# https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter3/generatefeedvector.py

from tweetparser import setup_api, parse
import re

def getwordcounts(api, screen_name):
    '''
    api: Twitter API object
    screen_name: Twitter screen_name
    returns screen_name and dictionary of word counts for a Twitter account
    '''
    
    # Parse the Twitter feed
    d = parse(api, screen_name)
    wc = {}

    # Loop over all the entries
    for tweet in d['tweets']:
        # Extract a list of words
        words = getwords(tweet)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1

    return (d['screen_name'], wc)

def getwords(tweet):
    '''
    returns lowercase list of words after filtering
    '''

    # Remove URLs
    text = re.compile(r'(http://|https://|www\.)([^ \'\"]*)').sub('', tweet)

    # Remove other screen names (start with @)
    text = re.compile(r'(@\w+)').sub('', text)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(text)

    # Filter for words between 3-15 characters, convert to lowercase, and return as a list
    return [word.lower() for word in words if (len(word) >= 3 and len(word) <= 15)]

#####
# MAIN CODE STARTS HERE
#####

# set up Twitter API object
api = setup_api("/Users/mweigle/Library/Application Support/twarc/config")

apcount = {}      # number of accounts each word appears in
wordcounts = {}   # words and frequency in each account
sumcounts = {}    # words and frequency over all accounts (to determine most popular)

# list of screen names should be in 'accounts.txt', one per line
accountlist = [line.strip() for line in open('accounts.txt')]

for screen_name in accountlist:
    try:
        # get tweets, filter and count words
        (user, wc) = getwordcounts(api, screen_name)
        wordcounts[user] = wc
        
        # count number of accounts each term appears in
        for (word, count) in wc.items():
            apcount.setdefault(word, 0)
            sumcounts.setdefault(word, 0)
            if count > 1:
                apcount[word] += 1        # counting accounts with the word
                sumcounts[word] += count  # summing total counts for the word
    except:
        print ('Failed to parse account %s' % screen_name)

# remove stopwords ("fake" way)
wordlist = []
for (w, ac) in apcount.items():
    # w is the word, ac is the account count (was bc 'blog count' in textbook)
    frac = float(ac) / len(accountlist)
    if frac > 0.1 and frac < 0.5:
        wordlist.append(w)

# popularlist will hold the 500 most frequent terms over all accounts
popularlist = []

#### 
# BEGIN YOUR CODE BLOCK
####

# Write code that stores the 500 most frequent non-stopword terms over all accounts in the list popularlist

# Hints:
# * sumcounts is a dict with the number of times that each word has appeared over all accounts
#        ex: sumcounts["the"] = 30
# * wordlist is a list of the non-stopwords

####
# END YOUR CODE BLOCK
####

# write out popular word list
with open('popularlist.txt', 'w') as outf:
    for word in popularlist:
        outf.write(word + '\n')

# write out account-term matrix
with open('tweetdata.txt', 'w') as outf:
    # write header row ("Account", list of words)
    outf.write('Account')
    for word in popularlist:
        outf.write('\t%s' % word)
    outf.write('\n')

    # write each row (screen_name, count for each word)
    for (screen_name, wc) in wordcounts.items():
        outf.write(screen_name)
        for word in popularlist:
            if word in wc:
                outf.write('\t%d' % wc[word])
            else:
                outf.write('\t0')
        outf.write('\n')
