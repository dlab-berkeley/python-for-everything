#!/bin/env python

# Welcome to the Ministry of Silly Functions! We'll start our first challenge of the day by doing some fun things with lists!

## 1. Write a function that inserts "In the name of Arthur of the House
## Pendragon, the first of his name, King of the Britons, Defeater of
## the Saxons, and Sovereign of all England:" to the *beginning* of a list

def prepend_arthur():
    pass

## 2. Write a function that returns only the second half of a list

def get_second_half():
    pass

## 3. Write a function that calculates the average value in a list

def get_mean():
    pass


## The stuff below here is okay -- no need to fix it!
if __name__ == '__main__':
    text_list = ["We dine well here in Camelot", "We eat ham and jam and Spam a lot"]
    text_list = prepend_arthur(text_list)
    for line in text_list:
        print(line)
