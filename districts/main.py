# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 10:39:44 2022
@author: 91790
"""
#Knowledge-driven feature engineering to detect multiple symptoms using ambulatory blood
# pressure monitoring data
import pandas as pd
import sklearn.metrics as metrics
#Load Ambulatory Blood Pressure Monitoring data
dataset=pd.read_csv('ABPM2.csv')
print("=====================================================")
print("Ambulatory Blood Pressure Monitoring (ABPM) Dataset")
print("=====================================================\n",dataset)
#Knowledge driven features
cols = ['BPS_24','BPD_24','BPS_Day24', 'BPD_Day24', 'BPS_Night24', 'BPD_Night24',
'BPS_load_Day', 'BPS_load_Night','Max_Sys']
print("==============================")
print("Knowledge-driven Feature")
print("==============================")
print(dataset[cols])
39
# rule set
def KDrule1(dataset,col1,col2):

 v1=dataset[col1]
 v2=dataset[col2]
 val=[]
 for i in range(len(v1)):
    if (v1[i] < 120 and v2[i] < 80):
        val.append("Optimal")
    elif (v1[i] >=120 and v1[i] <=129):
        val.append("Normal")
    elif (v1[i] >=130 and v1[i] <=139):
        val.append("High_Normal")
    elif (v1[i] >=140 and v1[i] <=159):
        val.append("Grade_1")
    elif (v1[i] >=160 and v1[i] <=179):
        val.append("Grade_2")
    else:
        val.append("Grade_3")
 return val
# rule set
def KDrule2(dataset,col1,col2,g):

 v1=dataset[col1] # Max_Sys
 v2=dataset[col2] # BPS_load_Day or # BPS_load_Night
 val=[]
 for i in range(len(v1)):
    if (v1[i] < 140):
        val.append("Normal")
    elif (v2[i] < g) and (v1[i] >=140 and v1[i] <=159):
        val.append("Grade_1")
    elif (v2[i] < g) and (v1[i] >=160 and v1[i] <=179):
        val.append("Grade_2")
    else:
        val.append("Grade_3")

 return val
# KD feature rules
val1=KDrule1(dataset,'BPS_24','BPD_24')
dataset['BPS_24']=val1
dataset['BPD_24']=val1
40
val2=KDrule1(dataset,'BPS_Day24','BPD_Day24')
dataset['BPS_Day24']=val2
dataset['BPD_Day24']=val2
val3=KDrule1(dataset,'BPS_Night24','BPD_Night24')
dataset['BPS_Night24']=val3
dataset['BPD_Night24']=val3
val4=KDrule2(dataset,'Max_Sys','BPS_load_Day',15)
dataset['BPS_load_Day']=val4
val5=KDrule2(dataset,'Max_Sys','BPS_load_Night',5)
dataset['BPS_load_Night']=val5
print("==============================")
print("Knowledge-driven Rules")
print("==============================")
print(dataset[cols])
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
cols1 = ['BPS_24','BPD_24','BPS_Day24', 'BPD_Day24', 'BPS_Night24', 'BPD_Night24',
'BPS_load_Day', 'BPS_load_Night']
dataset[cols1] = dataset[cols1].apply(label_encoder.fit_transform)
print("==============================")
print("Translated Features")
print("==============================")
print(dataset)
X = dataset.iloc[:, :33] # data without class label
Y=dataset.iloc[:,34:] # remaining
# Split dataset into train and test
from sklearn.model_selection import train_test_split
#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, shuffle=False)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, shuffle=True)
print("Train Data = ",X_train.shape)
print("Test Data = ",X_test.shape)
from scipy.sparse import lil_matrix
X_train = lil_matrix(X_train).toarray()
Y_train = lil_matrix(Y_train).toarray()
X_test = lil_matrix(X_test).toarray()
# Compute Evaluation metrics
def computeMetrics(Y_test,Y_pred,alg):

 mes1=metrics.precision_recall_fscore_support(Y_test, Y_pred, average='weighted')
 hamloss=metrics.hamming_loss(Y_test, Y_pred)
 jaccard = metrics.jaccard_score(Y_test, Y_pred,average='weighted')
 print("Algorithm = ",alg)
 print("\tPrecision = ",mes1[0])
 print("\tRecall = ",mes1[1])
 print("\tF-measure = ",mes1[2])
 print("\tHamming Loss = ",hamloss)
 print("\tJaccard Score = ",jaccard)
 r1=[mes1[0],mes1[1],mes1[2],hamloss]
 return r1
# NB
from skmultilearn.problem_transform import BinaryRelevance
#from sklearn.naive_bayes import MultinomialNB
#nb = BinaryRelevance(MultinomialNB())
from sklearn.naive_bayes import GaussianNB
nb = BinaryRelevance(GaussianNB())
nb.fit(X_train, Y_train)
nbpred=nb.predict(X_test)
alg1="NB"
nbres=computeMetrics(Y_test,nbpred,alg1)
# Random Forest
from sklearn.ensemble import RandomForestClassifier
from skmultilearn.ensemble import RakelD
rf = RakelD(base_classifier=RandomForestClassifier())
rf.fit(X_train,Y_train)
rfpred=rf.predict(X_test)
alg2="RF"
rfres=computeMetrics(Y_test,rfpred,alg2)
# KNN
from skmultilearn.adapt import MLkNN
knn1 = MLkNN(k=5)
knn1.fit(X_train, Y_train)
knn_pred = knn1.predict(X_test)
alg3="KNN"
knres=computeMetrics(Y_test,knn_pred,alg3)
#SVM
from sklearn import svm
from skmultilearn.ensemble import RakelD
svm1 = RakelD(base_classifier=svm.SVC(kernel='linear'))
svm1.fit(X_train,Y_train)
svm_pred=svm1.predict(X_test)
alg4="SVM"
svmres=computeMetrics(Y_test,svm_pred,alg4)
import numpy as np
import matplotlib.pyplot as plt

N = 4
ind = np.arange(N)
width = 0.15

prevals = [nbres[0], rfres[0], knres[0], svmres[0]]
bar1 = plt.bar(ind, prevals, width, color = 'r')

recvals = [nbres[1], rfres[1], knres[1], svmres[1]]
bar2 = plt.bar(ind+width, recvals, width, color='g')

f1vals = [nbres[2], rfres[2], knres[2], svmres[2]]
bar3 = plt.bar(ind+width*2, f1vals, width, color = 'b')
hamvals = [nbres[3], rfres[3], knres[3], svmres[3]]
bar4 = plt.bar(ind+width*3, hamvals, width, color = 'y')

plt.xlabel("Algorithms")
plt.ylabel('Value')
plt.title("Performance")

plt.xticks(ind+width,['NB', 'RF', 'KNN','SVM'])
plt.legend( (bar1, bar2, bar3,bar4), ('Precision', 'Recall', 'F-measure','Hamming Loss') )
plt.show()
