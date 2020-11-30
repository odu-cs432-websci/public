*This is the public posting of the assignment. See Blackboard for the invite link to make your submission in your own repository in the class organization.*

# Homework 3 - Ranking Webpages
**Due:** Sunday, October 18, 2020 by 11:59pm

## Assignment

This assignment will have you investigate different ways to rank webpages based on a query.  

Write a report that addresses the following questions.  Your GitHub repo should include all scripts, code, output files, images (including .tex file if submitting PDF) needed to complete the assignment.

### Q1. Data Collection

*For the following tasks, consider which items could be scripted, either with a shell script or with Python.  You may even want to create separate scripts for different tasks.  It's up to you to determine the best way to collect the data.*

Download the content of the 1000 URIs from HW2.  `curl`, `wget`, or `lynx` are all good candidate programs to use.  We want just the raw HTML, not the images, stylesheets, etc.

Examples from the command line:

`% curl http://www.cnn.com/ > www.cnn.com`

`% wget -O www.cnn.com http://www.cnn.com/`

`% lynx -source http://www.cnn.com/ > www.cnn.com`

<nolink>`www.cnn.com` is just an example output file name, keep in mind that the shell will not like some of the characters that can occur
in URIs (e.g., "?", "&").  You might want to hash the URIs to associate them with their respective filename, like:

```
% echo -n "http://www.cs.odu.edu/show_features.shtml?72" | md5 
41d5f125d13b4bb554e6e31b6b591eeb
```

(`md5` might be `md5sum` on some machines; note the `-n` in echo -- this removes the trailing newline.)

Now use a tool to remove (most) of the HTML markup for all 1000 HTML documents. `python-boilerpipe` will do a fair job, see 
http://ws-dl.blogspot.com/2017/03/2017-03-20-survey-of-5-boilerplate.html:

```{python}
from boilerpipe.extract import Extractor
extractor = Extractor(extractor='ArticleExtractor', html=html)
extractor.getText()
```

Keep both files for each URI (i.e., raw HTML and processed). Upload both sets of files to your GitHub repo.

### Q2. Rank with TF-IDF

Choose a query term (e.g., "coronavirus") that is not a stop word (e.g, "the"), not super-general (e.g., "web"), and not HTML markup (e.g., "http") that is found in at least 10 of your documents. (Hint: you can use `grep -c` on the processed files to identify a good query.)  If the term is present in more than 10 documents, choose any 10 English-language documents from different domains from the result set.  (If you do not end up with a list of 10 URIs, you've done something wrong.)

As per the example in the Week 6 slides, compute TF-IDF values for the query term in each of the 10 documents and create a table with the
TF, IDF, and TF-IDF values, as well as the corresponding URIs.  Rank the URIs in decreasing order by TF-IDF values.  For
example:

Table 1. 10 Hits for the term "shadow", ranked by TF-IDF.

|TF-IDF	|TF	|IDF	|URI
|------:|--:|---:|---
|0.150	|0.014	|10.680	|http://foo.com/
|0.044	|0.008	|10.680	|http://bar.com/

You can use Google or Bing for the DF estimation.  If you use Google, use 55 B as the total size of the corpus, and if you use Bing, use 10 B as the total size of the corpus (based on data from https://www.worldwidewebsize.com).

To count the number of words in the processed document (i.e., the denominator for TF), you can use `wc`:

```
% wc -w www.cnn.com.processed
    2370 www.cnn.com.processed
```

It won't be completely accurate, but it will be probably be consistently inaccurate across all files.  You can use more 
accurate methods if you'd like, just explain how you did it.  

Don't forget the log base 2 for IDF, and mind your [significant digits](https://en.wikipedia.org/wiki/Significant_figures#Rounding_and_decimal_places)!

### Q3. Rank with PageRank

Now rank the same 10 URIs from Q2, but this time by their PageRank.  Use any of the free PR estimaters on the web,
such as:
* http://www.prchecker.info/check_page_rank.php
* http://www.checkpagerank.net/
* https://dnschecker.org/pagerank.php
* https://smallseotools.com/google-pagerank-checker/

If you use these tools, you'll have to do so by hand (they have anti-bot captchas), but there are only 10 to do.  Normalize the
values they give you to be from 0 to 1.0.  Use the same tool on all 10 (again, consistency is more important than accuracy).  Also
note that these tools typically report on the domain rather than the page, so it's not entirely accurate.  

Create a table similar to Table 1:

Table 2.  10 hits for the term "shadow", ranked by PageRank.

|PageRank	|URI
|-----:|---
|0.9|		http://bar.com/[
|0.5	|	http://foo.com/

Briefly compare and contrast the rankings produced in Q2 and Q3.

## Extra Credit

### Q4. *(2 points)*
Re-do Q2 using your Twitter collection as the corpus instead of all of the Web. You should have 1000 total documents collected from Twitter, and you can use `grep` to discover how many of those documents contain your query term.  Compare this ranking to those obtained in Q2 and discuss.

### Q5. *(3 points)* 
Compute the Kendall Tau_b score for two of your lists (use "b" because there will likely be tie values in the rankings). You may choose any two from the Q2, Q3, and Q4 (if attempted) rankings.  Report both the Tau value and the "p" value.

See: 
* http://stackoverflow.com/questions/2557863/measures-of-association-in-r-kendalls-tau-b-and-tau-c
* http://en.wikipedia.org/wiki/Kendall_tau_rank_correlation_coefficient#Tau-b
* http://en.wikipedia.org/wiki/Correlation_and_dependence

### Q6. *(3 points)*  
Build a simple (i.e., no positional information) inverted file (in ASCII) for all the words from your 1000 URIs.  Upload the entire file your GitHub repo and discuss an interesting portion of the file in your report.

## Submission

Make sure that you have committed and pushed your local repo to GitHub.  Your GitHub repo should include all scripts, code, output files, images (including .tex file if submitting PDF) needed to complete the assignment. Include "Ready to grade @weiglemc @brutushammerfist" in your final commit message.

Submit the URL of your report in Blackboard:

* Click on HW3 under Assignments in Blackboard.
* Under "Assignment Submission", click the "Write Submission" button.
* Copy/paste the URL of your report into the edit box
  * should be something like https<nolink>://github.com/cs432-websci-fall20/hw3-ranking-*username*/blob/master/report.{pdf,md}
* Make sure to "Submit" your assignment.
