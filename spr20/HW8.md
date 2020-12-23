*This is the public posting of the assignment. See Piazza for the invite link to make your submission in your own repository in the class organization.*

# Homework 8 - Spam Classification
**Due:** Thursday, April 16, 2020 by 11:59pm

## Assignment

Write a report that answers and explains your answers to the following questions. Support your answers by including all relevant discussion, assumptions, examples, etc. *You must describe how you answered the questions.* Your GitHub repo should include all scripts, code, output files, images needed to complete the assignment. If you use a Google Colab notebook, you must save a copy in GitHub in your HW8 repo.

**Q1.** Create two datasets, Testing and Training.
	
The **Training** dataset should consist of
* 10 text documents for email messages you consider spam (from your spam folder)
* 10 text documents for email messages you consider not spam (from your inbox)

The **Testing** dataset should consist of:
* 10 text documents for email messages you consider spam (from your spam folder)
* 10 text documents for email messages you consider not spam (from your inbox)

Make sure that these are plain-text documents and that they do not include HTML tags.  The documents in the Testing set should be different than the documents in the Training set.

Upload your datasets to your GitHub repo. *Please do not include emails that contain sensitive information.*

**Q2.** Use the provided example code (see https://github.com/cs432-websci-spr20/assignments/blob/master/Week_11_Ch06_PCI.ipynb) to train and test the Naive Bayes classifier.  Use your Training dataset to train the Naive Bayes classifier.  Use your Testing dataset to test the Naive Bayes classifier and report the classification results for each email message in the Testing dataset.

**Q3.** Draw a confusion matrix for your classification results (see https://en.wikipedia.org/wiki/Confusion_matrix and Week-05 Searching slides for false positive/false negative examples).  

## Extra Credit

**Q4.** *(Extra credit, 3 points)* Report the precision and accuracy scores of your classification results
(see https://en.wikipedia.org/wiki/Precision_and_recall and Week-05 Searching slides).

**Q5.** *(Extra credit, 3 points)* Tune your classifier by updating weights to obtain better classification results. You may want to change the default weights (`weight`, `ap`) given to `weightedprob()` or the threshold used for the Bayesian classifier or change how the words are extracted from the document (for this you will need to re-train the model).  Report the changes you made, re-run your Testing dataset, and show that the performance improved (either by using the confusion matrix or by computing precision and accuracy).

**Q6.** *(Extra credit, 5 points)* Implement the classifier with the Multinomial model instead of the multiple Bernoulli model and re-run Q2 and Q3.  Did the classification improve?  *Make sure to remove the unique word filter from the extractor.*

## Submission

Make sure that you have committed and pushed your local repo to GitHub before the deadline.
