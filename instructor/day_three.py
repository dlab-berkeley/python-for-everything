
# coding: utf-8

# # Text Data
# 
# ## Pre-introduction
# 
# We'll be spending a lot of time today manipulating text. Make sure you remember how to split, join, and search strings.

# ## Introduction
# 
# We've spent a lot of time in python dealing with text data, and that's because text data is everywhere. It is the primary form of communication between persons and persons, persons and computers, and computers and computers. The kind of inferential methods that we apply to text data, however, are different from those applied to tabular data. 
# 
# This is partly because documents are typically specified in a way that expresses both structure and content using text (i.e. the document object model).
# 
# Largely, however, it's because text is difficult to turn into numbers in a way that preserves the information in the document. Today, we'll talk about dominant language model in NLP and the basics of how to implement it in Python.
# 
# ### The term-document model
# 
# This is also sometimes referred to as "bag-of-words" by those who don't think very highly of it. The term document model looks at language as individual communicative efforts that contain one or more tokens. The kind and number of the tokens in a document tells you something about what is attempting to be communicated, and the order of those tokens is ignored.
# 
# To start with, let's load a document.

# In[1]:

import nltk
#nltk.download('webtext')
document = nltk.corpus.webtext.open('grail.txt').read()


# Let's see what's in this document

# In[2]:

len(document.split('\n'))


# In[3]:

document.split('\n')[0:10]


# It looks like we've gotten ourselves a bit of the script from Monty Python and the Holy Grail. Note that when we are looking at the text, part of the structure of the document is written in tokens. For example, stage directions have been placed in brackets, and the names of the person speaking are in all caps.
# 
# ## Regular expressions
# 
# If we wanted to read out all of the stage directions for analysis, or just King Arthur's lines, doing so in base python string processing will be very difficult. Instead, we are going to use regular expressions. Regular expressions are a method for string manipulation that match patterns instead of bytes.

# In[4]:

import re
snippet = "I fart in your general direction! Your mother was a hamster, and your father smelt of elderberries!"
re.search(r'mother', snippet)


# Just like with `str.find`, we can search for plain text. But `re` also gives us the option for searching for patterns of bytes - like only alphabetic characters.

# In[5]:

re.search(r'[a-z]', snippet)


# In this case, we've told re to search for the first sequence of bytes that is only composed of lowercase letters between `a` and `z`. We could get the letters at the end of each sentence by including a bang at the end of the pattern.

# In[6]:

re.search(r'[a-z]!', snippet)


# If we wanted to pull out just the stage directions from the screenplay, we might try a pattern like this:

# In[7]:

re.findall(r'[a-zA-Z]', document)[0:10]


# So that's obviously no good. There are two things happening here:
# 
# 1. `[` and `]` do not mean 'bracket'; they are special characters which mean 'any thing of this class'
# 2. we've only matched one letter each
# 
# A better regular expression, then, would wrap this in escaped brackets, and include a command saying more than one letter.
# 
# Re is flexible about how you specify numbers - you can match none, some, a range, or all repetitions of a sequence or character class.
# 
# character | meaning
# ----------|--------
# `{x}`     | exactly x repetitions
# `{x,y}`   | between x and y repetitions
# `?`       | 0 or 1 repetition
# `*`       | 0 or many repetitions
# `+`       | 1 or many repetitions

# In[8]:

re.findall(r'\[[a-zA-Z]+\]', document)[0:10]


# This is better, but it's missing that `[clop clop clop]` we saw above. This is because we told the regex engine to match any alphabetic character, but we did not specify whitespaces, commas, etc. to match these, we'll use the dot operator, which will match anything expect a newline.
# 
# Part of the power of regular expressions are their special characters. Common ones that you'll see are:
# 
# character | meaning
# ----------|--------
# `.`       | match anything except a newline
# `^`       | match the start of a line
# `$`       | match the end of a line
# `\s`      | matches any whitespace or newline
# 
# Finally, we need to fix this `+` character. It is a 'greedy' operator, which means it will match as much of the string as possible. To see why this is a problem, try:

