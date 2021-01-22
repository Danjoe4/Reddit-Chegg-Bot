# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:09:38 2020

@author: Daniel Broderick
"""

from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib.parse import urlparse, urljoin
import re



def getLinks(url):
    """Takes a pastelink and returns an array of chegg links.
    """
    links = []
    print(url)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html.read(), 'lxml')
    
    
    
    for link in soup.find_all('a', limit = 75):
        foo = link.get('href')
        if "www.chegg.com/" in foo:
            if link_is_valid(foo):
                links.append(foo)
            else: #return the list as is if there is a broken link 
                return links
            
    return links


def link_is_valid(url):
    print(url)
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
    
    
    

if __name__ == "__main__":
    print(getLinks("https://pastelink.net/1lqma"))