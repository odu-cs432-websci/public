
*This is the public posting of the assignment. See Piazza or Blackboard for the invite link to make your submission in your own repository in the class organization.*


# Homework 2 - Web Archiving
**Due:** Tuesday, February 18, 2020 *before class* 

***Important: Q1 requires obtaining a Twitter Developer Account.  This may take a day or two, so figure out what needs to be done today!***

## Assignment

Write a report that answers the following questions.  Your GitHub repo should include all scripts, code, output files, images needed to complete the assignment.

**Q1.**  Write a Python program that extracts 1000 unique (collect more e.g., 1300 just in case) links from Twitter. Omit links from the Twitter domain (twitter.com).

You might want to take a look at:
* [Tweepy: a Python Library for the Twitter API](https://medium.com/@jasonrigden/tweept-a-python-library-for-the-twitter-api-9d0537dcebd4), [Tweepy documentation](http://docs.tweepy.org/en/latest/getting_started.html#introduction)
* [How to collect tweets from the Twitter Streaming API using Python](https://www.storybench.org/how-to-collect-tweets-from-the-twitter-streaming-api-using-python/)
* [Stream tweets with Tweepy in Python](https://medium.com/@adam.oudad/stream-tweets-with-tweepy-in-python-99e85b6df468)
* [Tutorial: Gathering text data w/ Python & Twitter Streaming API](https://medium.com/swlh/tutorial-gathering-text-data-w-python-twitter-streaming-api-e1007a3b70ef)

There are many other similar resources available on the web.  

Note that you need to verify that the final target URI (i.e., the one that responds with a 200) is unique.  You could have many
different shortened URIs (e.g., t.co, bit.ly, goo.gl, etc.) for the same URI-R.  For example:

```
$ curl -IL --silent https://t.co/DpO767Md1v | egrep -i "(HTTP/1.1|HTTP/2|^location:)"
HTTP/2 301
location: https://goo.gl/40yQo2
HTTP/2 302
location: https://soundcloud.com/roanoketimes/ep-95-talking-hokies-recruiting-one-week-before-signing-day
HTTP/1.1 200 OK
```

You might want to use the streaming or search feature to find URIs. *If you find something you consider to be inappropriate for any reason, just discard it and get some more links.*  We just want 1000 links that were shared via Twitter.

Hold on to this collection and upload it to your repo in GitHub -- we'll use it later throughout the semester.


**Q2.**  Download the [TimeMaps](http://www.mementoweb.org/guide/quick-intro/) for each of the target URIs from Q1 using the ODU Memento Aggregator.

For example:

URI-R = http://www.cs.odu.edu/

URI-T = http://memgator.cs.odu.edu/timemap/link/http://www.cs.odu.edu/

or

URI-T = http://memgator.cs.odu.edu/timemap/json/http://www.cs.odu.edu/

(depending on which format you'd prefer to parse)

Create a [histogram](https://en.wikipedia.org/wiki/Histogram) of URIs vs. number of mementos (as computed from the TimeMaps).  For example, 100 URIs with 0 mementos, 300 URIs with 1 memento, 400 URIs with 2 mementos, etc.  The x-axis will have the number of mementos, and the y-axis will have the frequency of occurence.  

You may want to refer to [Histograms and frequency polygons with ggplot2 and tidyverse](https://ggplot2.tidyverse.org/reference/geom_histogram.html).


**Q3.**  Estimate the age of each of the 1000 URIs from Q1 using the [Carbon Date](http://ws-dl.blogspot.com/2017/09/2017-09-19-carbon-dating-web-version-40.html) tool.  

Example: `http://carbondate.cs.odu.edu/cd/http://www.cs.odu.edu/`

*But the service will inevitably crash when everyone tries to use it at the last minute.*  So instead, use [Docker](https://www.docker.com/) and [install CarbonDate locally](https://github.com/oduwsdl/CarbonDate). 

Not all URIs will have mementos, and not all URIs will have an estimated creation date.  Show how many fall into either categories.
For example,

* total URIs:         1000
* no mementos:        137  
* no date estimate:   212

For URIs that have > 0 mementos and an estimated creation date, create a graph with age (in days) on the x-axis and number of
mementos on the y-axis.

    
## Submission

Make sure that you have committed and pushed your local repo to GitHub.  

Submit the URL of your report in Blackboard:

* Click on HW2 under Homeworks
* Under "Assignment Submission", click the "Write Submission" button.
* Copy/paste the URL of your report into the edit box
  * should be something like https<nolink>://github.com/cs432-websci-spr20/hw2-archiving-*username*/blob/master/report.{pdf,md}
* Make sure to "Submit" your assignment.
