*This is the public posting of the assignment. See Blackboard for the invite link to make your submission in your own repository in the class organization.*

# Homework 4 - Exploring Social Networks
**Due:** Sunday, March 14, 2021 by 11:59pm

Read through the entire assignment before starting. 

## Assignment 

Write a report that answers and explains your answers to the following questions.  *Be sure to include a description of how you answered the questions and any interesting observations you can make based on your analysis.* Your GitHub repo should include all scripts, code, output files, images needed to complete the assignment.

Report reminders:
* Reports are not just a list of questions and answers, but *must* include descriptions, screenshots, copy-paste of code output, references, as necessary.  For each question you address, you must describe how you answered the question, including describing the code you wrote to accomplish the task.  
* All graphs that you generate must be done in R or using a Python plotting library, and images must be inserted into your report.
* All reports must have a section labeled "References" for listing the outside resources you consulted.
* All reports must include your name, class (make sure to distinguish between CS 432 and CS 532), assignment number/title, and date.

### Q1. Friendship Paradox on Facebook

The [friendship paradox](http://en.wikipedia.org/wiki/Friendship_paradox) says that your friends have more friends than you do.  Determine if the friendship paradox holds for a user's Facebook account. *(This used to be more interesting when you could more easily download your friend's friends data from Facebook.  Facebook now requires each friend to approve this operation, effectively making it impossible.)* 

[HW4-friend-count.csv](HW4-friend-count.csv) contains a user's friends' names and number of friends they each have. 

Compute the mean, standard deviation, and median of the number of friends that the user's friends have.  

Create a graph of the number of friends (y-axis) and the friends (x-axis) themselves, sorted by number of friends (y-axis).  (The friends don't need to be labeled on the x-axis: just f1, f2, f3, ... fn.)  Include the user in the graph (count the number of their friends) and label as U.

### Q2. Friendship Paradox on Twitter

Determine if the friendship paradox holds for your Twitter account. Since Twitter is a directed graph, use *followers* as the value you measure (i.e., "do your followers have more followers than you?").  *Due to Twitter rate limits, this part will take some time to complete.*

Generate the same graph as in Q1, and calcuate the same mean, standard deviation, and median values.

I would recommend using [Cursor ()](https://docs.tweepy.org/en/v3.10.0/cursor_tutorial.html) from the [Tweepy API](https://docs.tweepy.org/en/v3.10.0/api.html#) for this.  You don't need the full information about the followers, just their IDs (so that you can request their followers and count them), so I recommend using `api.followers_ids` [(Tweepy documentation)](https://docs.tweepy.org/en/v3.10.0/api.html?highlight=follower_ids#API.followers_ids) instead of `api.followers`:

~~~python
tweepy.Cursor(api.followers_ids, id=id, wait_on_rate_limit=True).items(5000)
~~~

The line above includes the userid (or screen_name) as `id`, requests up to 5000 items (max in a single request), and includes the `wait_on_rate_limit=True` option, which will automatically pause your script while it waits for the rate limiting timeout.  According to [Twitter's GET followers/ids documentation](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids), the rate limit is 15 requests every 15 minutes.  For each request, you can get up to 5000 follower IDs.

To save time, you can use the 5000 follower max so that you don't have to make multiple requests for a single user's followers.  

If you have less than 50 followers on Twitter, then you can use my Twitter account ([weiglemc](https://twitter.com/weiglemc/)).

## Extra Credit

### Q3. (*1 point*) 

Repeat Q2, but change *followers* to *following*.  In other words, are the people you are following following more people than you are?

In Tweepy, this is `friends_ids` instead of `followers_ids`.  According to the [Twitter GET friends/ids documentation](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids), the rate limits are similar as for requesting follower IDs.

### Q4. (*2 points*)

*To complete this question, you must have saved the follower IDs you collected for each user in Q2, not just the counts.*

If you saved the lists of follower IDs from Q2, you should have lots of sets of user IDs (followers of the main account + followers of their followers).  Calculate how many times each user ID appears in the other follower lists.  Who are the 5 users who appear most often?  List those screen_name (not IDs) and how many times they appear. How many accounts only appear once?

### Q5. (*1 point*)

For the main user account, how many of their followers are also their friends (followees)?  That is, how many of the relationships are bi-directional?  List the screen_names (not IDs) of the bi-directional relationships.  (If there are more than 20, put the list in a separate file in your repo and provide the filename in your report.)

## Submission

Make sure that you have committed and pushed your local repo to GitHub.  Your repo should contain any code you developed to answer the questions.  Include "Ready to grade @weiglemc @brutushammerfist" in your final commit message. 

Submit the URL of your report in Blackboard:

* Click on HW4 under Assignments in Blackboard
* Under "Assignment Submission", click the "Write Submission" button.
* Copy/paste the URL of your report into the edit box
  * should be something like https<nolink>://github.com/cs432-websci-spr21/hw4-socialmedia-*username*/blob/master/HW4-report.{pdf,md}
* Make sure to "Submit" your assignment.
