*This is the public posting of the assignment. See Piazza for the invite link to make your submission in your own repository in the class organization.*

# Homework 9 - k-Nearest Neighbors (kNN)
**Due:** Thursday, April 23, 2020 by 11:59pm

## Assignment

Write a report that answers and explains your answers to the following questions. Support your answers by including all relevant discussion, assumptions, examples, etc. *You must describe how you answered the questions.* Your GitHub repo should include all scripts, code, output files, images needed to complete the assignment. If you use a Google Colab notebook, you must save a copy in GitHub in your HW9 repo.

In this assignment, we will be using kNN for computing nearest neighbors only, not for prediction.

**Q1.**  Using your data from HW7 (Twitter account-term matrix):

* Consider each row in the account-term matrix as a 1000 dimension vector, corresponding to a Twitter account.  

* Modify `getdistances()` to use the cosine distance metric instead of Euclidean distance (see [Euclidean vs. Cosine Distance](https://cmry.github.io/notes/euclidean-v-cosine) on why we use cosine for documents). You may want to check out [SciPy's cosine distance function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cosine.html).

* Use a modified version of `knnestimate()` from Ch 8 to compute the 5 nearest neighbors for 3 of the accounts in your list (pick any 3).  
	* Hint 1: Just return the distances, not some computed average (*there's nothing to compute the average of anyway*)
	* Hint 2: Since the account you pick will be in your training set, that account should always be reported as the top nearest neighbor with a distance of 0. When reporting the 5 nearest neighbors, omit the account that is being tested (but still report 5 other neighbors).
	
**Q2.** For each of the accounts you chose, do the 5 nearest neighbors chosen by the algorithm make sense?  What name (classification) would you give that group of accounts?

*You will not get full credit on this assignment if you just report the list of neighbors generated. You must describe the changes you made to the code, how the process works, and your assessment of how well the kNN algorithm performed.*

## Extra Credit

**Q3.** *(Extra credit, 3 points)* For each of the 3 accounts you chose in Q1, how many neighbors can you generate before the grouping tends to break down?  That is, when do accounts that are likely not very similar to the target account start to make the list?

**Q4.** *(Extra credit, 3 points)* For the 3 accounts you chose in Q1, compare the 5 nearest neigbors computed with cosine distance to those chosen using Euclidean distance.  Which distance metric seemed to do better?


## Submission

Make sure that you have committed and pushed your local repo to GitHub before the deadline.
