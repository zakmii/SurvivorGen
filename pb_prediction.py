# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FImNVBt-ijj2bfpgMWZQpmQvnqyTyX1Y
"""

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.cluster import KMeans
import warnings
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# reading the training and testing data
train_data = pd.read_csv('DATASET.csv')

train_data

X = train_data[["age", "timerecurrence", "chemo", "hormonal", "amputation", "histtype"]].astype(float)
y = train_data["survival"].astype(float)

# removing outliers using LOF algorithm
lof = LocalOutlierFactor(n_neighbors=40, contamination=0.01,metric = "euclidean")
y_pred = lof.fit_predict(X)
outliers = X[y_pred == -1]

# removing outliers from the training data
X = X[y_pred != -1]
y = y[y_pred != -1]

warnings.filterwarnings("ignore")

X_train = train_data.iloc[:, 1:-1]
y_train = train_data.iloc[:, -1]
X_test = train_data.iloc[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
best_params_list = []

X_train = pd.DataFrame(X_train)
X_test = pd.DataFrame(X_test)

lr1 = DecisionTreeRegressor(max_depth=3)

lr1.fit(X_train, y_train)
pred1 = lr1.predict(X_test)
print("Validation Accuracy: ", lr1.score(X_test, y_test))

# Create the decision tree regressor
regressor = DecisionTreeRegressor()

# Fit the regressor to the training data
regressor.fit(X_train, y_train)

age = input("Enter age ")
timerecurrence = input("Enter timerecurrence ")
chemo = input("Enter chemo ")
hormonal = input("Enter hormonal ")
amputation = input("Enter amputation ")
histtype = input("Enter histtype ")

# Make a prediction using the custom input values
prediction = regressor.predict([[age, timerecurrence, chemo, hormonal, amputation, histtype]])

# Print the prediction
print('The predicted survivability rate is {}%'.format(prediction[0]))