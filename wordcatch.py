# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 09:12:39 2019

@author: Anuj
"""

import pandas as pd
import re

train  = pd.read_excel('C:\\Users\\Anuj\\Desktop\ThreeUK2209_Final_1.xlsx')

p = "esim"

add = []
for index, row in train.iterrows():
    #analysis = TextBlob(row['tweet'])
    #print(t)
    result = re.findall(p,row['Tweet'],flags=re.IGNORECASE)
    add.append(result)
    
    
df_word = pd.DataFrame(add)
#df_word = df_word.drop(columns=[1])

merged = pd.merge(left=train,left_index=True,right=df_word, right_index=True,how='inner')    



with pd.ExcelWriter('C:\\Users\\Anuj\\Desktop\\ThreeUK2209_Final_1.xlsx') as writer:  # doctest: +SKIP
    merged.to_excel(writer, sheet_name='ThreeUK',index=False)