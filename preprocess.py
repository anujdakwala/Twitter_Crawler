# -- coding: utf-8 --
"""
Created on Fri Mar 22 19:10:35 2019

@author: ADakwala0070313
"""

import re
import pandas as pd 
import numpy as np 
import string
import warnings 
from textblob import TextBlob
warnings.filterwarnings("ignore", category=DeprecationWarning)

train  = pd.read_excel('C:\\Users\\Anuj\\Desktop\\GetOldTweets-python-master\\ThreeUK0207.xlsx')
df = train[~train['username'].isin(['EE','O2','ThreeUKSupport','ThreeUK','VodafoneUK','Vodafoneprobs])]
#df = train[~train['username'].isin(['ThreeUKSupport','ThreeUK'])]
#df = train[~train['username'].isin(['VodafoneUK','Vodafoneprobs'])]
#df = train[train['tweet'].isin(['@ EE','# EE'])]    
preprocesstrain =  df[df['mentions'].notnull() | (df['hashtags'].notnull())]

s = preprocesstrain.reset_index()
#s = s.drop(columns="index")


df2 = s.copy()
#print(df2)


sentiment = []

for index, row in df2.iterrows():
    analysis = TextBlob(row['tweet'])
    #print(analysis)
    if analysis.sentiment[0]>0:
     
        #sentiment.append(score)
        s = 'Positive'
        sentiment.append(s)
    
    elif analysis.sentiment[0]<0:
         
        
        s = 'Negative'
        sentiment.append(s)
    else:
                   
       s = 'Neutral'
       sentiment.append(s)


score = []

for index, row in df2.iterrows():
    analysis = TextBlob(row['tweet'])
    #print(analysis)
    if analysis.sentiment[0]>0:
        sent_score = analysis.sentiment[0]
        score.append(sent_score)
       
    
    elif analysis.sentiment[0]<0:
         
        sent_score = analysis.sentiment[0]
        score.append(sent_score)
    
    else:
       
       sent_score = analysis.sentiment[0]
       score.append(sent_score)
    



dfsentiment = pd.DataFrame({'sentiment_score':score,'sentiment':sentiment})

merged = pd.merge(left=df2,left_index=True,right=dfsentiment, right_index=True,how='inner')

with pd.ExcelWriter('C:\\Users\\Anuj\\Desktop\\GetOldTweets-python-master\\ThreeUK0207_Update.xlsx') as writer:  # doctest: +SKIP
    merged.to_excel(writer, sheet_name='O2')
