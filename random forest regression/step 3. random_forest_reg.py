#!/usr/bin/env python
# coding: utf-8

# In[2]:


## This file contains the random forest regression model to indentifying the feature significance of keywords' labels
## following mainly contain 3 parts
## first is our initial random forest model shown in presentation
## second is the result of prediction using our reallocation keywords
## third is our random forest regression model adding the number of types of keywords 

## finding the best number of trees in a random forest
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt

df1 = pd.read_excel("D:\是大学啦\MGT\自动打标_all.xlsx")

## Here is to find the best tree numbers for random forest.
## 175 is chosen for regressing CTR

df1 = df1.fillna(0)
df1.iloc[:, 1:20] = df1.iloc[:, 1:20].astype(int, errors='ignore')
param_grid = {'n_estimators': [100, 125, 150, 175]}
best_param = []
for i in range(20, 23): ## I run the regression for total click numbers, CTR, and CVR respectively
    X = df1.iloc[:, 1:20]  ## But finally only the second one is used
    y = df1.iloc[:, i]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf = RandomForestRegressor(random_state=42)
  
    grid_regress = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error') ## cv?
    grid_regress.fit(X_train, y_train)
    #y_pred = grid_regress.predict(X_test)
    best_param.append(grid_regress.best_params_)

print("the best choice of trees are:", best_param)


# In[4]:
##our initial random forest model shown in presentation

from sklearn import metrics
from sklearn import tree
import matplotlib.pyplot as plt

num_of_trees = [125, 175, 175]
column = [20, 21, 22]
table_name = ["total click numbers", "click rate", "conversion rate"]
features_array = df1.iloc[:, 1:23].columns.values
features = features_array.tolist()
#print(features)

for trees, col, title in zip(num_of_trees, column, table_name):
    X = df1.iloc[:, 1:20]
    y = df1.iloc[:, col]
    rf = RandomForestRegressor(n_estimators=trees, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    estimator = rf.estimators_[5] 
    
    print()
    
    print("This is random forest for", title)
    
    plt.figure(figsize=(28,22))

    _ = tree.plot_tree(decision_tree=estimator, filled=True, feature_names=features, max_depth=4)

    plt.show()
    
    print("The features importances are shown below:")

    importances = rf.feature_importances_

    feat_importances = pd.Series(rf.feature_importances_, index = X_train.columns).sort_values(ascending = False)
    print(feat_importances)
    plt.figure(figsize=(12, 9))
    plt.title(title)


    index = feat_importances.index
    values = feat_importances.values
    index_list = [0, 1, 2, 3, 4]
    legends = ["P: Product", "B:Brand", "C: Component", "F: Function", "R: Region"]
    for i, legend in zip(index_list, legends):
        plt.bar(index[i], values[i], label=legend, color="lightblue")

    plt.legend()

    for i in range(5, 19):
        plt.bar(index[i], values[i], color="lightblue")

    plt.show()


# In[3]:
## the result of prediction using our reallocation keywords
## In the raw data, the average CTR is 0.054

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn import metrics
import numpy as np
from sklearn import tree

df1 = pd.read_excel("D:\是大学啦\MGT\自动打标_all.xlsx")
df2 = pd.read_excel("D:\是大学啦\MGT\predict.xlsx")


df1 = df1.fillna(0)
df2 = df2.fillna(0)
df1.iloc[:, 1:20] = df1.iloc[:, 1:20].astype(int, errors='ignore')

X_train = df1.iloc[:, 1:20]
y_train = df1.iloc[:, 21]
X_pred = df2.iloc[:, 1:20]

rf = RandomForestRegressor(n_estimators=175, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_pred)
avg_pred = np.mean(y_pred)
print(avg_pred) ## this is the predicted average CTR after redistribution，which is around 0.068


# In[23]:

## tag the number of different types of words in keywords

import pandas as pd

df = pd.read_excel("D:\是大学啦\MGT\自动打标_all.xlsx")
df = df.fillna(0)
num_list = []

for i in range(3150):
    if df.iloc[i, 1] == 1 or df.iloc[i, 2] == 1 or df.iloc[i, 3] == 1 or df.iloc[i, 4] == 1 or df.iloc[i, 5] == 1:
        num_list.append(1)
    elif df.iloc[i, 16] == 1 or df.iloc[i, 17] == 1 or df.iloc[i, 18] == 1:
        num_list.append(3)
    elif df.iloc[i, 19] == 1:
        num_list.append(0)
    else:
        num_list.append(2)
        
df["number of words"] = num_list
        
df.to_excel("D:\是大学啦\MGT\自动打标_all.xlsx", index=False)






# In[2]:
## our random forest regression model adding the number of types of keywords 

from sklearn import metrics
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import tree
import pandas as pd

df1 = pd.read_excel("D:\是大学啦\MGT\自动打标_all.xlsx")
column = [20, 21, 22]
table_name = ["total click numbers", "click rate", "conversion rate"]
features_array = df1.iloc[:, 1:23].columns.values
features = features_array.tolist()
#print(features)

for col, title in zip(column, table_name):
    X = df1.iloc[:, 1:21]
    y = df1.iloc[:, col]
    rf = RandomForestRegressor(n_estimators=175, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    estimator = rf.estimators_[5] 
    
    print()
    
    print("This is random forest for", title)
    
    plt.figure(figsize=(28,22))

    _ = tree.plot_tree(decision_tree=estimator, filled=True, feature_names=features, max_depth=4)

    plt.show()
    
    print("The features importances are shown below:")

    importances = rf.feature_importances_

    feat_importances = pd.Series(rf.feature_importances_, index = X_train.columns).sort_values(ascending = False)
    print(feat_importances)
    plt.figure(figsize=(12, 9))
    plt.title(title)


    index = feat_importances.index
    values = feat_importances.values
    index_list = [0, 1, 2, 3, 4]
    legends = ["P: Product", "B:Brand", "C: Component", "F: Function", "R: Region"]
    for i, legend in zip(index_list, legends):
        plt.bar(index[i], values[i], label=legend, color="lightblue")

    plt.legend()

    for i in range(5, 19):
        plt.bar(index[i], values[i], color="lightblue")

    plt.show()


# In[ ]:




