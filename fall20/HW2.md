*This is the public posting of the assignment. See Blackboard for the invite link to make your submission in your own repository in the class organization.*

# Homework 2 - Web Archiving
**Due:** Sunday, October 11, 2020 by 11:59pm  

***Important: Q1 requires obtaining a Twitter Developer Account.  This may take a day or two, so figure out what needs to be done today!***

This assignment is going to take time. Read through the entire assignment before starting.  *Do not wait until the last minute to start working on it!* 

## Note about Programming Tasks

For several of the programming tasks this semester, you will be asked to write code to operate on 100s or 1000s of data elements.  If you have not done this type of development before, I *strongly encourage* you to start small and work your way up.  Especially when you are using new tools or APIs, start on a small test dataset to make sure you understand how to use the tool and that your processing scripts are working before ramping up to the full set. *This will save you an enormous amount of time.*

## Assignment

Write a report that answers the following questions.  Make sure to include a description of how you addressed the questions and any interesting findings that you discover from your analysis.  

Your GitHub repo should include all scripts, code, output files, images needed to complete the assignment.

### Q1

Write a Python program that extracts 1000 unique (collect more e.g., 1300 just in case) links from tweets in Twitter. 

You might want to take a look at:
* [Tweepy: a Python Library for the Twitter API](https://medium.com/@jasonrigden/tweept-a-python-library-for-the-twitter-api-9d0537dcebd4)
    * [Tweepy documentation](http://docs.tweepy.org/en/latest/getting_started.html#introduction)
    * [Stream tweets with Tweepy in Python](https://medium.com/@adam.oudad/stream-tweets-with-tweepy-in-python-99e85b6df468)
    * [How to collect tweets from the Twitter Streaming API using Python](https://www.storybench.org/how-to-collect-tweets-from-the-twitter-streaming-api-using-python/)
    * [Tutorial: Gathering text data w/ Python & Twitter Streaming API](https://medium.com/swlh/tutorial-gathering-text-data-w-python-twitter-streaming-api-e1007a3b70ef)
* [TwitterSearch](https://github.com/ckoepp/TwitterSearch) - alternate (and potentially simpler) library to Tweepy
    * [TwitterSearch documentation](https://twittersearch.readthedocs.io/en/latest/index.html)

There are many other similar resources available on the web.  

Your final list of 1000 URIs should have the following properties:
* no shortened URIs -- resolve all URIs to their final target URI (i.e., the one that responds with a 200)
* no links from the Twitter domain (twitter.com)
* be unique (i.e., no repeated URIs)

In particular, you need to verify that the final URIs are unique.  You could have many different shortened URIs (e.g., t.co, bit.ly, goo.gl, etc.) for the same URI-R.  For example:

```
$ curl -IL --silent https://t.co/DpO767Md1v | egrep -i "(HTTP/1.1|HTTP/2|^location:)"
HTTP/2 301
location: https://goo.gl/40yQo2
HTTP/2 302
location: https://soundcloud.com/roanoketimes/ep-95-talking-hokies-recruiting-one-week-before-signing-day
HTTP/1.1 200 OK
```

You might want to use the streaming or search feature to find URIs. *If you find something you consider to be inappropriate for any reason, just discard it and get some more links.*  We just want 1000 links that were shared via Twitter.

Hold on to this collection and upload it to your repo in GitHub -- we'll use it later in another assignment.

*How many links did you have to collect to get 1000 unique URIs?  How many of the URIs initially resolved in a 300-level status (redirection)?  How many of the URIs were intially shortened?*

### Q2

Download the [TimeMaps](http://www.mementoweb.org/guide/quick-intro/) for each of the target URIs from Q1 using the ODU Memento Aggregator, [MemGator](https://github.com/oduwsdl/MemGator).

For example, if URI-R = http://www.cs.odu.edu/ then  
URI-T = http://memgator.cs.odu.edu/timemap/link/http://www.cs.odu.edu/  
or  
URI-T = http://memgator.cs.odu.edu/timemap/json/http://www.cs.odu.edu/  
(depending on which format you'd prefer to parse)

Save the TimeMaps, as you'll need them for Q3.

*You may use memgator.cs.odu.edu for limited testing, but do not request all of your 1000 TimeMaps from memgator.cs.odu.edu*.  

There are two options for running MemGator locally:
* Install a stand-alone version of MemGator on your own machine, see https://github.com/oduwsdl/MemGator/releases/tag/1.0-rc7
* Install [Docker Desktop](https://www.docker.com/products/docker-desktop) and run MemGator as a Docker Container, see notes at https://github.com/oduwsdl/MemGator/blob/master/README.md

Create a histogram of URIs vs. number of mementos (as computed from the TimeMaps).  The x-axis will have bins representing the number of mementos, and the y-axis will have the frequency of occurence.  For example, you may have 100 URIs with 0 mementos, 300 URIs with 1 memento, 400 URIs with 2 mementos, etc.  (Recall our discussion of histograms and the impact of bin size on slide 22 of Week-03 InfoVis and in the examples in the Google Colab notebooks for R and Python.)

*How well archived are the URIs in your collection?*

### Q3

For each of the 1000 URI-Rs, use the saved TimeMap from Q2 to determine the datetime of the earliest memento. Since not all URIs will have mementos, show how many fall into either category.

For example,  
* total URIs:         1000
* no mementos:        137  

For URIs that have > 0 mementos, create a graph with the age (days between collection date and earliest memento datetime) on the x-axis and number of mementos on the y-axis.  For this graph, the item is the URI-R and the attributes are the estimated age of the URI-R and the number of mementos for that URI-R.

*What can you say about the relationship between the age of a URI-R and the number of its mementos?*

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

Make sure that you have committed and pushed your local repo to GitHub.  Your repo should contain any code you developed to answer the questions. Include "Ready to grade @weiglemc" in your final commit message.

Submit the URL of your report in Blackboard:

* Click on HW2 under Assignments in Blackboard
* Under "Assignment Submission", click the "Write Submission" button.
* Copy/paste the URL of your report into the edit box
  * should be something like https<nolink>://github.com/cs432-websci-fall20/hw2-archiving-*username*/blob/master/report.{pdf,md}
* Make sure to "Submit" your assignment.
