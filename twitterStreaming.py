# -*- coding: utf-8 -*-
#**********************************************************************
# FILENAME :        twitterStreaming.py            
#
# DESCRIPTION :
#       This file invokes the twitter streaming API and starts streaming   
#       tweets with different combination of #gun violance tags for 
#       project Safe Chicago. Features of this streamer is - 
#       1. Multi threading capability (utilizes in-built capability of tweepy)
#       2. Filters tweets which has geo-location avaiable in the tweets
#       3. Generates multiple JSON files of 200 MB each up to 1 GB
#
# NOTES :
#       Tweet streaming file. This is being called by demo.py
# 
# AUTHOR :    Shriram Bidkar        START DATE :    Feb 01 2020
#
# CHANGES :
# VERSION   DATE            WHO                 DETAIL
# V1.0      01/01/2020      Shriram Bidkar      First baseline version V1.0
#
#**********************************************************************

# import important packages
import tweepy                           # twapper to twitter streming API
import os                               # for file operations
from os import sys                      # for file and error handling operations
import json                             # for generating JSON file

# Set authentication tokens 
consumer_key = 'QR6UCZ31ZIMHAolocna0zMJmn'
consumer_secret = 'JUTN8UzDmEzozWMnuocHkPeOYxgh9WDsj7RoAR9OhyGBBwfSIq'
access_token = "111956853-D2hjbJe9tm0JAlP7oL0pEmoCcCTipoGBbcUDNcih"
access_token_secret = "PhUsoTwbTccx2VPjsg2eU4N8Cs9Ot5OxX6y2rKukeGLBy"

# StreamListener class inherits from tweepy.StreamListener and overrides on_status/on_error methods.
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        
        # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        is_retweet = hasattr(status, "retweeted_status")

        # check if text has been truncated
        if hasattr(status,"extended_tweet"):
            text = status.extended_tweet["full_text"]
        else:
            text = status.text

        # check if this is a quote tweet.
        is_quote = hasattr(status, "quoted_status")
        quoted_text = ""
        if is_quote:
            # check if quoted tweet's text has been truncated before recording it
            if hasattr(status.quoted_status,"extended_tweet"):
                quoted_text = status.quoted_status.extended_tweet["full_text"]
            else:
                quoted_text = status.quoted_status.text

        # remove characters that might cause problems with csv encoding
        remove_characters = [",","\n"]
        for c in remove_characters:
            text.replace(c," ")
            quoted_text.replace(c, " ")
        
        # filter twitter streams which has location attriutes 
        if (status.user.location is not None):  
            json_status = { "created" : status.created_at,
                            "name" : status.user.screen_name,
                            "id_str" : status.id_str,
                            "loc" : status.user.location,
                            "coords" : status.coordinates,
                            "isRetweet" : is_retweet,
                            "isQuote" : is_quote,
                            "text" : status.text,
                            "quotedText" : quoted_text,
                            "user_created" : status.user.created_at,
                            "followers" : status.user.followers_count,
                            "retweets" : status.retweet_count,
                            "bg_color" : status.user.profile_background_color,
                            "description" : status.user.description} 

#           set the JSON file size to 200 MB. Once the file reaches 200 MB it will split and generate another file
#            file_size = 200000000       
            file_size = 2000       

#           Validate the size of the JSON file. If the size is greater than 200 MB generate another file
            with open('tweet1.json', 'a', encoding='utf-8') as f:
                if (int(os.stat('tweet1.json').st_size < file_size)):    
                    json.dump(json_status, f, default=str, ensure_ascii=False, indent=4)
                else:
                    with open('tweet2.json', 'a', encoding='utf-8') as f:
                        if (int(os.stat('tweet2.json').st_size < file_size)):    
                            json.dump(json_status, f, default=str, ensure_ascii=False, indent=4)
                        else:
                            with open('tweet3.json', 'a', encoding='utf-8') as f:
                                if (int(os.stat('tweet3.json').st_size < file_size)):    
                                    json.dump(json_status, f, default=str, ensure_ascii=False, indent=4)
                                else:
                                    with open('tweet4.json', 'a', encoding='utf-8') as f:
                                        if (int(os.stat('tweet4.json').st_size < file_size)):    
                                            json.dump(json_status, f, default=str, ensure_ascii=False, indent=4)
                                        else:
                                            with open('tweet5.json', 'a', encoding='utf-8') as f:
                                                if (int(os.stat('tweet5.json').st_size < file_size)):    
                                                    json.dump(json_status, f, default=str, ensure_ascii=False, indent=4)
                                                else:
                                                    return False

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()

    def on_timeout(self):
        ("Timeout... (", sys.stderr, ")")
        return True # Don't kill the stream

# complete authorization and initialize API endpoint
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# initialize stream
streamListener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=streamListener,tweet_mode='extended')
tags = ["gun violence", 
        "gunviolence", 
        "Gun violence", 
        "Gun Violence", 
        "gun Violence", 
        "gunViolence", 
        "Gunviolence", 
        "GUNVIOLENCE", 
        "GUN VIOLANCE",
        "violance"]
stream.filter(track=tags, is_async=True)

# End of the file