# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 16:14:55 2017

@author: Manish_Jain04
"""
import pandas as pd
s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
data = {'Country': ['Belgium', 'India', 'Brazil'],
'Capital': ['Brussels', 'New Delhi', 'Brasília'],
'Population': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data,
columns=['Country', 'Capital', 'Population'])
df.iloc[0,1]