# In[9]:

snippet = 'This is [cough cough] and example of a [really] greedy operator'
re.findall(r'\[.+\]', snippet)


# Since the operator is greedy, it is matching everything inbetween the first open and the last close bracket. To make `+` consume the least possible amount of string, we'll add a `?`.

# In[10]:

p = re.compile(r'\[.+?\]')
re.findall(p, document)[0:10]


# What if we wanted to grab all of Arthur's speech? This one is a little trickier, since:
# 
# 1. It is not conveniently bracketed; and,
# 2. We want to match on ARTHUR, but not to capture it
# 
# If we wanted to do this using base string manipulation, we would need to do something like:
# 
# ```
# split the document into lines
# create a new list of just lines that start with ARTHUR
# create a newer list with ARTHUR removed from the front of each element
# ```
# 
# Regex gives us a way of doing this in one line, by using something called groups. Groups are pieces of a pattern that can be ignored, negated, or given names for later retrieval.
# 
# character | meaning
# ----------|--------
# `(x)`     | match x
# `(?:x)`   | match x but don't capture it
# `(?P<x>)` | match something and give it name x
# `(?=x)`   | match only if string is followed by x
# `(?!x)`   | match only if string is not followed by x

# In[11]:

p = re.compile(r'(?:ARTHUR: )(.+)')
re.findall(p, document)[0:10]


# Because we are using `findall`, the regex engine is capturing and returning the normal groups, but not the non-capturing group. For complicated, multi-piece regular expressions, you may need to pull groups out separately. You can do this with names.

# In[12]:

p = re.compile(r'(?P<name>[A-Z ]+)(?::)(?P<line>.+)')
match = re.search(p, document)
match


# In[13]:

match.group('name'), match.group('line')


# #### Now let's try a small challenge!
# 
# To check that you've understood something about regular expressions, we're going to have you do a small test challenge. Partner up with the person next to you - we're going to do this as a pair coding exercise - and choose which computer you are going to use.
# 
# Then, navigate to `challenges/03_analysis/` and read through challenge A. When you think you've completed it successfully, run `py.test test_A.py` .

# ## Tokenizing
# 
# Let's grab Arthur's speech from above, and see what we can learn about Arthur from it.

# In[14]:

p = re.compile(r'(?:ARTHUR: )(.+)')
arthur = ' '.join(re.findall(p, document))
arthur[0:100]


# In our model for natural language, we're interested in words. The document is currently a continuous string of bytes, which isn't ideal. You might be tempted to separate this into words using your newfound regex knowledge:

# In[15]:

p = re.compile(r'\w+', flags=re.I)
re.findall(p, arthur)[0:10]


# But this is problematic for languages that make extensive use of punctuation. For example, see what happens with:

# In[16]:

re.findall(p, "It isn't Dav's cheesecake that I'm worried about")


# The practice of pulling apart a continuous string into units is called "tokenizing", and it creates "tokens". NLTK, the canonical library for NLP in Python, has a couple of implementations for tokenizing a string into words.

# In[17]:

from nltk import word_tokenize
word_tokenize("It isn't Dav's cheesecake that I'm worried about")


# The distinction here is subtle, but look at what happened to "isn't". It's been separated into "IS" and "N'T", which is more in keeping with the way contractions work in English.

# In[18]:

tokens = word_tokenize(arthur)
tokens[0:10]


# At this point, we can start asking questions like what are the most common words, and what words tend to occur together.

# In[19]:

len(tokens), len(set(tokens))


# So we can see right away that Arthur is using the same words a whole bunch - on average, each unique word is used four times. This is typical of natural language. 
# 
# > Not necessarily the value, but that the number of unique words in any corpus increases much more slowly than the total number of words.
# 
# > A corpus with 100M tokens, for example, probably only has 100,000 unique tokens in it.
# 
# For more complicated metrics, it's easier to use NLTK's classes and methods.

