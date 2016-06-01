#!/bin/env python

import requests
from bs4 import BeautifulSoup

# In this challenge, you are going to practice handling HTML data by
# grabbing the data out of a page that tells you the time

## 1. Write a function that downloads the page at "whattimeisit.com"
## and returns it as a response object

def get_page():
    pass

## 2. Write a function that accepts a response object, and returns the
## time as a string

def get_time():
    pass

## The stuff below here is okay -- no need to fix it!
if __name__ == '__main__':

    page = get_page()
    print(get_time(page))
    print("""\n\n
    ## If you really want to blow your mind, open up 'isitchristmas.com'
    ## in a browser and compare the human-rendered version with the
    ## source code.
    """)
