#!/bin/env python

# In natural language processing, a stop word is a functional word that
# doesn't contain much meaning, like 'the' or 'for'. These also tend to
# be the most common words, which means they don't add much to the analysis
# but take up a lot of memory and processing time. In this challenge, we
# are going to use a sample of text to generate our own list of stop words
# that we can remove from documents in the future.

## 1. Write a function that tokenizes a document using NLTK's
## word tokenizer

def get_tokens():
    pass

## 2. Write a function that stems a list of tokens using NLTK's Snowball
## stemmer and returns a list of stems.

def get_stems():
    pass

## 3. Write a function that takes a list of stems, finds the ten most
## common items, and returns them as a list

def get_stopwords():
    pass

## 4. Write a function accepts a list of stems and a list of stop words,
## removes those stop words from the list of stems, and returns the cleaned
## list.

def remove_stopwords(stopwords, document):
    pass

## The stuff below here is okay -- no need to fix it!
if __name__ == '__main__':
    print("""
    This module is meant to be imported into python, and has no
    command line interface
    """)
