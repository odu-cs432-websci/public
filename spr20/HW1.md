*This is the public posting of the assignment. See Piazza or Blackboard for the invite link to make your submission in your own repository in the class organization.*

# Homework 1 - Web Science Intro
**Due:** Tuesday, January 28, 2020 *before class*

## Assignment

Write a report that contains the answers to the following questions. (When you include an image in your report, *do not change the [aspect ratio](https://en.wikipedia.org/wiki/Aspect_ratio_(image)) of the image*. If you have trouble with this, ask for help in our Piazza group.)

Remember that students in CS 532 must submit a PDF generated with LaTeX (and submit both their PDF and .tex files).  Students in CS 432 are encouraged to use LaTeX, but may use Markdown.  

**Q1.**  Demonstrate that you know how to use `curl` well enough to correctly POST data to a form.  Show that the HTML response that
is returned is "correct".  That is, the server should take the arguments you POSTed and build a response accordingly.  Save the
HTML response to a file and then view that file in a browser and take a screen shot.

You may use this simple server for sending POST requests: https://www.cs.odu.edu/~mweigle/courses/cs532/namesEcho.php

The server needs you to POST data for the `fname` and `lname` fields.

**Q2.**  Write a Python program that
* takes as a command line argument the URI of a web page
* extracts all the links from the page
* lists all the links that result in PDF files, and prints out the bytes for each of the links.  (Note: be sure to follow all the redirects until the link terminates with a "200 OK".)

Show that the program works on 3 different URIs, one of which must be https://www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html

**Q3.**  Consider the "bow-tie" structure of the web in the Broder et al. paper (http://snap.stanford.edu/class/cs224w-readings/broder00bowtie.pdf) that was described in Week 1. 

Now consider the following links:

    A --> B
    B --> C
    C --> D
    C --> A
    C --> G
    E --> F
    G --> C
    G --> H
    I --> H
    I --> K
    L --> D
    M --> A
    M --> N
    N --> D
    O --> A
    P --> G 

Draw the resulting graph (either sketch on paper or use another tool) and include an image in your report.

For the above graph, give the values for
* IN: 
* SCC: 
* OUT: 
* Tendrils: 
* Tubes: 
* Disconnected:
    
## Submission

Make sure that you have committed and pushed your local repo to GitHub.  You should be using GitHub version control as you develop your solutions, so your repo should contain any code you developed to answer the questions.

Submit the URL of your report in Blackboard:

* Click on HW1 under Homeworks
* Under "Assignment Submission", click the "Write Submission" button.
* Copy/paste the URL of your report into the edit box
  * should be something like https<nolink>://github.com/cs432-websci-spr20/hw1-websci-*username*/blob/master/report.{pdf,md}
* Make sure to "Submit" your assignment.
