# Twitter, twarc Setup

## Setup Steps

There are several steps that need to be completed before you can use twarc and the Twitter API.  These are based on the [Twitter Developer Access page](https://twarc-project.readthedocs.io/en/latest/twitter-developer-access/) from the twarc documentation:

[Step 0: Have a Twitter account](https://twarc-project.readthedocs.io/en/latest/twitter-developer-access/#step-0-have-a-twitter-account-in-good-standing)

[Step 1: Apply for a Developer Account](https://twarc-project.readthedocs.io/en/latest/twitter-developer-access/#step-1-applying-for-a-developer-account)  

Answer each question *carefully and completely*. State that you are a student taking a college course (CS 432/532 at Old Dominion University) and that you will be using the Twitter API to complete assignments for the course (provide your ODU email as contact to prove that you're a student). The course requires that you collect tweets based on a search query, analyze links shared in tweets, and analyze account follower counts. None of the data will be shared publicly or shared with government entities. The raw data will only be shared with your instructor and teaching assistant for grading purposes.

*Step 1 should be completed as soon as possible. If you provide incomplete answers, it could take several rounds of emails before you are approved.* ***If you have not received the approval email by the time HW1 has been assigned, please contact the instructor.***

Since this is for a class, skip Step 2 and move to [Step 3: Create a Project and App](https://twarc-project.readthedocs.io/en/latest/twitter-developer-access/#step-3-create-a-project-and-app).  

You only need "Read Only Access" since we will not be making posts.  And you will be creating a "Standard Access Project" since we will be using the Twitter API v2.

[Step 4: Collaborating with Others](https://twarc-project.readthedocs.io/en/latest/twitter-developer-access/#step-4-collaborating-with-others). Read this information carefully.

[Step 5: Next Steps](https://twarc-project.readthedocs.io/en/latest/twitter-developer-access/#step-5-next-steps)

Install [twarc2](https://twarc-project.readthedocs.io/en/latest/) with `python3 -m pip install --upgrade twarc`

* If you're using Windows 10, see [installing twarc2 on Windows 10](https://twarc-project.readthedocs.io/en/latest/windows10/)

Using the keys that you obtained in Step 3, configure twarc with `twarc2 configure`

* Answer `y` to the question `(Optional) Add API keys and secrets for user mode authentication [y or n]?` and enter the API key and secret you saved in Step 3.
* If you have already generated (and saved) the "Access Token and Secret" (different from your API Key and Secret), answer `2` to the question `How would you like twarc to obtain your user keys?`. Otherwise, answer `1` and twarc will walk you through the process.
* Note the file where twarc reports your keys have been written.

## Resources

Here are a few helpful resources that you'll want to be familiar with for assignments this semester.

[twarc2 API documentation](https://twarc-project.readthedocs.io/en/latest/api/client2/)

[Twitter tweet object format](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet)

[Python examples using twarc2 API](https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research/blob/main/modules/6b-labs-code-standard-python.md)
