#!/bin/env python

# In this challenge, you are going to practice manipulating json formatted
# data structures

## 1. Load "02_tweet.json" in from the data directory

tweet = json.load("02_tweet.json")

## 2. Write a function that takes a tweet and returns the data from all fields called "entities"

def entity_getter(json_object):
    for key in json_object:
        if the key is entities:
            yield value
        elif the value is a dictionary:
            entity_getter(json_object)
