#!/bin/env python

# In this challenge, we are going to use regular expressions to manipulate
# text data

import re

# 1. Compile a regular expression that matches URLs

P_URL = re.compile(r'http://dlab\.berkeley\.edu', flags=re.I)

# 2. Using that pattern, write a function that pulls all of the URLs out of a document and returns them as a list

def get_urls(document):
    assert that document is a string object
    initialize empty list
    for match in re.something:
        get match group
        append match group to list
    return list
