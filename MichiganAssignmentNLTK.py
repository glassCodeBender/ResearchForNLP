
"""
Assignment 2 for "Applied Text Mining in Python" from University of Michigan on Coursera 
Part 1 - Analyzing Moby Dick
"""

import nltk

# If you would like to work with the raw text you can use 'moby_raw'
with open('moby.txt', 'r') as f:
    moby_raw = f.read()

# If you would like to work with the novel in nltk.Text format you can use 'text1'
moby_tokens = nltk.word_tokenize(moby_raw)
text1 = nltk.Text(moby_tokens)

"""
Example 1
How many tokens (words and punctuation symbols) are in text1?
"""
def totalTokens():
    return len(nltk.word_tokenize(moby_raw))  # or alternatively len(text1)

totalTokens()

"""
Example 2
How many unique tokens (unique words and punctuation) does text1 have?
This function should return an integer.

"""
def uniqTokens():
    return len(set(nltk.word_tokenize(moby_raw)))  # or alternatively len(set(text1))

uniqTokens()

"""
Example 3
After lemmatizing the verbs, how many unique tokens does text1 have?
This function should return an integer.
"""
from nltk.stem import WordNetLemmatizer

def uniqLem():

    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(w,'v') for w in text1]

    return len(set(lemmatized))

uniqLem()

"""
Question 1¶
What is the lexical diversity of the given text input? (i.e. ratio of unique tokens to the total number of tokens)
"""

def lexDiversity():
    result = uniqTokens() / totalTokens()

    return result

lexDiversity()

"""
Question 2
What percentage of tokens is 'whale'or 'Whale'?
"""
from nltk import FreqDist
def whalePercent():
    freq = FreqDist(moby_tokens)
    keys = freq.keys()
    count = len(keys)
    whale = freq[u'whale']
    whaleUpper = freq[u'Whale']
    totalWhale = whale + whaleUpper
    result = (totalWhale / count)
    return result

whalePercent()

"""
Question 3
What are the 20 most frequently occurring (unique) tokens in the text? What is their frequency?
"""


def top20Freq():
    dictionary = {}
    freq = FreqDist(moby_tokens)

    return freq.most_common(20)

top20Freq()

"""
Question 4
What tokens have a length of greater than 5 and frequency of more than 150?
"""

def significantTokens():
    freq = FreqDist(moby_tokens)
    keys = freq.keys()
    result = [x for x in keys if len(x) > 5 and freq[x] > 150]

    return result

significantTokens()

"""
Question 5
Find the longest word in text1 and that word's length.
"""
import operator
def longestWord():
    tokens = moby_tokens
    wordDict = dict()
    for x in tokens:
        item = {len(x):x}
        wordDict.update(item)
    desc_sort = sorted(wordDict.items(), key=operator.itemgetter(0), reverse = True)

    return desc_sort[0]

longestWord()

"""
Question 6
What unique words have a frequency of more than 2000? What is their frequency?
"""
def findPseudoStopWords():
    freq = FreqDist(moby_tokens)
    keys = freq.keys()
    findIt = [x for x in keys if x.isalpha() and freq[x] > 2000]
    freqDict = dict()
    for x in findIt:
        value = {freq[x]: x}
        freqDict.update(value)

    return freqDict

findPseudoStopWords()

"""
Question 7
What is the average number of tokens per sentence?
"""
def avgWordsPerSent():
    sentences = nltk.sent_tokenize(moby_raw)
    sentCount = len(sentences)
    counts = []
    total = 0
    for x in sentences:
        words = nltk.word_tokenize(x)
        counts.append(len(words))
    for x in counts:
        total += x
    total_counts = total / len(counts)

    return total_counts

avgWordsPerSent()

"""
Question 8
What are the 5 most frequent parts of speech in this text? What is their frequency?
"""
from itertools import groupby

def answer_eight():
    words_pos = nltk.pos_tag(text1)
    tags = []
    for x, y in words_pos:
        tags.append(y)
    sorted_tags = sorted(tags, reverse=True)
    freqs = [(len(list(g)), k) for k, g in groupby(sorted_tags)]
    result = freqs[:5]

    return result

answer_eight()
