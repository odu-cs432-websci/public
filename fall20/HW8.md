*This is the public posting of the assignment. See Blackboard for the invite link to make your submission in your own repository in the class organization.*

# Homework 8 - Clustering
**Due:** Sunday, December 6, 2020 by 11:59pm

## Reports
* CS 432 students *may* complete this report in Markdown. Or, you may choose to use LaTeX instead. 
* CS 532 students *must* complete this report using LaTeX generated to a PDF file (GitHub repo must contain both the LaTeX source and PDF).
* Any graphs required for your reports must be done in R or using a Python plotting library (see ["The 7 most popular ways to plot data in Python"](https://opensource.com/article/20/4/plot-data-python)) -- Excel graphs are unacceptable!
* When you include an image in your report, *do not change the [aspect ratio](https://en.wikipedia.org/wiki/Aspect_ratio_(image)) of the image*. If you have trouble with this, ask for help in our Piazza group.

Reports are not just a list of questions and answers, but should include descriptions, screenshots, copy-paste of code output, references, as necessary.  For each question you address, you must describe how you answered the question.  

You may use existing code, but you **must** document and reference where you adapted the code -- give credit where credit is due! *Use without attribution is plagiarism!*

All reports must include your name, class (make sure to distinguish between CS 432 and CS 532), assignment number/title, and date.  You do not need a title page.  

## Assignment

Write a report that answers and explains your answers to the following questions. Support your answers by including all relevant discussion, assumptions, examples, etc. You must describe how you answered the questions. Your GitHub repo should include all scripts, code, output files, images needed to complete the assignment. If you use a Google Colab notebook, you must save a copy in GitHub in your HW8 repo.

We will be clustering Twitter accounts based on the content of their last 200 (or so) tweets.

### Q1. - collect data
Generate a list of 100 popular accounts on Twitter.  The accounts must be verified, have > 10,000 followers, and have > 5000 tweets.  See [GET users/lookup](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) and [User object](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) for details on obtaining this information for a set of accounts.  You may also generate this information manually by visiting individual account pages. For example:
* https://twitter.com/weiglemc - not verified, 435 followers, 2450 tweets - *don't include*
* https://twitter.com/WNBA - verified (blue checkmark), 659,000+ followers, 76,000+ tweets - *could include*

Save the list of accounts (screen_names) in a text file (one per line) and upload to your GitHub repo.

Download 200 English-language tweets from the 100 accounts. See [GET statuses/user_timeline](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline) for details. Note that you may receive fewer than 200 tweets in a single API call due to deleted or protected tweets. It's OK as long as you get somewhere close to 200 tweets for each account. (I don't want to you have to make more than one API call per account.)

Save the tweets from the 100 accounts to your GitHub repo.  It can all be in a single file or a separate file for each account. Since this is an intermediate file, the format is up to you. 

### Q2. - create account-term matrix
Generate an account-term matrix from the accounts' tweets.  

First, you'll need to process the tweets to extract the terms:
* Remove any terms that have non-ASCII characters (ex: you\u2019ll)
   * Hint: `any(ord(char) >= 128 for char in word)`
* Remove URIs
* Remove account names (ex: @weiglemc)
* Remove punctuation
* Remove any terms that are < 3 characters or > 15 characters long
* Convert all terms to lowercase

Hint: Take advantage of regular expressions to detect URIs, account names (always start with '@'), and punctuation.

All of the tweets from a single account should be considered the same as a "blog" in our examples.

Then use the criteria on p. 32 of the PCI book (Ch 3 and on slide 12 in [Week-12 Clustering](https://docs.google.com/presentation/d/1Sz5tSqXBjMCLOIq7oIEq53BXDfLvNWwjIZFug3Z_aVE/edit)) to fake removing stopwords and computing TF-IDF.  This keeps only terms that appear in more than 10% and fewer than 50% of the accounts.  Note that this requires you to first build a dictionary that counts the number of accounts each term appears in (*not the number of times each term appears, but the number of accounts*).

From this filtered list of terms, create a final list of the most "popular" (i.e., frequent) 1000 terms over all accounts.  This time, you're counting how many times the term appeared over all accounts.

Save the popular terms used in each account's tweets in a file and upload to your GitHub repo.  It can all be in a single file or a separate file for each account. Since this is an intermediate file, the format is up to you. 

In the account-term matrix, the account screen_name is the account identifier and should be start each row of the matrix.  Use the (max 1000) terms for the columns of the matrix.  The values are the frequency of occurrence in each account's tweets.  Essentially you are replicating the format of the "blogdata.txt" file included with the PCI book code. 

Save the matrix in a text file (either tab-separated like blogdata.txt or comma-separated) and upload to your GitHub repo.

### Q3. - dendrograms
Create an ASCII dendrogram and a JPEG dendrogram that uses hierarchical clustering to cluster the most similar accounts (see slides 21, 23 - Week 12).  Include the JPEG in your report and upload the ASCII file to GitHub (it will be too unwieldy for inclusion in the report).

### Q4. - k-means
Cluster the accounts using k-Means, using *k*=5,10,20 (see slide 37 - Week 12).  In separate files, list the accounts in each cluster, for each value of *k*.  How many iterations were required for each value of *k*?

Can you characterize the accounts that were clustered into each group?  Which *k* value created the most reasonable clusters?

### Q5. - MDS
Use MDS to create a JPEG of the accounts (see slide 50 - Week 12).  Include the JPEG in your report. How many iterations were required?

## Extra Credit

### Q6.
*(Extra credit, 3 points)*  

Re-generate the account-term matrix but this time process the terms using proper TF-IDF calculations instead of the hack discussed on slide 12 (p. 32).  Use the same 1000 terms, but this time replace their frequency count with TF-IDF scores (similar to as computed in HW3). Document the code, techniques, methods, etc. used to generate these TF-IDF values.  Upload the new account-term matrix file to GitHub.

Then re-do Q3 with the new matrix.  Compare and contrast the resulting dendrogram with the dendrogram from Q3.

Note: Ideally you would not reuse the same 1000 terms and instead would come up with TF-IDF scores for all the terms and then choose the top 1000 from that list, but I'm trying to limit the amount of work necessary.

### Q7. 
*(Extra credit, 1 point)* 

Generate the dendrogram figure from Q3 using [scipy's dendrogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html) or [plotly's create_dendrogram](https://plotly.com/python/dendrogram/). The clustering should be the same as what you get in Q3.

### Q8. 
*(Extra credit, 2 points)* 

Generate the MDS figure from Q5 using regular Python graphing libraries or Vega-Lite/D3 (i.e., don't generate a JPG file, but produce a scatterplot). Plot the labels (could be in addition to the points or in place of the points) or allow the user to mouse-over the points and display the labels. The figure won't look exactly like Q5 since the initial placement is random, but it should be similar. 

## Submission

Make sure that you have committed and pushed your local repo to GitHub.  Your repo should contain any code you developed to answer the questions.  Include "Ready to grade @weiglemc" in your final commit message. 

Submit the URL of your *report* in Blackboard:

* Click on HW8 under Assignments in Blackboard
* Under "Assignment Submission", click the "Write Submission" button.
* Copy/paste the URL of your report into the edit box
  * should be something like https<nolink>://github.com/cs432-websci-fall20/hw8-cluster-*username*/blob/master/HW8-report.{pdf,md}
* Make sure to "Submit" your assignment.