# In[20]:

from nltk import collocations
fd = collocations.FreqDist(tokens)
fd.most_common()[:10]


# In[21]:

measures = collocations.BigramAssocMeasures()
c = collocations.BigramCollocationFinder.from_words(tokens)
c.nbest(measures.pmi, 10)


# In[22]:

c.nbest(measures.likelihood_ratio, 10)


# We see here that the collocation finder is pulling out some things that have face validity. When Arthur is talking about peasants, he calls them "bloody" more often than not. However, collocations like "Brother Maynard" and "BLACK KNIGHT" are less informative to us, because we know that they are proper names.
# 
# If you were interested in collocations in particular, what step do you think you would have to take during the tokenizing process?

# ## Stemming
# 
# This has gotten us as far identical tokens, but in language processing, it is often the case that the specific form of the word is not as important as the idea to which it refers. For example, if you are trying to identify the topic of a document, counting 'running', 'runs', 'ran', and 'run' as four separate words is not useful. Reducing words to their stems is a process called stemming.
# 
# A popular stemming implementation is the Snowball Stemmer, which is based on the Porter Stemmer. It's algorithm looks at word forms and does things like drop final 's's, 'ed's, and 'ing's.
# 
# Just like the tokenizers, we first have to create a stemmer object with the language we are using.

# In[23]:

snowball = nltk.SnowballStemmer('english')


# Now, we can try stemming some words

# In[24]:

snowball.stem('running')


# In[25]:

snowball.stem('eats')


# In[26]:

snowball.stem('embarassed')


# Snowball is a very fast algorithm, but it has a lot of edge cases. In some cases, words with the same stem are reduced to two different stems.

# In[27]:

snowball.stem('cylinder'), snowball.stem('cylindrical')


# In other cases, two different words are reduced to the same stem.
# 
# > This is sometimes referred to as a 'collision'

# In[28]:

snowball.stem('vacation'), snowball.stem('vacate')


# In[29]:

snowball.stem('organization'), snowball.stem('organ')


# In[30]:

snowball.stem('iron'), snowball.stem('ironic')


# In[31]:

snowball.stem('vertical'), snowball.stem('vertices')


# A more accurate approach is to use an English word bank like WordNet to call dictionary lookups on word forms, in a process called lemmatization.

# In[32]:

# nltk.download('wordnet')
wordnet = nltk.WordNetLemmatizer()


# In[33]:

wordnet.lemmatize('iron'), wordnet.lemmatize('ironic')


# In[34]:

wordnet.lemmatize('vacation'), wordnet.lemmatize('vacate')


# Nothing comes for free, and you've probably noticed already that the lemmatizer is slower. We can see how much slower with one of IPYthon's `magic functions`.

# In[35]:

get_ipython().magic("timeit wordnet.lemmatize('table')")


# In[36]:

4.45 * 5.12


# In[37]:

get_ipython().magic("timeit snowball.stem('table')")


# #### Time for another small challenge!
# 
# Switch computers for this one, so that you are using your partner's computer, and try your hand at challenge B!

# ## Sentiment
# 
# Frequently, we are interested in text to learn something about the person who is speaking. One of these things we've talked about already - linguistic diversity. A similar metric was used a couple of years ago to settle the question of who has the [largest vocabulary in Hip Hop](http://poly-graph.co/vocabulary.html).
# 
# > Unsurprisingly, top spots go to Canibus, Aesop Rock, and the Wu Tang Clan. E-40 is also in the top 20, but mostly because he makes up a lot of words; as are OutKast, who print their lyrics with words slurred in the actual typography
# 
# Another thing we can learn is about how the speaker is feeling, with a process called sentiment analysis. Before we start, be forewarned that this is not a robust method by any stretch of the imagination. Sentiment classifiers are often trained on product reviews, which limits their ecological validity.
# 
# We're going to use TextBlob's built-in sentiment classifier, because it is super easy.

