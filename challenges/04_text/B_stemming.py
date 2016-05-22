#!/bin/env python

# In this challenge, we are going to prepare a document for processing

with open('../../data/03_text.md', 'r') as f:
    document = f.read()

# 1. Tokenize this document using one of NLTK's built-in functions

from nltk import something
token_list = tokenize(document)

# 2. Stem this document using the Snowball Stemmer, and serialize it to disk
# under the data folder as 'stemmed_document.json'

from nltk import something_else
stem_list = stemmed token_list # use list comprehension here?
write stem_list to json

# 3. Find the ten most common terms and put them in an object called 'stop_list'
