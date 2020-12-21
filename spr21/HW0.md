# Homework 0: Course Setup

**Recommended Due Date:** Tuesday, January 19, 2021 

This is an *optional, but highly recommended* assignment. It will cover the necessary steps to get set up for the semester.  There is nothing to submit, but there are review questions listed so that you can assess your own understanding.

*For this assignment only -- you may ask others in the class for help with these setup tasks. Please use Piazza and post in the `homework` folder for these questions so that others may benefit from the answers.* 

## ODU-CS Linux

We will be using the [ODU-CS Linux systems](https://systems.cs.odu.edu/Unix_and_Linux_Services) for part of the course (read the information in the linked webpage). If you do not already have an account, request one at https://accounts.cs.odu.edu/validate/

If you are not familiar with Unix/Linux systems, I strongly encourage you to read the materials from [CS 252 - Unix for Programmers](https://www.cs.odu.edu/~zeil/cs252/latest/Directory/outline/index.html). 

Create a directory for files for this course (name it whatever you wish, but something like `cs432-s21` or `cs532-s21` is probably a good idea). Change the permissions on this directory so that you are the only user who can read, write, or execute (view the contents) the directory (see ["Protection and Permission"](https://www.cs.odu.edu/~zeil/cs252/latest/Public/protection/index.html)).

In the directory that you just created, use the simple nano editor to create a file named text.txt (`nano test.txt`) with the following contents:
```
CS 800
CS 432
CS 725
MATH 212
MATH 32
```

**Q1.** Execute the following commands and make sure you understand what each command does: 
* a) `wc -l test.txt`
* b) `echo "CS 800" >> test.txt; cat test.txt`
* c) `grep CS test.txt`
* d) `grep -c CS test.txt`
* e) `sort test.txt`
* f) `sort -k2 test.txt`
* g) `sort -k2 -n test.txt`
* h) `sort test.txt | uniq -c`