# In[38]:

from textblob import TextBlob


# In[39]:

blob = TextBlob(arthur)


# In[40]:

for sentence in blob.sentences[10:25]:
    print(sentence.sentiment.polarity, sentence)


# ## Semantic distance
# 
# Another common NLP task is to look for semantic distance between documents. This is used by search engines like Google (along with other things like PageRank) to decide which websites to show you when you search for things like 'bike' versus 'motorcycle'.
# 
# It is also used to cluster documents into topics, in a process called topic modeling. The math behind this is beyond the scope of this course, but the basic strategy is to represent each document as a one-dimensional array, where the indices correspond to integer ids of tokens in the document. Then, some measure of semantic similarity, like the cosine of the angle between unitized versions of the document vectors, is calculated.
# 
# Luckily for us there is another python library that takes care of the heavy lifting for us.

# In[41]:

from gensim import corpora, models, similarities


# We already have a document for Arthur, but let's grab the text from someone else to compare it with.

# In[42]:

p = re.compile(r'(?:GALAHAD: )(.+)')
galahad = ' '.join(re.findall(p, document))
arthur_tokens = tokens
galahad_tokens = word_tokenize(galahad)


# Now, we use gensim to create vectors from these tokenized documents:

# In[43]:

dictionary = corpora.Dictionary([arthur_tokens, galahad_tokens])
corpus = [dictionary.doc2bow(doc) for doc in [arthur_tokens, galahad_tokens]]
tfidf = models.TfidfModel(corpus, id2word=dictionary)


# Then, we create matrix models of our corpus and query

# In[44]:

query = tfidf[dictionary.doc2bow(['peasant'])]
index = similarities.MatrixSimilarity(tfidf[corpus])


# And finally, we can test our query, "peasant" on the two documents in our corpus

# In[45]:

list(enumerate(index[query]))


# So we see here that "peasant" does not match Galahad very well (a really bad match would have a negative value), and is more similar to the kind of speach output that we see from King Arthur.

# # Tabular data
# 
# In data storage, data visualization, inferential statistics, and machine learning, the most common way to pass data between applications is in the form of tables (these are called tabular, structured, or rectangular data). These are convenient in that, when used correctly, they store data in a DRY and easily queryable way, and are also easily turned into matrices for numeric processing.
# 
# > note - it is sometimes tempting to refer to N-dimensional matrices as arrays, following the numpy naming convention, but these are not the same as arrays in C++ or Java, which may cause confusion
# 
# It is common in enterprise applications to store tabular data in a SQL database. In the sciences, data is typically passed around as comma separated value files (.csv), which you have already been dealing with over the course of the last two days.
# 
# For this brief introduction to analyzing tabular data, we'll be using the [scipy stack](https://www.scipy.org/), which includes numpy, pandas, scipy, and "scikits" like sk-learn and sk-image.

# In[46]:

import pandas as pd


# You might not have seen this `as` convention yet. It is just telling python that when we import `pandas`, we don't want to access it in the namespace as `pandas` but as `pd` instead.
# 
# ## Pandas basics
# 
# We'll start by making a small table to practice on. Tables in pandas are called data frames, so we'll start by making an instance of class `DataFrame`, and initialize it with some data.
# 
# > note - pandas and R use the same name for their tables, but their behavior is often very different

# In[47]:

table = pd.DataFrame({'id': [1,2,3], 'name':['dillon','juan','andrew'], 'age':[47,27,23]})
print(table)


# Variables in pandas are represented by a pandas-specific data structure, called a `Series`. You can grab a `Series` out of a `DataFrame` by using the slicing operator with the name of the variable that you want to pull.

# In[48]:

table['name'], type(table['name'])


# We could have made each variable a `Series`, and then put it into the DataFrame object, but it's easier in this instance to pass in a dictionary where the keys are variable names and the values are lists. You can also modify a data frame in place using similar syntax:

# In[49]:

table['fingers'] = [9, 10, None]


# If you try to run that code without the `None` there, pandas will return an error. In a table (in any language) each column must have the same number of rows.
# 
# We've entered `None`, base python's missingness indicator, but pandas is going to swap this out with something else: 

# In[50]:

table['fingers']


# You might be tempted to write your own control structures around these missing values (which are variably called `NaN`, `nan`, and `NA`), but this is always a bad idea:

# In[51]:

table['fingers'][2] == None


# In[52]:

table['fingers'][2] == 'NaN'


# In[53]:

type(table['fingers'][2]) == str


# None of this works because the pandas `NaN` is a subclass of numpy's double precision floating point number. However, for ambiguous reasons, even numpy.nan does not evaluate as being equal to itself.
# 
# To handle missing data, you'll need to use the pandas method `isnull`.

# In[54]:

pd.isnull(table['fingers'])


# In the same way that we've been pulling out columns by name, you can pull out rows by index. If I want to grab the first row, I can use: 

# In[55]:

table[:1]


# Recall that indices in python start at zero, and that selecting by a range does not include the final value (i.e. `[ , )`).
# 
# Unlike other software languages (R, I'm looking at you here), row indices in pandas are immutable. So, if I rearrange my data, the index also get shuffled.

# In[56]:

table.sort_values('age')


# Because of this, it's common to set the index to be something like a timestamp or UUID.
# 
# We can select parts of a `DataFrame` with conditional statements:

# In[57]:

table[table['age'] < 40]


# ## Merging tables
# 
# As you might expect, tables in pandas can also be merged by keys. So, if we make a new dataset that shares an attribute in common:

# In[58]:

other_table = pd.DataFrame({
        'name':['dav', 'juan', 'dillon'], 
        'languages':['python','python','python']})


# In[59]:

table.merge(other_table, on='name')


# Note that we have done an "inner join" here, which means we are only getting the intersection of the two tables. If we want the union, we can specify that we want an outer join:

# In[60]:

table.merge(other_table, on='name', how='outer')


# Or maybe we want all of the data from `table`, but not `other_table`

# In[61]:

table.merge(other_table, on='name', how='left')


# ## Reshaping
# 
# To make analysis easier, you may have to reshape your data. It's easiest to deal with data when each table meets the follwing criteria:
# 
# 1. Each row is exactly one observation
# 2. Each column is exactly one kind of data
# 3. The table expresses one and only one relationship between observations and variables
# 
# This kind of format is easy to work with, because:
# 
# 1. It's easy to update when every piece of data exists in one and only one place
# 2. It's easy to subset conditionally across rows
# 3. It's easy to test across columns
# 
# To make this more concrete, let's take an example table.
# 
# name   | city1 | city2 | population
# -------|-------|-------|-----------
# dillon | williamsburg | berkeley | 110
# juan   | berkeley | berkeley | 110
# dav    | cambridge | berkeley | 110
# 
# This table violates all three of the rules above. Specifically, it:
# 
# 1. each row is about two observations
# 2. two columns are about the same kind of date (city), while another datatype (time) has been hidden in the column names
# 3. it expresses the relationship between people and where they live; and, cities and their population
# 
# In this particular example, our data is too wide. If we create that dataframe in pandas

# In[62]:

wide_table = pd.DataFrame({'name' : ['dillon', 'juan', 'dav'],
                           'city1' : ['williamsburg', 'berkeley', 'cambridge'],
                           'city2' : ['berkeley', 'berkeley', 'berkeley'],
                           'population' : [110, 110, 110]
                          })
wide_table


# We can make this longer in pandas using the `melt` function

# In[63]:

long_table = pd.melt(wide_table, id_vars = ['name'])
long_table


# We can make the table wider using the pivot method
# 
# > side note - this kind of inconsistency between `melt` and `pivot` is un-pythonic and should not be emulated

# In[64]:

long_table.pivot(columns='variable')


# **WHOA**
# 
# One of the really cool things about pandas is that it allows you to have multiple indexes for rows and columns. Since pandas couldn't figure out what do with two kinds of value variables, it doubled up our column index. We can fix this by specifying that we only want the 'values' values

# In[65]:

long_table.pivot(columns='variable', values='value')


# #### Challenge time!
# 
# Switch computers *again* so that you are working on the first computer of the day, and have a look at challenge C. This will have you practice reading and merging tables. Again, when you are finished, check your work by running `py.test test_C` in a shell.

# ## Descriptive statistics
# 
# Single descriptives have their own method calls in the `Series` class.

# In[66]:

table['fingers'].mean()


# In[67]:

table['fingers'].std()


# In[68]:

table['fingers'].quantile(.25)


# In[69]:

table['fingers'].kurtosis()


# You can call several of these at once with the `describe` method

# In[70]:

table.describe()


# ## Inferential statistics
# 
# pandas does not have statistical functions baked in, so we are going to call them from the `scipy.stats` library.
# 
# We are also going to load in an actual dataset, as stats examples aren't very interesting with tiny bits of fake data.

# In[71]:

from scipy import stats
data = pd.read_csv('../data/03_feedback.csv')


# Using what you've learned so far about manipulating pandas objects, how would you find out the names of the variables in this dataset? Their datatypes? The distribution of their values?

# ### Comparisons of group means
# 
# A common statistical procedure is to look for differences between groups of values. Typically, the values are grouped by a variable of interest, like sex or age. Here, we are going to compare the barriers of access to technology that people experience in the D-Lab compared to the world outside.
# 
# If you only have two groups in your sample, you can use a t-test:

# In[72]:

i = data['inside.barriers'].dropna()
o = data['outside.barriers'].dropna()
stats.ttest_ind(i, o)


# Notice that here, we are passing in two whole columns, but we could also be subsetting by some other factor.
# 
# If you have more than two groups (or levels) that you would like to compare, you'll have to use something like an ANOVA:

# In[73]:

m = data[data.gender == "Male/Man"]['outside.barriers'].dropna()
f = data[data.gender == "Female/Woman"]['outside.barriers'].dropna()
q = data[data.gender == "Genderqueer/Gender non-conforming"]['outside.barriers'].dropna()
stats.f_oneway(m, f, q)


# #### Linear relationships
# 
# Another common task is to establish if/how two variables are related across linear space. This could be something, for example, like relating shoe size to height. Here, we are going to ask whether barriers to access to technology inside and outside of the D-Lab are related.
# 
# One implementation of linear relationships is correlation testing:

# In[74]:

intermediate = data.dropna(subset=['inside.barriers', 'outside.barriers'])
stats.pearsonr(intermediate['outside.barriers'], intermediate['inside.barriers'])


# Another implementation is to use a linear regression to predict the levels of one variable based on the levels of another. Here, we are predicting the barriers in the D-Lab based on what we know about barriers outside:

# In[75]:

stats.linregress(intermediate['outside.barriers'], intermediate['inside.barriers'])


# You'll notice that we haven't done a whole lot of statistical analyses yet. For more robust tests and more kinds of tests, you can look through the algorithms in scipy's machine learning library, [scikit-learn](http://scikit-learn.org/stable/). Another option, according to Scipy's own documentation, is to switch to R:
# 
# > For many more stat related functions install the software R and the interface package rpy

# # Practice
# 
# In the time remaining, pull up a dataset that you have, and that you'd like to work with in Python. The instructors will be around to help you apply what you've learned today to problems in your data that you are dealing with.
# 
# If you don't have data of your own, you should practice with the test data we've given you here. For example, you could try to figure out:
# 
# 1. Is King Arthur happier than Sir Robin, based on his speech?
# 2. Which character in Monty Python has the biggest vocabulary?
# 3. Do different departments have the same gender ratios?
# 4. What variable in this dataset is the best predictor for how useful people find our workshops to be?

# In[76]:



