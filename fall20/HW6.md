*This is the public posting of the assignment. See Blackboard for the invite link to make your submission in your own repository in the class organization.*

# Homework 6 - Analyzing Disinformation Domains
**Due:** Sunday, November 15, 2020 by 11:59pm 

## Reports
* CS 432 students *may* complete this report in Markdown. Or, you may choose to use LaTeX instead. 
* CS 532 students *must* complete this report using LaTeX generated to a PDF file (GitHub repo must contain both the LaTeX source and PDF).
* Any graphs required for your reports must be done in R or using a Python plotting library (see ["The 7 most popular ways to plot data in Python"](https://opensource.com/article/20/4/plot-data-python)) -- Excel graphs are unacceptable!
* When you include an image in your report, *do not change the [aspect ratio](https://en.wikipedia.org/wiki/Aspect_ratio_(image)) of the image*. If you have trouble with this, ask for help in our Piazza group.

Reports are not just a list of questions and answers, but should include descriptions, screenshots, copy-paste of code output, references, as necessary.  For each question you address, you must describe how you answered the question.  

You may use existing code, but you **must** document and reference where you adapted the code -- give credit where credit is due! *Use without attribution is plagiarism!*

All reports must include your name, class (make sure to distinguish between CS 432 and CS 532), assignment number/title, and date.  You do not need a title page.  

## Data Sources:
* [D1](https://docs.google.com/spreadsheets/d/1lk3pFSc5wo3OfJc8ekONqO3MJCCigqe8SBSYwLYlHLo/) - 117 domains shared in tweets in the ICWSM 2017 paper, related to mass shootings
   * not all links are to disinformation sites, includes some mainstream news sources
* D2 - 1679 URIs shared in tweets in the ICWSM 2018 paper, related to work of White Helmets in Syria
  * *this dataset is only available via the GitHub Classroom invite*
  * not all links are to disinformation sites
* [D3](https://docs.google.com/spreadsheets/d/1bjuMnAnDsiVWrIuGIIpsXKBqkYNrOehmx0_ZWGVI6d0/) - 347 domains publishing false Coronavirus information, gathered by [NewsGuardTech's Coronavirus Misinformation Tracking Center](https://www.newsguardtech.com/coronavirus-misinformation-tracking-center/) as of October 28, 2020

*Google spreadsheets can be downloaded as CSV or TSV files using the File...Download... menu option* 

## Assignment 

Write a report that answers the following questions. Support your answers by including all relevant discussion, assumptions, examples, etc. You must describe how you answered the questions and any interesting insights from your work. Your GitHub repo should include all scripts, code, output files, images needed to complete the assignment. If you use a Google Colab notebook, you must save a copy in GitHub in your HW6 repo.

### Q1
*(2 points)* 

The D2 dataset (1679 URIs) contains some shortened URIs and proxies. Process each URI and follow redirects until it resolves as a 200 or there is a 40x HTTP status. 

Save a data file that contains the original URI, tweet frequency (from the original data file), final URI (many of these will be the same as the original URI), and current HTTP status.

Questions to answer:
* How many URIs redirected to a different URI?
* How many of the final URIs reported a 200 OK?
* How many of the final URIs reported a 404 Not Found (or some other non-200 status)?

For each of the final URIs, extract the domain from the URI. Examples:
* Given the URI `https://en.wikipedia.org/wiki/Domain_name`, the domain is `wikipedia.org`.
* Given the URI `https://www.theregister.co.uk/2020/04/16/cloudflare_cobol/`, the domain is `theregister.co.uk`.

Save a data file that contains each unique domain, the number of times that domain appeared in the dataset, and the total number of tweets the domain appeared in. 

Questions to answer:
* How many unique domains are there?
* What were the top 5 domains that appeared in the most tweets?

### Q2
*(2 points)* 

Compare the amount of overlap between the three datasets (use your D2 processed domains dataset from Q1).  Create a table showing the amount of overlap among the datasets.  

Generate the following datasets:
* a. domains that are present in both D1 and D2
* b. domains that are present in both D2 and D3
* c. domains that are present in both D1 and D3
* d. domains that are present in all three datasets

Is there anything interesting about the domains that are present in multiple datasets?

### Q3
*(4 points)*

Collect at least 200 tweets that contain links from domains that appear in both D3 and one of the other datasets (so, dataset b or dataset c from Q2).
* Hint: If you're using tweepy, you can use `api.search("url:" + domain, lang="en", count=200)` to search for English language tweets that contain links with the given domain (see [Search Methods](http://docs.tweepy.org/en/latest/api.html#search-methods)).

For each tweet, save the following information:
* tweet id (`id_str`)
* account that shared the link (`user.screen_name`)
* tweet time (`created_at.strftime("%Y%m%d%H%M%S")` - *prints date in YYYYMMDDHHMMSS format*)
* domain (*the domain you searched for*)
* link (`entities["urls"][0]["expanded_url"]`)
* tweet text (`text`) - *if you plan to do extra credit Q6*

I would recommend writing a separate script to collect tweets and write out the information to a JSON file (see `json.dump()`) and then read in the file later for processing.
* if you store your tweet data as an array of Python dictionaries (one dictionary for each tweet), then you can write out the data in formatted JSON to stdout with `json.dump(tweet_data, sys.stdout, indent=2)`
  * example of running a program and writing the data to a file via stdout: `python3 gather_tweets.py > tweets.json`
* to load the data from stdin, you can use `tweet_data = json.load(sys.stdin)`
  * example of running a program and reading in a file via stdin: `python3 process_tweets.py < tweets.json`

*If you cannot gather the tweets, you can request a JSON file from us, but it costs 1.5 points.*

Questions to answer:
* How many tweets did you gather?  
* What was the time range of the tweets you gathered?
* How many different accounts posted those tweets?
* How many tweets did you discover for each domain? 
  * To answer this question, create a bar chart showing the number of tweets for each domain.
* How many accounts were posting links for each domain?  
  * To answer this question, create a bar chart showing the number of accounts for each domain.

### Q4
*(2 points)*

Compare the number of tweets per domain (from Q3) with the original D1 data and your domain dataset from Q1 (for the D2 dataset).  

Questions to answer:
* What are the top 5 shared domains in each set?  How do these compare?  
* The datasets will have different numbers because of different number of tweets captured, but how do the distributions compare?  
  * eCDFs ([Week-03 InfoVis](https://docs.google.com/presentation/d/1qBZreni_aXcBbj4K5xAPvt2IPP7nVfv_DCtslINcehc/edit?usp=sharing), slide 24) might be helpful in comparing the distributions.  There's a section on creating eCDFs in our Week-03 Google Colab notebooks: [Python notebook](https://github.com/cs432-websci-fall20/assignments/blob/master/432_Week_03_InfoVis_Python.ipynb), [R notebook](https://github.com/cs432-websci-fall20/assignments/blob/master/432_Week_03_InfoVis_R.ipynb)

## Extra Credit

### Q5 
*(2 points)*

Create a network graph, similar to Dr. Starbird's, where a domain shared in a tweet is a node and a link exists between two nodes if a single account shared a link from both domains.  The size of the node should be based on the number of tweets the domain was shared in.

For example, if user weiglemc shared a tweet with a link to www.odu.edu and another tweet with a link to www.lsu.edu, then there should be a link between node odu.edu and node lsu.edu.

### Q6
*(2 points)*

Investigate the text of the tweets you collected in Q3 and report on any interesting findings.  Here are some example questions you could look at:
* What were the most common terms?
* How many tweets contained the most common terms?
* How many tweets were retweets (text starting with "RT")?
* How many times was a single tweet repeated?

What insights did you gain?  What could be some avenues for further investigation?

*A thoughtful examination of the data is required to receive the full 2 points.*

### Q7 
*(3 points)*

For each domain in D1, D2 (using results from Q2), and D3, check the archival status of the domain's main webpage using MemGator. If a domain appears in multiple datasets, only check the status once.

You don't need to figure out the actual main webpage URI, just putting the domain in the request should work, for example
`% curl http://memgator.cs.odu.edu/timemap/link/theregister.co.uk/`

Save the TimeMap for each domain in your GitHub repo.

Save a data file that contains each domain name, the dataset(s) it appears in (D1/D2/D3), datetime of its first memento, datetime of its last memento, and its total number of mementos. 

Note that some of the main webpages for the domains in D3 should have at least 1 memento because the Internet Archive has created an Archive-It collection of these (see https://archive-it.org/collections/13559). Though, this was created in March 2020 and the list is continually being updated by NewsGuardTech.

Create the following charts based on the collected data:
* Scatterplot of domain vs. datetime of the first memento and last memento (x-axis), sorted by the datetime of the first memento.  Color dots based on the dataset (or datasets) it comes from. This should look similar to this [chart of URIs vs. memento datetimes](https://3.bp.blogspot.com/-8vNC-7UraiQ/U43lwAC0pSI/AAAAAAAAAE4/1IyHbXH9CKQ/s1600/mementosScatterDmoz.png), but with only the first and last dot on each row plotted (since you're only plotting the datetimes of the first and last mementos).
* eCDF of the number of mementos per domain for all the datasets. The x-axis should be number of mementos for a domain.

## Submission

Make sure that you have committed and pushed your local repo to GitHub. Your repo should contain any code you developed to answer the questions. Include "Ready to grade @weiglemc @brutushammerfist" in your final commit message.

Submit the URL of your report in Blackboard:
* Click on HW6 under Assignments in Blackboard
* Under "Assignment Submission", click the "Write Submission" button.
* Copy/paste the URL of your report into the edit box
  * should be something like https<nolink>://github.com/cs432-websci-fall20/hw6-disinfo-*username*/blob/master/HW6-report.{pdf,md}
* Make sure to "Submit" your assignment.