For more information, see ["Redirection and Pipes"](https://www.cs.odu.edu/~zeil/cs252/latest/Public/redirection/index.html).  For information on the Unix commands, you can use the `man` command (ex: `man grep`) to display the manual page or do a web search for the command.

## Python

You can use Python 3 on the ODU-CS Linux machines *(make sure to use /usr/bin/python3 and **not** /usr/bin/python)* or you can [download it ](https://www.python.org/downloads/) and run on your local machine.  Review some of the [important differences between Python 2.7 and Python 3](https://www.geeksforgeeks.org/important-differences-between-python-2-x-and-python-3-x-with-examples/).

**Q2.** Practice executing a Python program on the ODU-CS machines. Pick one of the "Python Strings" examples from [Python examples](https://www.w3schools.com/python/python_examples.asp), save it to a file in the directory you created in the previous section, and execute it using Python 3.

## Google Colab

[Google Colab](https://colab.research.google.com) is a project to host Python-based [Jupyter notebooks](https://jupyter.org/) in the cloud.  We'll look at many of our Python (and R) examples using this service.  For more information about Google Colab, see their [FAQ](https://research.google.com/colaboratory/faq.html).

Make sure you're logged into a Google account (either a personal one or your ODU student account) and open [Overview of Colaboratory Features](https://colab.research.google.com/notebooks/basic_features_overview.ipynb). Walk through and execute the examples shown.  Experiment with changing some of the code and re-execute the cells.

**Q3.** Create a new cell in the notebook and copy in and execute the code you used in **Q2**.

## Git, GitHub

Git is a version control system for tracking changes in source code, used in the popular [GitHub](https://github.com) code hosting platform.  To become familiar with the basics of Git, read [git - the simple guide](https://rogerdudler.github.io/git-guide/).

If you do not have one already, you must create a GitHub account.  I recommend a username that incorporates at least part of your actual name (e.g., mine is [weiglemc](https://github.com/weiglemc)).  If you already have a GitHub account, you do *not* need to create a new one for this class.

Mr. Thomas Kennedy has a nice introduction and walkthrough of Git available.  Read through [his materials](https://git-community.cs.odu.edu/tkennedy/git-workshop/-/wikis/Git-Workshop) and work through all of the exercises in the "Setting Up a Local Git Repository" section to create a repository, make changes, commit them locally, and then create a remote repo at GitHub.  

Notes about the "Adding a Remote" section:
* You will be using GitHub (not GitLab)
* Mr. Kennedy's example output is based on using GitLab and git-community.cs.odu.edu.  You are not using that system.

**Q4.** What is your GitHub username?

**Q5.** What is the URL of your remote GitHub repo (created through Mr. Kennedy's exercises)?

## Markdown

Markdown is a lightweight markup language that is widely used in GitHub, especially for README pages.  

Here are some helpful links for Markdown (and GitHub-flavored Markdown):
* [Markdown Basic Syntax](https://www.markdownguide.org/basic-syntax)
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Markdown on GitHub](https://help.github.com/en/categories/writing-on-github) -- it can be slightly different than regular Markdown
  * [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) (GitHub flavor)

**Q6.** Complete the following tasks:
* a) Create a bulleted list with at least 3 items
* b) Write a sentence or paragraph that demonstrates the use of *italics*, **bold**, ***bold italics***, and `inline code`.
* c) Create an example of a fenced code block.
* d) Create a level 4 heading
* e) Create a line that includes a link to a website (your choice)

## LaTeX and Overleaf

LaTeX is *the* markup language for academic publication. [Overleaf](https://overleaf.com) provides an online setup for writing and compiling LaTeX into PDF.  

Sign up for a free [Overleaf](https://overleaf.com) account.

Walk through [part 1](https://www.overleaf.com/learn/latex/Free_online_introduction_to_LaTeX_(part_1)) and [part 2](https://www.overleaf.com/learn/latex/Free_online_introduction_to_LaTeX_(part_2)) of this [LaTeX introduction](https://www.overleaf.com/learn/latex/Free_online_introduction_to_LaTeX_(part_1)). 

If you are in CS 532, you must use LaTeX for writing your HW reports.  I've provided a [report template](https://www.overleaf.com/read/tzvqcjvjtgdx) in Overleaf.

**Q7.** What environment is used for bulleted lists?  What command is used to start a bulleted list?

**Q8.** What is the command to include an image in a LaTeX file?

## Web Science Tools

Two tools that you'll use this semester are [Memgator](https://github.com/oduwsdl/MemGator) and the [Twitter Developer API](https://developer.twitter.com/en).  Getting these set up now will save you a lot of time later in the semester.

### Memgator
Download and install a local version of Memgator
* Go to the Releases page in the repository, https://github.com/oduwsdl/MemGator/releases
* Scroll down to the "Assets" section.  Click the triangle icon to expand the list.  Choose the executable that matches your OS.
  * -darwin is for MacOS
  * -386 is for 32-bit architectures (older machines)
  * -amd64 is for 64-bit architectures (newer machines)

Memgator is a command-line tool, so you will need to run it from Terminal (for MacOS) or PowerShell (for Windows).  You may need to set the permissions to executable before it will run.
* MacOS: If you get a security pop-up the first time you run it, open Finder to where you've installed it.  Right-click on memgator and choose Open.  Then you'll be able to select 'Open' from the pop-up.  Once you've done that, you'll be able to run it from the command line.

**Q9.** Test out your installation of memgator with the following example.  The result in `mweigle-tm.json` should be similar to what you see below.  What do the `-F 2` and `-f JSON` options do?
* `%` is the command line prompt (don't type that in)
* Replace `memgator-darwin-amd64` with the appropriate executable for your system

```
% ./memgator-darwin-amd64 -F 2 -f JSON https://www.cs.odu.edu/~mweigle/ > mweigle-tm.json
% head mweigle-tm.json
{
  "original_uri": "https://www.cs.odu.edu/~mweigle/",
  "self": "http://localhost:1208/timemap/json/https://www.cs.odu.edu/~mweigle/",
  "mementos": {
    "list": [
      {
        "datetime": "2006-08-30T23:22:00Z",
        "uri": "https://web.archive.org/web/20060830232200/http://www.cs.odu.edu/~mweigle/"
      },
      {
``` 

### Twitter

Apply for a [Twitter Developer Account](https://developer.twitter.com/en/apply-for-access).  The form will ask for a reason and just state that you're using this for a class project and that data will not be shared publicly.

Download the test file [collect-tweets.py](collect-tweets.py) and insert your API keys in the `consumer_key` and `consumer_secret` variables.

**Q10.** Use `collect-tweets.py` to collect tweets:
* a) tweets related to 'coronavirus' (`python3 collect-tweets.py > coronavirus-tweets.json`)
* b) tweets related to 'ODU' (`python3 collect-tweets.py ODU > ODU-tweets.json`)
