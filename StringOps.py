"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Helpful String operations in python for NLP and other things with python and pandas.

Notes from University of Michigan "Applied Text Mining" in Python course.

~~~~~~~~~~~~~~ I HIGHLY recommend U of Michigan's python courses!!! ~~~~~~~~~~~~~~~~~
"""

# clean up this screwed up text by stripping and joining it w/ spaces.
text = "    The dog is   cool I think."
change = text.strip()
cleaned = change.join(' ')

# convert string to char list.
char_list = list(cleaned)

# get unique characters.
# must make chars lowercase first
new_list = []
for x in char_list:
    new_list.append(x.lower())
unique_chars = set(new_list)

# Demo how to deal with multi-line string.
multiline_text = "I want to be a dog\nbecause dogs are the coolest.\nIf I was a dog I'd be happy."
# convert string to list of lines
convert_to_list = multiline_text.splitlines()

# FILE OPERATIONS

# Reading text files.
f = open('text.txt', 'r')
# the following will include \n at ends of lines.
f.readline() # read only the first line. So we could loop and read as much as we want.
f.seek(0)    # If we've already opened we use seek() to reset pointer to beginning of file.
entire_file = f.read()     # read the entire file. Can pass integer to say read(n) n characters
file_with_separate_lines = entire_file.splitlines()

# Use rstrip() to get rid of \n or \r.


"""
PANDAS Text Mining EXAMPLES!!!!!!!!!!
"""
import pandas as pd

time_sentences = ["Monday: The doctor's appointment is as 2:45 pm.",
                  "Tuesday: The dentist's appointment is at 11:30 am.",
                  "Wednesday: At 7:00 pm, there is a basketball game.",
                  "Thursday: Be back home by 11:15 pm at the latest."]

# Create a series.
df = pd.DataFrame(time_sentences, columns = ['text'])
# find the length of each line in column.
df['text'].str.len()
# see which of the iterms contain the word 'appointment'
# returns Boolean
df['text'].str.contains('appointment')
# count how many occurences of a pattern occur in series.
df['text'].str.count(r'\d')
# find out what the matches were.
df['text'].str.findall(r'\d')
# find all the times in entries
df['text'].str.findall(r'(\d?\d):(\d\d)')
# replace each week day with ? marks
df['text'].str.replace(r'\w+day\b', '???')
# Replace full day names with the first 3 letters of their name (e.g. Monday -> Mon)
# groups() gets tuple of the groups.
df['text'].str.replace(r'(\w+day\b)', lambda x: x.groups()[0][:3])
# the following extracts groups, one for the hours and one for the minutes. Only does for first match of pattern
# Creates dataframe with columns for hours and column for minutes.
df['text'].str.extract(r'(\d?\d):(\d\d)')
# the following extracts all. So more columns.
# returns columns: 2:45pm, 2, 45, pm
df['text'].str.extractall(r'((\d?\d):(\d\d) ?([ap]m))')
# The following adds column names to the previous operation. AWESOME!!
df['text'].str.extractall(r'(?P<time>(?<hour>\d?\d):(?P<minute>\d\d) ?(?<period>[ap]m))')
