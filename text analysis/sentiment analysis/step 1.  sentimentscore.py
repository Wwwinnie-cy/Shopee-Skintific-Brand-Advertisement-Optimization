#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#%matplotlib widget
import matplotlib.pyplot as plt
import numpy as np
import os
import re
path=r"E:\OneDrive - CUHK-Shenzhen\桌面\MGT4187\final\sentiment"
os.chdir(path)
os.getcwd()


# In[2]:


#pos
pos = pd.read_excel('positive.xlsx')
pos['word']=pos['word'].astype('string')
pos.head()
pos_word = []
for i in pos['word']:
    pos_word.append(i)


# In[3]:


#neg
neg = pd.read_excel('negative.xlsx')
neg['word']=neg['word'].astype('string')
neg.head()
neg_word = []
for i in neg['word']:
    neg_word.append(i)


# In[4]:


neg_weight = []
for i in neg['weight']: 
    neg_weight.append(i)
pos_weight = []
for i in pos['weight']: 
    pos_weight.append(i)


# In[5]:


def compute_sentiment(text):
    
    text=re.sub('[^\w+\s\']','',text)
    positive=0
    negative=0
    for i in pos_word:
        if i in text:
            index=pos_word.index(i)
            pweight=pos_weight[index]
            positive=positive+pweight
    for i in neg_word:
        if i in text:
            index=neg_word.index(i)
            nweight=neg_weight[index]
            negative=negative+nweight 
    net_sentiment = positive+negative
    return net_sentiment


# In[6]:


#skintific_5X
skintific_5X = pd.read_excel('skintific_5X_comment.xlsx')
skintific_5X=skintific_5X.dropna(subset=['Comments']).reset_index(drop=True) 
skintific_5X['Comments']=skintific_5X['Comments'].astype('string')
skintific_5X['net_sentiment']=skintific_5X.Comments.apply(compute_sentiment)
skintific_5X.head(20)


# In[7]:


skintific_5X_sentiment= sum(skintific_5X['net_sentiment'])/len(skintific_5X)
print(skintific_5X_sentiment)


# In[8]:


#somethinc
somethinc = pd.read_excel('somethinc_comment.xlsx')
somethinc=somethinc.dropna(subset=['Comments']).reset_index(drop=True) 
somethinc['Comments']=somethinc['Comments'].astype('string')
somethinc['net_sentiment']=somethinc.Comments.apply(compute_sentiment)
somethinc.head(20)


# In[9]:


somethinc_sentiment= sum(somethinc['net_sentiment'])/len(somethinc)
print(somethinc_sentiment)


# In[10]:


#scatter plot_skintific
plt.clf()
fig = plt.figure()
ax = fig.add_subplot()
x_values = skintific_5X.index
y_values = skintific_5X['net_sentiment']
plt.ylim(-100, 40)
ax.scatter(x_values, y_values, s=30, color="#069AF3", marker="v")
ax.set_ylabel('skintific_sentiment_score', family='Times New Roman',fontsize=16)
ax.set_xlabel('comments', family='Times New Roman',fontsize=16)
plt.xticks(color='black', family='Times New Roman')
plt.yticks(color='black', family='Times New Roman')
plt.savefig('skintific_5X.png', dpi=300)


# In[11]:


#scatter plot_somethinc
plt.clf()
fig = plt.figure()
ax = fig.add_subplot()
x_values = somethinc.index
y_values = somethinc['net_sentiment']
plt.ylim(-100, 40)
ax.scatter(x_values, y_values, s=30, color="#7BC8F6", marker="v")
ax.set_ylabel('somethinc_sentiment_score', family='Times New Roman',fontsize=16)
ax.set_xlabel('comments', family='Times New Roman',fontsize=16)
plt.xticks(color='black', family='Times New Roman')
plt.yticks(color='black', family='Times New Roman')
plt.savefig('somethinc.png', dpi=300)


# In[ ]:




