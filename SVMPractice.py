"""
A Sample Support Vector Machine 
This model should not be used for large datasets, but it should be perfect for my Scala program. 

Even though this model sucks for the dataset I used it for, I'm saving the code because it 
shows how to remove stop_words and I like the code for the LemmaTokenizer (taking from sklearn web-site)
"""

import pandas as pd
import numpy as np

from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

# This can be used w/ CountVectorizer, but it wouldn't work with TfidfVectorizer
class LemmaTokenizer(object):
    def __init__(self):
        self.wnl = WordNetLemmatizer
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]

df = pd.read_csv('Amazon_Unlocked_Mobile.csv')
df.head


# Drop columns with empty values
df.dropna(inplace=True)

# Remove neutral ratings
df = df[df['Rating'] != 3]

# Create new column where positive rating are encoded with 1s.
# np.where() is kind of like a findReplace method. 
# For all values, replace with either this or this based on Bool. 
df['PositiveReviews'] = np.where(df['Rating'] > 3, 1, -1)


df['PositiveReviews'].mean()

from sklearn.model_selection import train_test_split
# Split up our data. x = String Reviews y = binary value for pos/neg
x_train, x_test, y_train, y_test = train_test_split(df['Reviews'],
                                                   df['PositiveReviews'],
                                                     random_state = 0)

# Use bag of word approach. Ignore structure.
# Added option to remove stop words 
from sklearn.feature_extraction.text import TfidfVectorizer

vec = TfidfVectorizer(min_df=5, stop_words='english').fit(x_train)

print(len(vec.get_feature_names()))

# Gives us the bag of words representation of x_train
# Each row corresponds to a document and each column is a word from training vocab.
x_train_vectorized = vec.transform(x_train)

# This model takes an extremely long time to fit. 
from sklearn import svm
model = svm.SVC(kernel='linear', C=0.1)
model.fit(x_train_vectorized, y_train)

from sklearn.metrics import roc_auc_score

predicted_labels = model.predict(vec.transform(x_test))
print('AUC: ', roc_auc_score(y_test, predicted_labels))

# Look at coefficients from the model

feature_names = np.array(vec.get_feature_names())
# Sort the coefficients to make it easy to figure out high and low
sorted_coef_index = model.coef_[0].argsort()

print("Smallest Coefficients:\n{}\n".format(feature_names[sorted_coef_index[:10]]))
print("Largest Coefficients:\n{}\n".format(feature_names[sorted_coef_index[:-11:-1]]))
