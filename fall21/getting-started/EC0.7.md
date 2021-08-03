# Extra Credit (EC) 0.7 - Twitter, twarc

Once you have performed the steps described in [Twitter Setup](twitter-setup.md), including receiving approval for Twitter Developer Access and installing `twarc2`, you can work on the steps below.

You can use `twarc2` as a command-line application (and you might want to do this for testing), but for your homework assignments, you will be using twarc [programmatically as a Python library](https://twarc-project.readthedocs.io/en/latest/#use-as-a-library).

## General Notes

For assignments that require you to obtain data from the web and process it, you are encouraged to separate those two tasks.  Create one script that collects the data and another script that processes the data.  That way, if there's an error in your processing script, you don't have to collect the data again.

You are encouraged to look at the code in the provided scripts to see how the collection and processing was done, but for now the main point is to make sure that you can access tweets programmatically.

## Collecting Tweets

Download [collect-tweets.py](collect-tweets.py) and edit the code to point to the file where twarc has stored your Twitter API keys.  

Use `collect-tweets.py` to collect 25 recent English-language tweets related to 'covid' that contain links:

`% python3 collect-tweets.py covid`

The output will be saved in `tweets.jsonl`.

## Processing Tweets

Download [process-tweets.py](process-tweets.py) and use it to save information about each of the collected tweets to a file:

`% python3 process-tweets.py < tweets.jsonl > tweets-info.txt`

For each tweet in the file, this script will print the tweet ID, creation time, author, Twitter-assigned entities, and links included in the tweet.
