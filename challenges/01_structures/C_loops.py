#!/bin/env python

# Welcome back to the Ministry of Silly Functions! Our third challenge
# of the day is going to be about loops!

## 1. Write a function that turns the items in a list into keys in a
## dictionary, then returns the dictionary.

def list_to_dict(L):
    pass

## 2. We saw how to print each letter in 'berkeley' on a separate
## line using a `for` loop. Dillon has tried to do the same thing with
## a `while` loop, but he made some mistakes. Let's fix them!

def print_while():
    best_public_university = 'berkeley' # the string we want to print
    index = 1 # initialize a counter to get us out of the while loop
    while index > len(best_public_university): # while index is in the string
        print(best_public_university) # print the value at the index
