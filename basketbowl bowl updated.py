# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:17:49 2022

@author: forev
"""

import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from importlib import reload
plt=reload(plt)

#Inserting our dataset

df=pd.read_csv('collegefootballbowl.csv')
#print(df.info())


df['date'] = pd.to_datetime(df['date']).dt.date


#Handling Missing Values 

df['winner_rank']=df['winner_rank'].fillna(df['winner_rank'].mode()[0])
df['loser_rank']=df['loser_rank'].fillna(df['loser_rank'].mode()[0])
df['sponsor']=df['sponsor'].fillna('No Sponsor')
#print(len(df),len(df.dropna()))
df=df.dropna()
# =============================================================================
# 
# print(df.isnull().sum())
# sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
# 
# =============================================================================

#Relation of winner_points according to winner_tie(highest point by teams)
# =============================================================================
# 
# df1=df.groupby('winner_tie',as_index=False)['winner_points'].mean()
# df2=df1.sort_values(by='winner_points',ascending=False).head(10)
# #print(df2)
# ax=df2.plot(kind='pie',title='Highest Winning Point by a Team',labels=df2['winner_tie'],y='winner_points',legend=False,explode=(0.2,0,0,0,0,0,0,0,0,0))
# ax.set_ylabel('')
# =============================================================================

#Relation of loser_points according to loser_tie(lowest point by teams)

# =============================================================================
# df1=df.groupby('loser_tie',as_index=False)['loser_points'].mean()
# df1['loser_points']=df1['loser_points'].replace(0.0,0.5)
# df2=df1.sort_values(by='loser_points',ascending=True).head(10)
# #print(df2)
# ax=df2.plot(kind='pie',title='lowest losing Point by a Team',labels=df2['loser_tie'],y='loser_points',legend=False,explode=(0.2,0.2,0.2,0.2,0.2,0.2,0,0,0,0))
# ax.set_ylabel('')
# =============================================================================

#Highly Used Bowl
# =============================================================================
# df3=df.groupby('bowl_name',as_index=False)['year'].count().nlargest(10,columns='year')
# ax=df3.plot(kind='pie',title='Highest used bowl',labels=df3['bowl_name'],y='year',legend=False,explode=(0.2,0,0,0,0,0,0,0,0,0))
# ax.set_ylabel('')
# 
# =============================================================================
 


#Attendance by years

# =============================================================================
# 
# df.plot.bar(x='year',y='attendance',title='Attendance by Year')
# df.plot(kind="line",x='year',y='attendance', use_index=False)
# 
# =============================================================================

plt.show()











