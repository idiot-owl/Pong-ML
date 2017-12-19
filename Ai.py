from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pickle

regr = linear_model.LinearRegression()
trainX = []
trainY = []
with open('trainX.pkl', 'rb') as f:
    trainX = pickle.load(f)
with open('trainY.pkl', 'rb') as f:
    trainY = pickle.load(f)
tx = np.array(trainX)
regr.fit(tx, np.array(trainY))
print(regr.coef_)
