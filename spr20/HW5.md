*This is the public posting of the assignment. See Piazza for the invite link to make your submission in your own repository in the class organization.*

# Homework 5 - Graph Partitioning
**Due:** Tuesday, March 24, 2020 *by 11:59pm*

## Assignment 

**Q1.**  We know the result of the Karate Club (Zachary, 1977) split. Prove or disprove that the result of split could have been predicted by the weighted graph of social interactions.  How well does the mathematical model represent reality?

Generously document your answer with all supporting equations, code, graphs, arguments, etc.

Clues: 
1. Draw original Karate club graph (two connected components) after split (see [Week-06 slides 86-87](https://docs.google.com/presentation/d/1vJhPxA_ybU1y7CJZvBqqjD7MZjSZN9BZz4yhlJ_XF6g/edit#slide=id.g7e0acafd7b_0_0)).
2. Run multiple iterations of graph partioning algorithm (e.g., Girvan-Newman Algorithm) on experimental Karate Club graph until the graph splits into two connected components.
3. Compare the connected components of the experimental graph (in 2.) with the original connected components of the split Karate club graph (in 1.). Are they similar?

Useful resources

* Original paper, http://aris.ss.uci.edu/~lin/76.pdf
* [Week 6 Slides](https://docs.google.com/presentation/d/1vJhPxA_ybU1y7CJZvBqqjD7MZjSZN9BZz4yhlJ_XF6g/edit)
* https://en.wikipedia.org/wiki/Zachary's_karate_club
* Data: http://vlado.fmf.uni-lj.si/pub/networks/data/Ucinet/UciData.htm#zachary
* Example code
  * [Python NetworkX](https://networkx.github.io/documentation/networkx-1.9/index.html) - https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.generators.social.karate_club_graph.html
  * Python NetworkX - https://networkx.github.io/documentation/networkx-1.9/examples/graph/karate_club.html
  * Jupyter notebook (see #14) - http://nbviewer.ipython.org/url/courses.cit.cornell.edu/info6010/resources/11notes.ipynb
  * [Snap.py](https://snap.stanford.edu/snappy/doc/tutorial/index-tut.html) - https://snap.stanford.edu/snappy/doc/reference/CommunityGirvanNewman.html
  * [Python igraph](https://igraph.org/python/) - http://igraph.org/python/doc/igraph-pysrc.html#Graph.community_edge_betweenness
  * http://stackoverflow.com/questions/9471906/what-are-the-differences-between-community-detection-algorithms-in-igraph/9478989#9478989
  * http://stackoverflow.com/questions/5822265/are-there-implementations-of-algorithms-for-community-detection-in-graphs

## Extra Credit

**Q2.**  *(Extra credit, 3 points)* We know the group split in two different groups.  Suppose the
disagreements in the group were more nuanced -- what would the clubs
look like if they split into groups of 3, 4, and 5?

**Q3.** *(Extra credit, 10 points)* Use D3.js's force-directed graph layout to draw the Karate Club Graph before split. Color the nodes according to the factions they belong to (John A or Mr. Hi). After a button is clicked, split the graph based on the original graph split. Include a link to the HTML/JavaScript files in your report and all necessary screenshots.

See: https://bl.ocks.org/mbostock/4062045, https://d3js.org/

## Submission

Make sure that you have committed and pushed your local repo to GitHub before the deadline.  

*You do not need to submit anything to Blackboard.*
