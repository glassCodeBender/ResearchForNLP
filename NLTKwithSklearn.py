# Saving some code that shows how to use Sci-kit learn with NLTK


from nltk import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# In this example, there are no parameters we need to pass.
classifierNB = SklearnClassifier(MultinomialNB()).train(train_set)

# In this example we need to pass a parameter to the classifier 
classifierSVM = SklearnClassifier(SVC(), kernel='linear').train(train_set)

modelLog = SklearnClassifier(LogisticRegression()).train(train_set)
