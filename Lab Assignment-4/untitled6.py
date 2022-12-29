# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vbNwotiu9qcOBv_yOA3U1CLt8RMsD8Bh
"""

import pandas as pd
import numpy as np
import sklearn


volunteer = pd.read_csv('/content/breast cancer classification dataset.csv')
volunteer.head(6)

volunteer.shape

volunteer.isnull().sum()

from sklearn.impute import SimpleImputer

impute = SimpleImputer(missing_values=np.nan, strategy='mean')

impute.fit(volunteer[['radius_mean']])

volunteer['radius_mean'] = impute.transform(volunteer[['radius_mean']])


impute.fit(volunteer[['fractal_dimension_worst']])

volunteer['fractal_dimension_worst'] = impute.transform(volunteer[['fractal_dimension_worst']])

volunteer.isnull().sum()

volunteer.info()

volunteer['diagnosis'].unique()

from sklearn.preprocessing import LabelEncoder

# diagnosis
enc = LabelEncoder()
volunteer['diagnosis'] = enc.fit_transform(volunteer['diagnosis'])
print(volunteer[['diagnosis']].head(23))

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

scaler.fit(volunteer)

scaled = scaler.transform(volunteer)

print("per-feature minimum before scaling:\n {}".format(volunteer.min(axis=0)))
print("per-feature maximum before scaling:\n {}".format(volunteer.max(axis=0)))

print("per-feature minimum after scaling:\n {}".format(scaled.min(axis=0)))
print("per-feature maximum after scaling:\n {}".format(scaled.max(axis=0)))

corr = volunteer.corr()
corr

import seaborn as sns

sns.heatmap(corr, cmap = 'YlGnBu')

feature = volunteer [['radius_mean', 'perimeter_mean', 'area_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'radius_se', 'perimeter_se', 'area_se', 'compactness_se', 'concavity_se', 'concave points_se', 
       'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']]
label = volunteer['diagnosis']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(feature, label, test_size = 0.2, random_state=0)

print(X_train.shape)
print(X_test.shape)

from sklearn.neighbors import KNeighborsClassifier

knn=KNeighborsClassifier()

knn.fit(X_train, y_train)

print("Test set accuracy: {:.2f}".format(knn.score(X_test, y_test)))

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)

print("per-feature minimum before scaling:\n {}".format(X_train.min(axis=0)))
print("per-feature maximum before scaling:\n {}".format(X_train.max(axis=0)))

print("per-feature minimum after scaling:\n {}".format(X_train_scaled.min(axis=0)))
print("per-feature maximum after scaling:\n {}".format(X_train_scaled.max(axis=0)))

X_test_scaled = scaler.transform(X_test)

knn.fit(X_train_scaled, y_train)

# scoring on the scaled test set
print("Scaled test set accuracy: {:.2f}".format(
    knn.score(X_test_scaled, y_test)))