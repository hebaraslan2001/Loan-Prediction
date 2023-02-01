# -*- coding: utf-8 -*-
"""Copy of LoanPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n8kX-qOf2tHtAiG4SdjySku2c59okHjm

Installing Libraries
"""

!pip install pandas

!pip install numpy

!pip install scikit-learn



!pip install seaborn

"""Importing The Dependencies"""

import numpy as np
import pandas as pd 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

"""Data Collection And Processing"""

#laoding the dataSet to pandas dataFrame 
loan_dataset=pd.read_csv('loan_data.csv')

type(loan_dataset)  #type of the data

loan_dataset.head()

loan_dataset.shape

loan_dataset.describe()

#number of missing values in each column
loan_dataset.isnull().sum()

#for numerical terms -- mean
loan_dataset['LoanAmount'] = loan_dataset['LoanAmount'].fillna(loan_dataset['LoanAmount'].mean())
loan_dataset['Credit_History'] = loan_dataset['Credit_History'].fillna(loan_dataset['Credit_History'].mean())
loan_dataset['Loan_Amount_Term'] = loan_dataset['Loan_Amount_Term'].fillna(loan_dataset['Loan_Amount_Term'].mean())
loan_dataset['Gender'] = loan_dataset['Gender'].fillna(loan_dataset['Gender'].mode()[0])
loan_dataset['Married'] = loan_dataset['Married'].fillna(loan_dataset['Married'].mode()[0])
loan_dataset['Dependents'] = loan_dataset['Dependents'].fillna(loan_dataset['Dependents'].mode()[0])
loan_dataset['Self_Employed'] = loan_dataset['Self_Employed'].fillna(loan_dataset['Self_Employed'].mode()[0])

loan_dataset.info()

loan_dataset.isnull().sum()

loan_dataset.shape

loan_dataset.replace({"Loan_Status":{'N':0,'Y':1}},inplace=True)

loan_dataset.head()

loan_dataset['Dependents'].value_counts()

loan_dataset=loan_dataset.replace(to_replace='3+', value =4)



loan_dataset['Dependents'].value_counts()

#education correlation with loan status
sns.countplot(x='Education',hue='Loan_Status',data=loan_dataset)

sns.countplot(x='Married',hue='Loan_Status',data=loan_dataset)

sns.countplot(x='Credit_History',hue='Loan_Status',data=loan_dataset)

loan_dataset.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1}, 
                      'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)

loan_dataset.head()

# separating the data and label 
X=loan_dataset.drop(columns=['Loan_ID','Loan_Status'],axis=1)
Y=loan_dataset['Loan_Status']

X = pd.get_dummies(X , drop_first= True)

#thismodel = LinearRegression()
#sel = SelectFromModel(estimator= thismodel)
#sel.fit(X , Y)
#X = sel.transform(X)
#X.shape

#print(X)
#print(Y)

"""TRAIN TEST SPLIT"""

X_train ,X_test,Y_train ,Y_test=train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

"""Starting Logistic regression"""

model = LogisticRegression()
model.fit(X_train,Y_train)
#accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train) 
print('Accuracy on training data : ', training_data_accuracy)

lr_prediction = model.predict(X_test)
print('Logistic Regression accuracy = ' , metrics.accuracy_score(lr_prediction , Y_test))

"""Starting SVM"""

classifier=svm.SVC(kernel='linear')

classifier.fit(X_train,Y_train)

X_train_prediction=classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)

print('train SVM accuracy = ' , training_data_accuracy)

X_test_prediction = classifier.predict(X_test)
test_data_prediction = accuracy_score(X_test_prediction , Y_test)

print('test SVM accuracy = ' , test_data_prediction)

"""Starting DecisionTreeClassifier"""

dt = DecisionTreeClassifier(max_depth = 3 , random_state = 33)
dt.fit(X_train,Y_train)
print ('Decision tree model classifier train accuracy :',dt.score(X_train,Y_train))

print ('Decision tree model classifier test accuracy :',dt.score(X_test,Y_test))

#plt.figure(figsize = (20,10))
#plot_tree(dt,filled=True)

# "Random Forest is a classifier that contains a number of decision trees on various subsets of the given dataset and takes the average to improve the predictive accuracy of that dataset." 
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=20, random_state=33)
rfc.fit(X_train, Y_train)
print('random forest model accuracy for training set :' ,rfc.score(X_train,Y_train))

print('random forest model accuracy for testing set :' ,rfc.score(X_test,Y_test))



#scaling
#fig,ax = plt.subplots(figsize=(12,4))
scaler = StandardScaler()
X_train= scaler.fit_transform(X_train) 
X_test =scaler.fit_transform(X_test)

knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train,Y_train)

print('KNN model accuracy for testing set : ',knn.score(X_test,Y_test))

X_new = X_test[0]
input_data_as_numpy_array = np.asarray(X_new)

# reshape the np array as we are predicting for one instance
#input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
#prediction = model.predict(input_data_reshaped)
#print(prediction)

#if (prediction[0]==0)
 # print('The user cannot take loan')
#else
 # print('The user can take loan')

#print(Y_test)
#Y_test.head()

