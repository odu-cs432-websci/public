*This is the public posting of the assignment. See Blackboard for the invite link to make your submission in your own repository in the class organization.*

# Homework 6 - Analyzing Disinformation Domains
**Due:** Sunday, April 4, 2021 by 11:59pm 

## Assignment

Write a report that answers the questions asked below. Support your answers by including all relevant discussion, assumptions, examples, etc. You must describe how you answered the questions and any interesting insights from your work. Your GitHub repo should include all scripts, code, output files, images needed to complete the assignment. If you use a Google Colab notebook, you must save a copy in GitHub in your HW6 repo.

Report reminders:
* Reports are not just a list of questions and answers, but *must* include descriptions, screenshots, copy-paste of code output, references, as necessary.  For each question you address, you must describe how you answered the question, including describing the code you wrote to accomplish the task.  
* All graphs that you generate must be done in R or using a Python plotting library, and images must be inserted into your report.
* All reports must have a section labeled "References" for listing the outside resources you consulted.
  * You may use existing code, but you **must** document and reference where you adapted the code -- give credit where credit is due! *Use without attribution is plagiarism!*
* All reports must include your name, class (make sure to distinguish between CS 432 and CS 532), assignment number/title, and date.

### Data Sources:

Note: *These datasets are only available via the GitHub Classroom invite*

* D1 - 117 domains shared in tweets in Dr. Starbird's ICWSM 2017 paper, related to mass shootings
   * not all links are to disinformation sites, includes some mainstream news sources
   * fields: domain, media type, primary orientation, how cited, # citations in tweets
* D2 - 628 domains that were shared in tweets in Dr. Starbird's ICWSM 2018 paper, related to work of White Helmets in Syria
  * not all links are to disinformation sites
  * fields: domain, URL count, Tweet count
