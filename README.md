# Sentiment-Analysis

Sentiment Analysis on Twitter Data. This is a repository for the assignment given by The Code Work.

**Dataset Link** - https://www.kaggle.com/arkhoshghalb/twitter-sentiment-analysis-hatred-speech

### Modelling Steps : 
1. Data Cleaning, Preprocessing and Exploratory Data Analysis
2. Fitting Machine Learning and Deep Learning models on given dataset.
3. Evaluating and comparing model performance
4. Deploying best fit model to a Flask App.

### Following Machine Learning models were tested: 

1. Naive Bayes' Classifier
2. Linear Support Vector Machines Classifier
3. 1-Dimensional Convolutional Neural Network 





# Usage

### Directories
1. code - You can find all the jupyter notebooks here.
2. models - Saved trained models and their preprocessing tokenizers, vectorizers, etc.
3. app - This contains a dummy flask application in which the sentiment analysis model is deployed

### Web Application 
The best fit trained model is deployed as a flask web application. A user can enter any tweet and the application will respond whether the tweet is having a positive or a negative sentiment.

To Run the web application 
1. Navigate to `/app`
2. Run the flask application using `python app.py` or `flask run`


