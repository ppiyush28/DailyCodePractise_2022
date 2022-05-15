# -*- coding: utf-8 -*-
"""
Created on Sat May 14 14:25:23 2022

@author: Piyush
"""
#Classification of hospital dataset 


import pandas as pd
#import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import re

df=pd.read_excel('C:\\Users\\Piyush\\Desktop\\Data.xlsx')

sns.countplot(x="l1",data=df)


def data_clean(data):
    text = re.sub(r"[^a-zA-Z?.!,¿,. . ,]"," ",data)
    text = re.sub(r"[\s+]"," ",data)
    return text.lower()

df['data_clean'] = df['item_description'].apply(lambda x : data_clean(x))

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer()

input = tfidf.fit_transform(df['data_clean'])
#output = tfidf.fit_transform(df['l1'])
#ValueError: Unknown label type: 'continuous-multioutput'
print(input)
#print(output)

#x = df['item_description']
#y = df['l1']

#df['clean_text'] = df['item_description'].replace('#', '').replace('%', '').replace('-','').replace('+','').replace('"','')

from sklearn import preprocessing

lab_enc = preprocessing.LabelEncoder()
output = lab_enc.fit_transform(df['l1'])

print(output)

x_train,x_test,y_train,y_test=train_test_split(input,output,test_size=0.3)



#model
from sklearn.tree import DecisionTreeClassifier 

tree =DecisionTreeClassifier()

tree.fit(x_train,y_train)


pred = tree.predict(x_test)

from sklearn.metrics import classification_report

print(classification_report(pred,y_test))


