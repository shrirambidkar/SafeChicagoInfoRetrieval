# -*- coding: utf-8 -*-
#**********************************************************************
# FILENAME :        demo.py            
#
# DESCRIPTION :
#       This is the startup file which will be run by the user to run streaming 
#       program which will provide stream twitter with gun violance tags for 
#       project Safe Chicago
#
# NOTES :
#       Since this is initiator for the program we need to ensure file structure is intact
# 
# AUTHOR :    Shriram Bidkar        START DATE :    Feb 01 2020
#
# CHANGES :
# VERSION   DATE            WHO                 DETAIL
# V1.0      01/01/2020      Shriram Bidkar      First baseline version V1.0
#
#**********************************************************************
# import important packages which will help us invoke other python scripts
import os
import sys

# Below is the introduction which explains what and how of this program  
print("============================================================================")
print("                      Welcome to Project Safe Chicago")
print("This program will allow us to run a demo which will provide below things - ")
print("  1. As part of web crawling stream twitter API through tweepy wrapper.")
print("  2. Collect all the tweets related to gun violance in a tweet.json file")
print("  3. Split the files into multiple files (tweetn[n].json) of size 200MB")
print("============================================================================")
print("For this program to run we need few prequisites which includes - ")
print("  1. Packages - please refer to README.txt for list of dependent packages")
print("  2. Working Directory - place where we have demo.py file")
print("Please make sure all the files including dataset is located in the same folder")
print("and invoke this file (demo.py) from the that folder.")
print("Please NOTE - The program once run will exit after collecting 1 GB of data.")
print("While collecting the data it will generate tweet1.json, tweet2.json and so on")
print("with 200 MB of json files each until it reaches 1 GB.")
print("============================================================================")

# Take input from user to start the program
try:
    start_key = input("Please hit enter key to start the program ->")
except:
    print ("")
    sys.exit()

# Make the current path as absolute path and use it everywhere in subsequent programs
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
print ('Your current working directory - ', dname)

# Ensure the folder and file structure is correct and give user a opportunity to correct
try:
    ter_key = input("We assume all files are under this directory, if YES please enter [Y] to continue else [N] to terminate -> ")
    print("")
    if ter_key.lower() not in ['y']:
        sys.exit()

except:
    print ("")
    sys.exit()
print("============================================================================")
print("Now we will start the crawling process through Twitter API")
print("")
print(" Streaming tweets...")
print("")

# If everything is correct with the folder structure and files within the folder, run the program
os.system('python -W ignore twitterStreaming.py')
print ('We successfully crawled using twitter API with tag gun violance')
print ('Please find tweet<n>.json files under -', dname)
print ("")

# End of the file