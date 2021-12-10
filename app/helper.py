'''
This file contains the helper functions needed for the twitter sentiment analysis model
for preprocessing of data and predictions
'''
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import pickle
import re
import nltk

nltk.download('punkt')
nltk.download('wordnet')

# Initialising the vectorizer and sentiment analysis model

with open('../models/count_vectorizer.pkl', 'rb') as vf:
    vectorizer = pickle.load(vf)

with open('../models/tfidf_transformer.pkl', 'rb') as tf:
    transformer = pickle.load(tf)

with open('../models/svm.pkl', 'rb') as f:
    model = pickle.load(f)

lemmatizer = WordNetLemmatizer()


def preprocess_tweet(tweet):

    # removing website links or emails
    tweet = re.sub(r'\S+(.com)', '', tweet)

    # removing other non-alphabetical characters
    tweet = re.sub(r'[^A-Za-z ]+', '', tweet)

    tweet_words = word_tokenize(tweet)
    cleaned_tweet = ''
    for word in tweet_words:
        cleaned_tweet += ' ' + lemmatizer.lemmatize(word)
    return cleaned_tweet


def predict(x):
    y = model.predict([x])
    print(y)
    return
