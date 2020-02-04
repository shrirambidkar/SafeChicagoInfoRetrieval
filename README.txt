Project - Safe Chicago
With Safe Chicago project we will make Chicago a better and safer place to live, a place we all love, admire and appreciate using information Retrieval & Web Search Techniques

General info
In Chicago these days, the moment we start television news there is at least one news involving gun violence and innocent people are either injured or killed. Goal of this project 
is to provide search capability to the users to search relevant gun violence prone area based on location. This will provide users to take informed decision. In this search initially
we will perform web crawling through twitter streaming API using tweepy wrapper. The streamed tweets are collected in JSON format in batches of 200 MB. We collect roughly 5 JSON files
which eventually will be stored in database.


Technologies
Python 3.6.9 :: Anaconda, Inc.
    List of packages to be installed - 
    - json 2.0.9 [Default with Anaconda Distribution]
    - tweepy version 3.8.0

Setup
Navigate to folder where The entire package comes in zip file called "CS242ProjectCode.zip". Upon download please move this file to desired folder and unzip the file. Contains of the file are as below -
    1. twitterStreaming.py  ----- [Streams tweets using tweepy based twitter streaming API]
    2. demo.py              ----- [File to run the program which will invoke all above file` ]
    3. README.txt           ----- [README file - Read this file first!]
Validate if necessary tools and dependent packages are installed which are mentioned in the Technology section. Once environment is setup we can move to execution section which is described in below section.

Execution
Navigate to folder where file "CS242ProjectCode.zip" is unzipped. Invoke "demo.py" using python with command (illustrated below) on the terminal/cmd. This will initiate the system and will provide brief on the 
objective and what to expect from this system. Next system will prompt the user to hit enter to start the program. The system will share the present working directory and let the user confirm if the present working 
directory is same as where all the project files are located. With confirmation from user that everything is set, system will start streaming the tweets. While streaming the system will start generating JSON files
with size of 200 MB each. System will generate 5 json files with name tweet1.json, tweet2.json, tweet3.json, tweet4.json, tweet5.json. 
Below is the example of system with various prompts user is expected -    

    > python demo.py
    .
    .
    Please hit enter key to start the program ->
    .
    .
    We assume all files are under this directory, if YES please enter [Y] to continue else [N] to terminate -> 
    .
    .


Features
This project will provide below features as part A -
    1. Web crawling capability using twitter streaming API via tweepy wrapper.
    2. Index the crawled data using Lucene indexer

Status
Project is: In-progress

References 
1. http://docs.tweepy.org/en/latest/install.html

Contact
sbidk002@ucr.edu
