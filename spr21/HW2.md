*This is the public posting of the assignment. See Blackboard for the invite link to make your submission in your own repository in the class organization.*

# Homework 2 - Web Archiving
**Due:** Sunday, February 28, 2021 by 11:59pm  

***Important: Q1 requires obtaining a Twitter Developer Account.  This may take a day or two, so figure out what needs to be done today!***

This assignment is going to take time. Read through the entire assignment before starting.  *Do not wait until the last minute to start working on it!* 

## Note about Programming Tasks

For several of the programming tasks this semester, you will be asked to write code to operate on 100s or 1000s of data elements.  If you have not done this type of development before, I *strongly encourage* you to start small and work your way up.  Especially when you are using new tools or APIs, start on a small test dataset to make sure you understand how to use the tool and that your processing scripts are working before ramping up to the full set. *This will save you an enormous amount of time.*

## Assignment

Write a report that answers the following questions.  Make sure to include a description of how you addressed the questions and any interesting findings that you discover from your analysis.  

Your GitHub repo should include all scripts, code, output files, images needed to complete the assignment.

### Q1

Collect 1000 unique links from tweets in Twitter. 

There are several steps involved in this:
* Obtain a Twitter Developer Account, create a standalone app in the [Developer Portal](https://developer.twitter.com/en/portal), and generate consumer keys (API key and secret) and authentication tokens (access token and secret) -- *you should have done this in HW0*
  * [thread in Piazza related to this](https://piazza.com/class/khuxxbpeiesu2?cid=113)
* Write a Python program that collects links shared in tweets. 
  * exclude links from the Twitter domain (twitter.com)
* Resolve all URIs to their final target URI (i.e., the one that responds with a 200) -- some may be shortened links (dlvr.it, bit.ly, etc.)
* Verify that the final URIs are unique.  
  * if after this step, you don't have 1000 unique URIs, go back and gather more until you are able to get to 1000 unique URIs
* Save this collection of links and upload it to your repo in GitHub -- we'll use it again in HW3

**Collecting Links in Tweets**

There are several Twitter API wrappers available:
* [Tweepy](https://www.tweepy.org) - used in the example [collect-tweets.py](https://github.com/cs432-websci-master/public/blob/main/spr21/collect-tweets.py) that was provided in HW0
  * [Tweepy documentation](http://docs.tweepy.org/en/latest/getting_started.html#introduction)
  * [Cursor Tutorial](https://docs.tweepy.org/en/v3.10.0/cursor_tutorial.html)
  * [Search Methods](https://docs.tweepy.org/en/v3.10.0/api.html#search-methods)
  * [Python – Status object in Tweepy](https://www.geeksforgeeks.org/python-status-object-in-tweepy/)
  * [Tweet Object](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet) - Twitter API data structure returned 
* [TwitterSearch](https://twittersearch.readthedocs.io)
  * [tweet structure](https://twittersearch.readthedocs.io/en/latest/advanced_usage_ts.html#returned-tweets) - TwitterSearch data structure returned

There are many other similar resources available on the web.  

Note that you'll likely need to collect more than 1000 links initially to get 1000 unique links.

There are rate limits associated with different types of API calls to Twitter.  The search API has a larger limit than the streaming API, so I suggest using that.  Choose a few keywords and use the search API to collect links for each of those keywords.  Use keywords that you might actually search for (ex: coronavirus, election, vaccine) rather than "stopwords" (ex: test, the, tweet).

I've provided starter code, [collect-links-cursor.py](collect-links-cursor.py) for collecting links from Twitter using the Tweepy library. 
* accepts a command-line parameter with the search term and uses "coronavirus" if no term is provided
* uses Cursor() and the search API to search for English language tweets containing the given search term
* attempts to collect 1200 links
  * if you get fewer than 1200 links and see `Tweepy Error: Twitter error response: status code = 429` at the end of your file, you've hit the rate limit, so wait 15 minutes and try again
  * you may want to reduce the number of links that are collected and use multiple search terms so that you can space out the requests
* prints the URIs to stdout
* does not exclude links containing `twitter.com` -- you should add code to do this
* you will need to supply your Twitter API consumer_key and consumer_secret

`% python3 collect-links-cursor.py archive > links.txt`

This will run the program with the search term "archive" and write the output to the file `links.txt`.

*If you find a link you consider to be inappropriate for any reason, just discard it and get some more links.*  

**Resolve URIs to Final Target URI**

Many of the links that you collect will be shortened links (dlvr.it, bit.ly, buff.ly, etc.).  We want the final URI that resolves to an HTTP 200 (not a redirection).  For example:

```
$ curl -IL --silent https://t.co/DpO767Md1v | egrep -i "(HTTP/1.1|HTTP/2|^location:)"
HTTP/2 301
location: https://goo.gl/40yQo2
HTTP/2 302
location: https://soundcloud.com/roanoketimes/ep-95-talking-hokies-recruiting-one-week-before-signing-day
HTTP/1.1 200 OK
```

We want https<nolink>://soundcloud.com/roanoketimes/ep-95-talking-hokies-recruiting-one-week-before-signing-day, not https<nolink>://t.co/DpO767Md1v or https<nolink>://goo.gl/40yQo2

You can either write a Unix shell script that uses `curl` to do this, or write a Python program using the [requests library](https://requests.readthedocs.io/en/master/).

**Save Only Unique URIs**

You can write Python code for this part, but I'd strongly recommend using the Unix tools `sort` and `uniq`.  [Back to Basics: Sort and Uniq](https://www.linuxjournal.com/content/back-basics-sort-and-uniq) is a nice introduction to this.

### Q2

Download the [TimeMaps](http://www.mementoweb.org/guide/quick-intro/) for each of the unique URIs from Q1 using the ODU Memento Aggregator, [MemGator](https://github.com/oduwsdl/MemGator).  (Save the TimeMaps and upload them to your GitHub repo -- you'll also use these for Q3.)

*You may use https://memgator.cs.odu.edu for limited testing, but do not request all of your 1000 TimeMaps from memgator.cs.odu.edu*.  

There are two options for running MemGator locally:
* Install a stand-alone version of MemGator on your own machine, see https://github.com/oduwsdl/MemGator/releases
  * This was described in [HW0](https://github.com/cs432-websci-master/public/blob/main/spr21/HW0.md#memgator)
* Install [Docker Desktop](https://www.docker.com/products/docker-desktop) and run MemGator as a Docker Container, see notes at https://github.com/oduwsdl/MemGator/blob/master/README.md

**Important:** Downloading TimeMaps requires contacting several different web archives for each URI-R.  *This process will take time.*
Look at MemGator options and figure out how to process the output before running the entire process.  You might want to get JSON output, or you might want to limit to the top *k* archives (especially if there's one that's currently taking a long time to return).

Once you have downloaded and saved all of the TimeMaps, you will use them to analyze how well the URIs you collected are archived.

Create a table showing how many URI-Rs have certain number of mementos.  For example

|Mementos | URI-Rs |
|---------|--------|
|   0     |  750   |
|   1     |  150   |
|   2     |   50   |
|   5     |   47   |
|  57     |    3   |

If you are using LaTeX, you should create a [LaTeX table](https://www.overleaf.com/learn/latex/tables) -- don't submit a spreadsheet or image of a table created in something else.  If you are using Markdown, view the source of this file for an example of how to generate a table.

*What URI-Rs had the most mementos?  Did that surprise you?*

### Q3

For each of the URI-Rs from Q2 that had > 0 mementos, use the saved TimeMap to determine the datetime of the earliest memento. 

Create a scatterplot with the age of each URI-R (days between collection date and earliest memento datetime) on the x-axis and number of mementos for that URI-R on the y-axis.  For this graph, the item is the URI-R and the attributes are the estimated age of the URI-R and the number of mementos for that URI-R.

*What can you say about the relationship between the age of a URI-R and the number of its mementos?*

*What URI-R had the oldest memento?  How many URI-Rs had an age of < 1 week, meaning that their first memento was captured the same week you collected the data?*

## Extra Credit 

### Q4 (2 points)

Create an account at [Conifer](https://conifer.rhizome.org) and create a collection.  Archive at least 10 webpages related to a common topic that you find interesting. Make the collection public and include the link to your collection in your report.

*Why did you choose this particular topic?  Did you have any issues in archiving the webpages?  Do the archived webpages look like the original webpages?*

After creating your collection at Conifer, download the collection as a WARC file (see [Exporting or Downloading Content](https://guide.conifer.rhizome.org/docs/manage-sessions/exporting-warc/)).

Then load this WARC file into [ReplayWeb.page](https://replayweb.page), a tool from the Webrecorder Project (folks who developed Conifer).  From https://webrecorder.net/tools:

<blockquote>ReplayWeb.page provides a web archive replay system as a single web site (which also works offline), allowing users to view web archives from anywhere, including local computer or even Google Drive. See the <a href="https://replayweb.page/docs">User guide</a> for more info.</blockquote>

Once the WARC file has loaded, click on the "Pages" tab.  Take a screenshot that includes the list of pages and the browser address bar (showing `replayweb.page/?source=file%3A%2F%2F`..., which indicates that the WARC file is being loaded from your local computer).

Then click on the "URLs" tab and choose "All URLs" from the dropdown menu.  How many URLs were archived in the WARC file?  How does this compare to the number of Pages?

Create a bar chart showing the number of URLs in the WARC file for each of the file types in the dropdown menu.

*Which file type had the most URLs?  Were you surprised by this?*

## Submission

Make sure that you have committed and pushed your local repo to GitHub.  Your repo should contain any code you developed to answer the questions. Include "Ready to grade @weiglemc @brutushammerfist" in your final commit message.

Submit the URL of your report in Blackboard:

* Click on HW2 under Assignments in Blackboard
* Under "Assignment Submission", click the "Write Submission" button.
* Copy/paste the URL of your report into the edit box
  * should be something like https<nolink>://github.com/cs432-websci-spr21/hw2-archiving-*username*/blob/master/report.{pdf,md}
* Make sure to "Submit" your assignment.