* D3 - 347 domains publishing false Coronavirus information, gathered by [NewsGuardTech's Coronavirus Misinformation Tracking Center](https://www.newsguardtech.com/coronavirus-misinformation-tracking-center/) as of October 28, 2020
   * fields: domain, country, notes

### Q1 - Dataset Analysis

Datasets D1 and D2 include the number of tweets that each domain was shared in (found in the last column/field of the dataset).

For each of D1 and D2, what were the top 10 domains in terms of tweets?  Which ones are no longer live?  Load the main webpage in your web browser.  How would you classify the domain? Show this information in a table like the one below, sorted by number of tweets.  You should have 2 tables, one for D1 and one for D2.

| domain | tweets | website type | status | 
|---- | ---- | ---- | ---- |
|rt.com | 1598 | foreign government media | live |
|cnn.com | 756 | mainstream media | live |
|1clickdaily.com | 14 | alternative media | not live | 

Notes:
* You may want to refer to the "media type" field in the D1 dataset to help with the classification.  
* If the domain is not live and does not have a classification in D1, do a Google search to see if you can find out more information about the domain.  If that doesn't reveal anything, then just put 'unknown' in the "website type" column.

*What can you say about the domains that have been frequently shared on Twitter?*

### Q2 - Dataset Overlap

Compare the amount of overlap between the three datasets.  

Generate the following datasets:
* a. domains that are present in both D1 and D2
* b. domains that are present in both D2 and D3
* c. domains that are present in both D1 and D3
* d. domains that are present in all three datasets

Create a table showing the number of domains in each of the datasets above.  List out the domains in each of the datasets in your report.  Upload each of the datasets to your GitHub repo.

Hints:
* Make sure that your domains are all lowercase before processing.
* [Python sets](https://realpython.com/python-sets/) have intersection operators.

*Is there anything interesting about the domains that are present in multiple datasets?*

### Q3 - Collect Tweets

Collect at least 200 tweets that contain links from domains that appear in both D3 and one of the other datasets (so, dataset b or dataset c from Q2).
* Hint: If you're using tweepy, you can use `api.search("url:" + domain, lang="en", count=200)` to search for English language tweets that contain links with the given domain (see [Search Methods](http://docs.tweepy.org/en/latest/api.html#search-methods)).

For each tweet, save the following information:
* tweet id (`id_str`)
* account that shared the link (`user.screen_name`)
* tweet time (`created_at.strftime("%Y%m%d%H%M%S")` - *prints date in YYYYMMDDHHMMSS format*)
* domain (*the domain you searched for*)
* link (`entities["urls"][0]["expanded_url"]`)
* tweet text (`text`) - *if you plan to do extra credit Q7*

I would recommend writing a separate script to collect tweets and write out the information to a JSON file (see `json.dump()`) and then read in the file later for processing.
* if you store your tweet data as an array of Python dictionaries (one dictionary for each tweet), then you can write out the data in formatted JSON to stdout with `json.dump(tweet_data, sys.stdout, indent=2)`
  * example of running a program and writing the data to a file via stdout: `python3 gather-tweets.py > tweets.json`
* to load the data from stdin, you can use `tweet_data = json.load(sys.stdin)`
  * example of running a program and reading in a file via stdin: `python3 process-tweets.py < tweets.json`

*If you cannot gather the tweets, you can request a JSON file from us, but it costs 1.5 points.*

Questions to answer:
* How many tweets did you gather?  
* What was the time range of the tweets you gathered?
* How many different accounts posted those tweets?
* For those domains that had at least one tweet, how many tweets did you discover for each domain? 
  * To answer this question, create a bar chart showing the number of tweets for each domain.

### Q4 - Further Tweet Analysis

**This is required for CS 532 students, but counts as extra credit for CS 432 students**

Compare the number of tweets per domain from Q3 with the information in D1 and D2.  What were the top 10 shared domains from Q3?  How does this compare with the top 10 shared domains in D1 and D2 (from Q1)?  

For those domains that had at least one tweet, how many accounts were posting links for each domain?  
  * To answer this question, create a bar chart showing the number of accounts for each domain.

## Extra Credit

### Q5 - Disinformation Games
*(1 point)*

There have been several online games created to educate people about disinformation and how it spreads on social media.  Play one of the games at either https://www.getbadnews.com or https://goviralgame.com.  Write a paragraph about your experience and some lessons you learned by playing the game. Take some screenshots as you play to include in your report.

### Q6 - Network Graph
*(2 points)*

Use your data from Q3 to create a network graph, similar to Dr. Starbird's, where a domain shared in a tweet is a node and a link exists between two nodes if a single account shared a link from both domains.  For example, if user weiglemc shared a tweet with a link to www.odu.edu and another tweet with a link to www.lsu.edu, then there should be a link between node odu.edu and node lsu.edu.

For an *additional point of extra credit*, have the size of the node be based on the number of tweets the domain was shared in.

### Q7 - Tweet Text Analysis
*(2 points)*

Investigate the text of the tweets you collected in Q3 and report on any interesting findings.  Here are some example questions you could look at:
* What were the most common terms?
* How many tweets contained the most common terms?
* How many tweets were retweets (text starting with "RT")?
* How many times was a single tweet repeated?

What insights did you gain?  What could be some avenues for further investigation?

*A thoughtful examination of the data is required to receive the full 2 points.*

### Q8 - Archived Domains
*(3 points)*

For each domain in D1, D2, and D3, check the archival status of the domain's main webpage using MemGator. If a domain appears in multiple datasets, only check the status once.

You don't need to figure out the actual main webpage URI, just putting the domain in the request should work, for example  
`% curl http://memgator.cs.odu.edu/timemap/link/theregister.co.uk/`

Save the TimeMap for each domain in your GitHub repo.

Save a data file that contains each domain name, the dataset(s) it appears in (D1/D2/D3), datetime of its first memento, datetime of its last memento, and its total number of mementos. 

Note that some of the main webpages for the domains in D3 should have at least 1 memento because the Internet Archive has created an Archive-It collection of these (see https://archive-it.org/collections/13559). Though, this was created in March 2020 and the list is continually being updated by NewsGuardTech.

Create the following charts based on the collected data:
* Scatterplot of domain vs. datetime of the first memento and last memento (x-axis), sorted by the datetime of the first memento.  Color dots based on the dataset (or datasets) it comes from. This should look similar to this [chart of URIs vs. memento datetimes](https://3.bp.blogspot.com/-8vNC-7UraiQ/U43lwAC0pSI/AAAAAAAAAE4/1IyHbXH9CKQ/s1600/mementosScatterDmoz.png), but with only the first and last dot on each row plotted (since you're only plotting the datetimes of the first and last mementos).
* A single chart with multiple eCDFs ([Week-03 InfoVis](https://docs.google.com/presentation/d/1qBZreni_aXcBbj4K5xAPvt2IPP7nVfv_DCtslINcehc/edit?usp=sharing), slide 24) showing the number of mementos per domain for all the datasets. Each dataset should have its own eCDF curve. The x-axis should be number of mementos for a domain.
    * There's a section on creating eCDFs in our Week-03 Google Colab notebooks: [Python notebook](https://github.com/cs432-websci-fall20/assignments/blob/master/432_Week_03_InfoVis_Python.ipynb), [R notebook](https://github.com/cs432-websci-fall20/assignments/blob/master/432_Week_03_InfoVis_R.ipynb)

## Submission

Make sure that you have committed and pushed your local repo to GitHub. Your repo should contain any code you developed to answer the questions. Include "Ready to grade @weiglemc @brutushammerfist" in your final commit message.

Submit the URL of your report in Blackboard:
* Click on HW6 under Assignments in Blackboard
* Under "Assignment Submission", click the "Write Submission" button.
* Copy/paste the URL of your report into the edit box
  * should be something like https<nolink>://github.com/cs432-websci-spr21/hw6-disinfo-*username*/blob/master/HW6-report.{pdf,md}
* Make sure to "Submit" your assignment.
