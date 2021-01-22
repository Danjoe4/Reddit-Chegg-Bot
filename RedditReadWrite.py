# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:59:19 2020

@author: Daniel Broderick
"""
import praw
import prawcore

import re
import requests
import time
import traceback
import time

import PasteLinkPull
import Message

r = praw.Reddit("bot1", config_interpolation="basic")
dict = {} #this will store the 
replied_to = []


def run():
    while 1:
        parseInstantChegg()
        time.sleep(10) 
        Message.response()
        time.sleep(10)
    
    


def parseInstantChegg():
    mainposturl= "https://www.reddit.com/r/InstantCheggAnswers/comments/gexfjn/comment_your_pastelink_and_uchegganswermachine/"
    submission = r.submission(url=mainposturl)
    for cmt in submission.comments:
        is_comment(cmt)
        if cmt.stickied == True:
            set_status(cmt, 1)



def is_comment(cmt):
    """checks if the comment is appropriate to reply to and use
    """
    #if cmt.parent_id[:3] == "t1_": # only proceed if the parent is a comment
    #implement this ^ if it starts replying to itself or performance is lacking
    
    age = time.time() - cmt.created_utc
    print("cmt age",age)
    if age < 600 and cmt.id not in replied_to and cmt.author != "u/CheggAnswerMachine":
    #proceed if comment is less than 10min old, not already replied to, and cmt author not self
        
        if link_checker(cmt):
            #variables that need to be sent to our DM bot
            links_tmp =  PasteLinkPull.getLinks(comment_to_url(cmt))
            message = Message.init_msg(cmt.author, links_tmp) 
            
            cmt.reply("I've found the links. Check your inbox")
            replied_to.append(cmt.id) #mark as replied to
            r.send_message(cmt.author, "Your Chegg links", message)
            #sends the user the initial message
            
        else:
            cmt.reply("Not a valid url")
            print("Link checker did not detect a valid url")
            replied_to.append(cmt.id)
    return




def comment_to_url(cmt):
    """bullshit formatting necessary because of reddits weird link system
    """
    url = re.findall(r'(https?://\S+)', cmt.body)[0]
    url = url.split(')')[0]
    print(url)
    return url



def link_checker(cmt):
    """transforms the comment into a url then checks if that url is a 
    valid pastelink with valid Chegg links via the PasteLinkPull doc"""
    if "pastelink.net/" in cmt.body:
        url = comment_to_url(cmt)   
    else:
        return False
    return PasteLinkPull.link_is_valid(url)

        

def set_status(cmt, status):
    if status == 0:
        cmt.edit("Status: Offline")
    elif status == 1:
        cmt.edit("Status: Online for testing purposes only. Still in development")
    elif status == 2:
        cmt.edit("Status: Fully operational and accepting links.")
    else:
        cmt.edit("Status: Broken. Please contact u/Danjoe4 and let him know")
    return



if __name__ == '__main__':

        try:
            run()

        except praw.exceptions.APIException:
                print('An API exception happened.')
                time.sleep(30)
        except prawcore.exceptions.ServerError:
            print('503 error occurred.')
            time.sleep(180)
        except prawcore.exceptions.InvalidToken:
            print('401 error: Token needs refreshing.')
            time.sleep(30)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            traceback.print_exc()
            time.sleep(30)