import pandas as pd
import numpy as np

df = pd.read_csv('Amazon_Unlocked_Mobile.csv')
df.head

# Drop columns with empty values
df.dropna(inplace=True)
# Remove neutral ratings
df = df[df['Rating'] != 3]
# Create new column where positive rating are encoded with 1s.
# np.where() is kind of like a findReplace method. 
# For all values, replace with either this or this based on Bool. 
df['PositiveReviews'] = np.where(df['Rating'] > 3, 1, 0)

df['PositiveReviews'].mean()

from sklearn.model_selection import train_test_split
# Split up our data. x = String Reviews y = binary value for pos/neg
x_train, x_test, y_train, y_test = train_test_split(df['Reviews'],
                                                   df['PositiveReviews'],
                                                     random_state = 0)

# Use bag of word approach. Ignore structure.
# Added option to remove stop words 
from sklearn.feature_extraction.text import TfidfVectorizer

vec = TfidfVectorizer(min_df=10, stop_words='english', ngram_range=(1,2)).fit(x_train)

len(vec.get_feature_names())


# Gives us the bag of words representation of x_train
# Each row corresponds to a document and each column is a word from training vocab.
x_train_vectorized = vec.transform(x_train)


# Experimenting with a naive bayes implementation of the model demonstrated
# in the U of Michigan's Applied Data Mining in Python Course. 
# Notes on naive classifier 

from sklearn import naive_bayes
from sklearn.metrics import f1_score

model = naive_bayes.MultinomialNB()
model.fit(x_train_vectorized, y_train)
predicted_labels = model.predict(vec.transform(x_test))
# What does f1 mean? What kind of averaging can you do?
print(f1_score(y_test, predicted_labels, average = 'micro'))

# The Accuracy is .9137 w/out bigrams 
# Accuracy is .937 w/ bigrams. Logistic Regression wins again. 

# Look at coefficients from the model

feature_names = np.array(vec.get_feature_names())
# Sort the coefficients to make it easy to figure out high and low
sorted_coef_index = model.coef_[0].argsort()

print("Smallest Coefficients:\n{}\n".format(feature_names[sorted_coef_index[:10]]))
print("Largest Coefficients:\n{}\n".format(feature_names[sorted_coef_index[:-11:-1]]))
