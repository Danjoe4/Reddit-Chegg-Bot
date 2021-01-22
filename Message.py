# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:23:32 2020

@author: Daniel Broderick
"""
import praw
import prawcore


#is it okay to do this? best not
#r = praw.Reddit("bot1", config_interpolation="basic")
dict = {}


def init_msg(author, links):
    """Formulates the initial message, used by RedditReadWrite
    """
    dict[author] = links #store the authors name and their links
    
    link_count = len(links)
    cost = round(.1 + link_count*0.20*.986**link_count, 1)
    links_str = ""
    for link in links: #convert links to a string format
        links_str += link + "\n\n"
    
    print(author)
    message = "Hello " + str(author) + ". I found " + str(link_count) + " links in your" \
    " pastelink. PLease confirm these are them: \n\n" + links_str + \
    "The cost will be $"+ str(cost)+ "0; accepted payment methods include (1)Paypal "\
    ". If you no longer need your Chegg answers, I can (0)leave. " \
    "Please respond with the number corresponding to your desired action."
    
    print(message)
    return message



def response():
    """detects user input
    """
    



if __name__ == "__main__":
    init_msg('/u/Danjoe4', ['https://www.chegg.com/homework-help/questions-and-answers/1-applications-5pts-fill-input-output-table-digital-logic-circuit-output-abc-l-output-10-1-q49228255', 'https://www.chegg.com/homework-help/questions-and-answers/5-prove-set-z-xz-x-71-x-zt-countable-7-marks-q41675202?trackid=8b5e4d188886&strackid=703be631d281'])