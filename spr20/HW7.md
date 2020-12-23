*This is the public posting of the assignment. See Piazza for the invite link to make your submission in your own repository in the class organization.*

# Homework 7 - Clustering
**Due:** Thursday, April 9, 2020 by 11:59pm

## Assignment

Write a report that answers and explains your answers to the following questions. Support your answers by including all relevant discussion, assumptions, examples, etc. You must describe how you answered the questions. Your GitHub repo should include all scripts, code, output files, images needed to complete the assignment. If you use a Google Colab notebook, you must save a copy in GitHub in your HW7 repo.

We will be clustering Twitter accounts based on the content of their last 200 (or so) tweets.

**Q1.** Generate a list of 100 popular accounts on Twitter.  The accounts must be verified, have > 10,000 followers, and have > 5000 tweets.  See [GET users/lookup](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) and [User object](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) for details on obtaining this information for a set of accounts.  You may also generate this information manually by visiting individual account pages. For example:
* https://twitter.com/weiglemc - not verified, 414 followers, 2189 tweets - *don't include*
* https://twitter.com/WNBA - verified (blue checkmark), 615,000+ followers, 69,000+ tweets - *could include*

Save the list of accounts (screen_names) in a text file (one per line) and upload to your GitHub repo.

Download 200 tweets from the 100 accounts. See [GET statuses/user_timeline](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline) for details. Note that you may receive fewer than 200 tweets in a single API call due to deleted or protected tweets. It's OK as long as you get somewhere close to 200 tweets for each account. (I don't want to you have to make more than one API call per account.)

Save the responses received from the 100 accounts to your GitHub repo.  It can all be in a single file or a separate file for each account. Since this is an intermediate file, the format is up to you. 

**Q2.** Generate an account-term matrix from the accounts' tweets.

Using the responses from Q1, extract the text from each tweet to generate terms. Remove any URIs in the tweets, but keep regular text and hashtags as terms.  Limit the number of terms to the most "popular" (i.e., frequent) 1000 terms, this is *after* the criteria on p. 32 (chapter 3 PCI book) (slide 11 - Week 10) has been satisfied. 

Save the terms for each account in a file and upload to your GitHub repo.  It can all be in a single file or a separate file for each account. Since this is an intermediate file, the format is up to you. 

In the account-term matrix, the account screen_name is the account identifier and should be start each row of the matrix.  Use the (max 1000) terms for the columns of the matrix.  The values are the frequency of occurrence.  Essentially you are replicating the format of the "blogdata.txt" file included with the PCI book code. 

Save the matrix in a text file (either tab-separated like blogdata.txt or comma-separated) and upload to your GitHub repo.

**Q3.**  Create an ASCII dendrogram and a JPEG dendrogram that uses hierarchical clustering to cluster the most similar accounts (see slides 21 & 23 - Week 10).  Include the JPEG in your report and upload the ASCII file to GitHub (it will be too unwieldy for inclusion in the report).

**Q4.**  Cluster the accounts using k-Means, using *k*=5,10,20 (see slide 37 - Week 10).  Print the accounts in each cluster, for each value of *k*.  How many iterations were required for each value of *k*?

**Q5.**  Use MDS to create a JPEG of the accounts (see slide 50 - Week 10).  Include the JPEG in your report. How many iterations were required?

## Extra Credit

**Q6.** *(Extra credit, 3 points)*  Re-run Q3, but this time with proper TF-IDF calculations instead of the hack discussed on slide 11 (p. 32).  Use the same 1000 terms, but this time replace their frequency count with TF-IDF scores (similar to as computed in HW3).  Document the code, techniques, methods, etc. used to generate these TF-IDF values.  Upload the new data file to GitHub.

Compare and contrast the resulting dendrogram with the dendrogram from Q3.

Note: Ideally you would not reuse the same 1000 terms and instead come up with TF-IDF scores for all the terms and then choose the top
1000 from that list, but I'm trying to limit the amount of work necessary.

**Q7.** *(Extra credit, 2 points)* Generate the dendrogram figure from Q3 using [scipy's dendrogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html) or [plotly's create_dendrogram](https://plotly.com/python/dendrogram/). The clustering should be the same as what you get in Q3.

**Q8.** *(Extra credit, 2 points)* Generate the MDS figure from Q4 using regular Python graphing libraries or Vega-Lite/D3 (i.e., don't generate a JPG file, but produce a scatterplot). Plot the labels (could be in addition to the points or in place of the points) or allow the user to mouse-over the points and display the labels. The figure won't look exactly like Q4 since the initial placement is random, but it should be similar. 

## Submission

Make sure that you have committed and pushed your local repo to GitHub before the deadline.  
