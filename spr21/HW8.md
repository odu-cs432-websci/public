*This is the public posting of the assignment. See Blackboard for the invite link to make your submission in your own repository in the class organization.*
# Homework 8 - Clustering
**Due:** Sunday, April 18, 2021 by 11:59pm  

## Assignment

Write a report that answers and explains your answers to the following questions. Support your answers by including all relevant discussion, assumptions, examples, etc. You must describe how you answered the questions. Your GitHub repo should include all scripts, code, output files, images needed to complete the assignment. If you use a Google Colab notebook, you must save a copy in your GitHub repo.

**Important:** Because much of the code for this assignment is provided for you, your report will carry even more weight in your final grade for this assignment.  Your report must include a high-level description of how the code works and answers to all of the sub-questions asked.

*The goal of this assignment is to cluster Twitter accounts based on the content of their last 200 (or so) tweets.*

**Tips for Completing this Assignment:**
* First, read the entire assignment before starting.
* Make sure you've watched the Module 12 lecture videos.
* Watch the HW8 intro video.
* Your first reference should be the [Module 12 lecture slides](https://docs.google.com/presentation/d/10Oo6E3U2goYCgztDf11UzGUFYxm2oksfiUv1id1sEcg/edit?usp=sharing), class Colab notebook, and *Programming Collective Intelligence* book and [Chapter 3 code](https://github.com/arthur-e/Programming-Collective-Intelligence/tree/master/chapter3).  *Don't start with a Google search.*

**Report reminders:**
* Reports are not just a list of questions and answers, but *must* include descriptions, screenshots, copy-paste of code output, references, as necessary.  For each question you address, you must describe how you answered the question, including code snippets and description of the code you wrote to accomplish the task.  
* All graphs that you generate must be done in R or using a Python plotting library, and images must be inserted into your report.
* All reports must have a section labeled "References" for listing the outside resources you consulted.
  * You may use existing code, but you **must** document and reference where you adapted the code -- give credit where credit is due! *Use without attribution is plagiarism!*
* All reports must include your name, class (make sure to distinguish between CS 432 and CS 532), assignment number/title, and date.

### Q1. - Find Popular Twitter Accounts
Generate a list of 100 popular accounts on Twitter.  The accounts must be verified, have > 10,000 followers, and have > 5000 tweets.  For example:
* https://twitter.com/weiglemc - not verified, 457 followers, 2554 tweets - *don't include*
* https://twitter.com/WNBA - verified (blue checkmark), 672,800+ followers, 77,900+ tweets - *could include*

See [GET users/lookup](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup), [Tweepy's API.lookup_users()](https://docs.tweepy.org/en/latest/api.html), and [User object](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) for details on obtaining this information for a set of accounts.  

You may also generate this information manually by visiting individual account pages. 

Because we're trying to cluster the accounts based on the text in their tweets, you should choose several sets of accounts that are similar (political, tech, sports, etc.) to see if they'll get clustered together later.

Save the list of accounts (screen_names), one per line, in a text file named `accounts.txt` and upload to your GitHub repo.

*How did you choose to collect the accounts?*

*What topics/categories do the accounts belong to?  You don't need to specify a grouping for each account, but what general topics/categories will you expect to be revealed by the clustering?*

### Q2. - Create Account-Term Matrix

Before we can run the clustering code from the PCI book, we have to build an account-term matrix (like the blog-term matrix in the Module 12 slides), where all of the tweets from a single account are considered the same as a "blog" in our examples.

The PCI book provided code for creating the blog-term matrix given a list of blog feeds.  I've provided similar code for you in this repo:
* [tweetparser.py](tweetparser.py) - This is similar to the feedparser library mentioned on pg. 31.  It contains two functions used by `generatetweetvector.py`:
    * `setup_api(filename)` - set up and return a Twitter API object, `filename` is the file containing your API keys (same format as `secrets.json`) 
    * `parse(api, screen_name, num_tweets=200)` - use Tweepy to download about 200 tweets (English language, extended mode, excluding replies and retweets) from the timeline of the `screen_name` account and return a dictionary with the following structure:   
    `{'screen_name': screen_name, 'tweets': [tweet1, tweet2, ...]}`

* [generatetweetvector.py](generatetweetvector.py) - This is similar to `generatefeedvector.py` described on pgs. 31-33.  It requires `tweetparser.py` to be located in the same folder.  It contains main code and two functions:
    * `getwordcounts(api, screen_name)` - calls `parse()` from `tweetparser.py` and returns the screen_name and a dictionary of word counts appearing in that account's tweets, almost exactly like `getwordcounts()` in our examples
    * `getwords(tweet)` - takes a tweet and returns a filtered list of words, similar to `getwords()` in our examples, but with some added filtering:
        * removes URLs
        * removes screen names (starting with @)
        * splits words by non-alphabetic characters (and thus removes any numbers and symbols)
        * removes any words < 3 characters or > 15 characters
        * lowercases all words

`generatetweetvector.py` requires that you have two additional files in the same folder:
* `secrets.json` - containing your Twitter API keys (same format as [secrets.json](https://github.com/cs432-websci-master/public/blob/main/spr21/secrets.json) that was provided before)
* `accounts.txt` - list of accounts (one per line) from Q1

The code is similar to that from pgs. 31-33 in PCI and [`generatefeedvector.py`](https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter3/generatefeedvector.py)

`generatetweetvector.py` will ***not work out-of-the-box*** -- there is some code that you'll need to add.  Instead of creating an account-term matrix for every term in the tweets, I only want the 1000 most popular terms.  ***You will need to write this code.***  To help with this, I've added a `sumcounts` variable that holds the words and frequency of those words over all accounts.  You will see a section labeled `# INSERT YOUR CODE HERE` and that's where you need to construct a list of the 1000 most frequent terms and save it in the variable `popularlist`.

Once complete, `generatetweetvector.py` will produce two files that you need to upload to your GitHub repo:
* `popularlist.txt` - the list (one per line) of the 1000 most frequent terms in the tweets
* `tweetdata.txt` - the generated account-term matrix

Once `tweetdata.txt` has been generated, you can use it in place of `blogdata.txt` in the example code to complete the remaining parts of this assignment.

*Explain the general operation of generatetweetvector.py and how the tweets are converted to the account-term matrix. Explain in detail the code that you added to filter for the 1000 most frequent terms.*

*Do the 1000 most frequent terms make sense based on the accounts that you chose?*

### Q3. - Create Dendrogram
Create an ASCII dendrogram *and* a JPEG dendrogram that uses hierarchical clustering to cluster the most similar accounts (see Module 12, slides 21, 23).  Include the JPEG in your report and upload the ASCII file to GitHub (it will be too unwieldy for inclusion in the report).

*How well did the hierarchical clustering do in grouping similar accounts together?  Were there any particularly odd groupings?*

### Q4. - Cluster using k-Means
Cluster the accounts using k-Means, using `k`=5,10,20 (see Module 12, slide 37).  For each value of `k`, create a file that lists the accounts in each cluster and upload to your GitHub repo.  

*Give a brief explanation of how the k-Means algorithm operates on this data.  What features is the algorithm considering?*

*How many iterations were required for each value of `k`?*

*Which `k` value created the most reasonable clusters?  For that grouping, characterize the accounts that were clustered into each group.*

### Q5. - Create MDS Image

Use MDS to create a JPEG of the accounts (see Module 12, slide 50).  Include the JPEG in your report. 

*How many iterations were required?*

*How well did the MDS do in grouping similar accounts together?  Were there any particularly odd groupings?*

## Extra Credit

### Q6. - Generate Nicer Dendrogram (not ASCII art)
*(Extra credit, 1 point)* 

Generate the dendrogram figure from Q3 using [scipy's dendrogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html) or [plotly's create_dendrogram](https://plotly.com/python/dendrogram/). The clustering should be the same as what you get in Q3.

### Q7. - Generate Nicer MDS Image
*(Extra credit, 2 points)* 

Generate the MDS figure from Q5 as a scatterplot using regular Python graphing libraries or Vega-Lite/D3.  Plot the labels (could be in addition to the points or in place of the points) or allow the user to mouse-over the points and display the labels (i.e., tooltips). The figure won't look exactly like Q5 since the initial placement is random, but it should be similar. 

### Q8. - Generate Account-Term Matrix with TF-IDF
*(Extra credit, 3 points)*  

Re-generate the account-term matrix but this time process the terms using proper TF-IDF calculations instead of the hack discussed on slide 12 (p. 32).  Use the same 1000 terms, but this time replace their frequency count with TF-IDF scores (similar to as computed in HW3). Document the code, techniques, methods, etc. used to generate these TF-IDF values.  Upload the new account-term matrix file to GitHub.
*  For this IDF computation, you can use the tweets you gathered in Q1 as your corpus (instead of searching Google for each term).  Treat the set of tweets from each account as a single document.

Then re-do Q3 with the new matrix.  Compare and contrast the resulting dendrogram with the dendrogram from Q3.

Note: Ideally you would not reuse the same 1000 terms and instead would come up with TF-IDF scores for all the terms and then choose the top 1000 from that list, but I'm trying to limit the amount of work necessary.

## Submission

Make sure that you have committed and pushed your local repo to GitHub.  Your repo should contain any code you developed to answer the questions.  Include "Ready to grade @weiglemc @brutushammerfist" in your final commit message. 

Submit the URL of your *report* in Blackboard:
* Click on HW8 under Assignments in Blackboard  
* Under "Assignment Submission", click the "Write Submission" button.
* Copy/paste the URL of your report into the edit box
  * should be something like https<nolink>://github.com/cs432-websci-spr21/hw8-cluster-*username*/blob/master/HW8-report.{pdf,md}
* Make sure to "Submit" your assignment.

After grades have been submitted, you can view feedback in your GitHub repo ([slides with screenshots of this from a different class](https://docs.google.com/presentation/d/1F0H9pMHKbD-VdeWSQip6QciUdocnnRPMdXhoInCge-E/edit?usp=sharing)):
* Click on "Pull requests"
* Click "1 Closed"
* Click "Feedback"
* Scroll through Conversation tab to see comments from both me and GTA Matthew. The final comments and your grade are at the end.
