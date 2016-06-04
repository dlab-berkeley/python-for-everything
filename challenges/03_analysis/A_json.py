#!/bin/env python

# In this challenge, you are going to write a recursive function to search
# for fields in a json object. A recursive function is a function that
# calls itself during runtime, and is often used to navigate data structures
# that are nested or linked. Because we haven't seen recursive functions yet
# we're going to provide you with "pseudo code" that you'll need to translate
# into Python. When iterating through a json object, there are four cases we
# need to consider.
# 1. We are inside a dict, and need to check if the key equals the search term
# 2. We are inside a dict, and need to search any dicts we find
# 3. We are inside a list, and need to search any dicts we find
# 4. We are inside a container, and need to ignore any strings/ints we get
# In the second and third case, we want to get a results object back (which
# will be a list) and add it to the results object we have in the upper call.

def search(json_object, item):
    initialize empty result list
    if the json object is a dictionary
        iterate through the key/value pairs
            if the key is the item
                add the item to the results list
            else if the value is a dictionary
                add the output of searching the value to the result list
    else if the json object is a list:
        iterate through the things in the list
            if any of those things are a dictionary
                add the output of searching the thing to the result list
    return the result list
