# -*- coding: utf-8 -*-
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
import pickle
from random import random

dt = pd.read_csv("../files/train_finalized.csv")


for i in range(len(dt[dt['y'] == 0]) - len(dt[dt['y'] == 1])):
    row_num = int(random() * len(dt))
    while (dt.iloc[row_num]['y'] == 1):
        row_num = int(random() * len(dt))
    dt = dt.drop(dt.index[[row_num]])

dt.to_csv("../files/train_50x50.csv", index=False)


dt = pd.read_csv("../files/train_50x50.csv")    

X = dt.drop('y',axis=1)
y = dt['y']

X_train, X_test, y_train, y_test = train_test_split(X, y)


scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


mlp = MLPClassifier(hidden_layer_sizes=(7, 7,), max_iter=1000)
mlp.fit(X_train,y_train)

predictions = mlp.predict(X_test)

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))


filename = '../files/ann_model_50x50.sav'
pickle.dump(mlp, open(filename, 'wb'))

"""
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict(X_test)

print(confusion_matrix(y_test,result))
print(classification_report(y_test,result))
"""