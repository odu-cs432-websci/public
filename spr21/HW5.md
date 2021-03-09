*This is the public posting of the assignment. See Blackboard for the invite link to make your submission in your own repository in the class organization.*

# Homework 5 - Graph Partitioning
**Due:** Sunday, March 28, 2021 by 11:59pm

## Assignment 

We know the result of the Karate Club (Zachary, 1977) split. ***Prove or disprove that the result of split could have been predicted by the weighted graph of social interactions.***  How well does the mathematical model represent reality?  Generously document your answer with all supporting equations, code, graphs, arguments, etc.

Use a Python or JavaScript library (as discussed in [Week-09 Graph Vis](https://docs.google.com/presentation/d/1M_c2CKSnVS9fe-1vAfV4sac6KoZ36KdknFiYBL575uw/edit?usp=sharing)) to generate the graphs and illustrate the Girvan-Newman algorithm graph partitioning algorithm.

Report reminders:
* Reports are not just a list of questions and answers, but *must* include descriptions, screenshots, copy-paste of code output, references, as necessary.  For each question you address, you must describe how you answered the question, including describing the code you wrote to accomplish the task.  
* All graphs that you generate must be done in R or using a Python plotting library, and images must be inserted into your report.
* All reports must have a section labeled "References" for listing the outside resources you consulted.
  * You may use existing code, but you **must** document and reference where you adapted the code -- give credit where credit is due! *Use without attribution is plagiarism!*
* All reports must include your name, class (make sure to distinguish between CS 432 and CS 532), assignment number/title, and date.

### Steps

1. Draw the original Karate club graph (before the split) and color the nodes according to the factions they belong to (John A or Mr. Hi).

2. Run multiple iterations of the Girvan-Newman graph partioning algorithm (see [Week-07 Social Networks](https://docs.google.com/presentation/d/1G9bY32EslxRdIq7znDZoGJd3-_Ock1FeJcqN3QgQuy4/edit?usp=sharing), slides 90-99) on the Karate Club graph until the graph splits into two connected components. Keep the node colors the same as they were set in Q1. *How many iterations did it take?*  
    * Your report should include images of all of the iterations.  It will be easier to see the splits if you use a force-directed layout (such as Kamada-Kawai) rather than a circular layout.

3. Compare the connected components of the experimental graph (Step 2) with the connected components of the split Karate club graph (Step 1). *Are they similar?  Did all of the same colored nodes end up in the same group?  If not, what is different?*

Note that it is not sufficient just to show the output of three steps.  You must provide an explanation of what is going on and an argument that "proves or disproves that the result of split could have been predicted by the weighted graph of social interactions".

### Useful Resources

* Wayne Zachary, ["An Information Flow Model for Conflict and Fission in Small Groups"](http://aris.ss.uci.edu/~lin/76.pdf), 1977 - original paper 
* [Zachary's Karate Club](https://en.wikipedia.org/wiki/Zachary's_karate_club) (Wikipedia)
* Data 
   * matrix format: [UCINET IV Version 1.0 DATASETS](http://vlado.fmf.uni-lj.si/pub/networks/data/Ucinet/UciData.htm#zachary)
   * GML file: [Gephi Datasets](https://github.com/gephi/gephi/wiki/Datasets)
   * [karate_club_graph()](https://networkx.org/documentation/stable/auto_examples/graph/plot_karate_club.html) in [NetworkX](https://networkx.org/documentation/stable/index.html)
* Example code
  * [CS 432/532 Google Colab notebook](https://github.com/cs432-websci-master/public/blob/main/432_NetworkX_example.ipynb) - [direct link](https://colab.research.google.com/github/cs432-websci-master/public/blob/main/432_NetworkX_example.ipynb) *if GitHub one doesn't work*
  * [CommunityGirvanNewman](https://snap.stanford.edu/snappy/doc/reference/CommunityGirvanNewman.html) in [Snap.py](https://snap.stanford.edu/snappy/doc/tutorial/index-tut.html) 
  * [community_edge_betweenness()](https://igraph.org/python/doc/api/igraph.Graph.html#community_edge_betweenness) in [igraph-python](https://igraph.org/python/) 
  * ["What are the differences between community detection algorithms in igraph?"](http://stackoverflow.com/questions/9471906/what-are-the-differences-between-community-detection-algorithms-in-igraph/9478989#9478989), StackOverflow question/answer
  * ["Are there implementations of algorithms for community detection in graphs? "](http://stackoverflow.com/questions/5822265/are-there-implementations-of-algorithms-for-community-detection-in-graphs), StackOverflow question/answer

## Extra Credit

### Q1. (1 point)
We know the group split in two different groups.  Suppose the disagreements in the group were more nuanced.  *What would the clubs look like if they split into 3, 4, and 5 groups?*  A single node can be considered as a "group".

### Q2. 
Use D3.js's force-directed graph layout to draw the Karate Club Graph before the split. Color the nodes according to the factions they belong to (John A or Mr. Hi). After a button is clicked, split the graph based on the original graph split. Include a link to the HTML/JavaScript files (or Observable notebook) in your report and all necessary screenshots.
* If you load a new file containing the split upon button press, this EC is worth 2 points.
* If you modify the nodes and edges using D3 (without loading a new file), this EC is worth 4 points.
* If you use D3 transitions to move the nodes and edges to their new locations, this EC is worth 6 points.

## Submission

Make sure that you have committed and pushed your local repo to GitHub.  Your repo should contain any code you developed to answer the questions.  Include "Ready to grade @weiglemc @brutushammerfist" in your final commit message. 

Submit the URL of your *report* in Blackboard:

* Click on HW5 under Assignments in Blackboard
* Under "Assignment Submission", click the "Write Submission" button.
* Copy/paste the URL of your report into the edit box
  * should be something like https<nolink>://github.com/cs432-websci-spr21/hw5-graph-*username*/blob/master/HW5-report.{pdf,md}
* Make sure to "Submit" your assignment. 
