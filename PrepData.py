import nltk

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
NLTK Notes 

Notes from University of Michigan "Applied Text Mining" in Python course.

~~~~~~~~~~~~~~ I HIGHLY recommend U of Michigan's python courses!!! ~~~~~~~~~~~~~~~~~
"""
# download corpora
nltk.download()

from nltk.book import *

#~~~~~~~~~~~~~~~~~~Basics of NLTK~~~~~~~~~~~~~~~~~~~~#
text7   # wallstreet journal article
sents() # shows you individual sentences.
sent7   # sentence 7 in text7

# Create a dictionary with words and # of occurrences
dist = FreqDist(text7)
vocab_words = dist.keys()
number_of_times_president_occurs = dist[u'President'] # must add unicode indicator

# get list of commonly used words that are longer than 4 chars.
freqwords = [w for w in vocab_words if len(w) >= 4 and dist[w] > 100]

#~~~~~~~~~~~NORMALIZATION AND STEMMING~~~~~~~~~~~~~~~~~#
separate_words = text7.lower().split()
porter = nltk.PorterStemmer()

# Using Lemmatization is like porter stemmer, but makes words only valid words.

# gets universal declaration of human rights.
udhr = nltk.corpus.udhr.words('English-Latin1')

### Lemmatization ###
# gets rid of plurals, but remains pretty similar.
# should probably make lower before lemmatizing because will not changes.
WNlemma = nltk.WordNetLemmatizer
lemmatized = [WNlemma.lemmatize(t) for t in udhr]

### word_tokenize() ####
# splits up tokens in a more useful way. Example: makes "shouldn't" into separate ("should", "n't")
# also makes "." separate
nltk.word_tokenize(text7)

### sent_tokenize() ###
# NLTK builtin sentence separator
sentences = nltk.sent_tokenize(text7)

#~~~~~~~~~~Part of Speech Tagging~~~~~~~~~~#

# get help with tags in jupyter
nltk.help.upenn_tagset('MD') # parameter is the tag. Modal in this example.

# The following returns list of tuples with (words, part of speech tag)
words_and_pos = nltk.pos_tag(text7)

# skipped section on speech parsing in Advanced NLP tasks because unnecessary for current projects.

