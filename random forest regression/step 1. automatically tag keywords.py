## for the code runned on jupyter and pictures are generated, we provide html to show the result directly
## The raw data contains around 6k data, but you can see that the labeled keywords only around 3k
## That's because in the raw data, the same keywords may contain several rows
## The labeled data only choose one keyword once, the corresponding data (CTR...) is the average if this keyword appears more than once

#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
import numpy as np
import re

df1 = pd.read_excel("D:\是大学啦\MGT\自动打标_all.xlsx")
df2 = pd.read_excel("D:\是大学啦\MGT\词典表4.xlsx")

i = 0 #记录第几行
for keyword in df1["keywords"]:
    keyword = str(keyword)
    tag = [0, 0, 0, 0, 0] #一共五个值
    #print(keyword)
    word_list = re.split(r'\s+', keyword)  #根据空格split
    #print(word_list)
    for word in word_list:
        for brand in df2["品牌"]:
            if word == brand:
                tag[0] = 1
        for product in df2["产品"]:
            if word == product:
                tag[1] = 1
        for location in df2["部位"]:
            if word == location:
                tag[2] = 1
        for func in df2["功效"]:
            if word == func:
                tag[3] = 1
        for element in df2["成分"]:
            if word == element:
                tag[4] = 1
                
    print(tag) #品牌 产品 部位 功效 成分
    if tag == [1, 0, 0, 0, 0]:
        df1.loc[i, "品牌词"] = 1
    elif tag == [0, 1, 0, 0, 0]:
        df1.loc[i, "产品词"] = 1
    elif tag == [0, 0, 1, 0, 0]:
        df1.loc[i, "部位词"] = 1
    elif tag == [0, 0, 0, 1, 0]:
        df1.loc[i, "功效词"] = 1
    elif tag == [0, 0, 0, 0, 1]:
        df1.loc[i, "成分词"] = 1
    elif tag == [1, 1, 0, 0, 0]:
        df1.loc[i, "产品词+品牌词"] = 1
    elif tag == [1, 0, 1, 0, 0]:
        df1.loc[i, "品牌词+部位词"] = 1
    elif tag == [1, 0, 0, 1, 0]:
        df1.loc[i, "品牌词+功效词"] = 1
    elif tag == [1, 0, 0, 0, 1]:
        df1.loc[i, "品牌词+成分词"] = 1
    elif tag == [0, 1, 1, 0, 0]:
        df1.loc[i, "产品词+部位词"] = 1
    elif tag == [0, 1, 0, 1, 0]:
        df1.loc[i, "产品词+功效词"] = 1
    elif tag == [0, 1, 0, 0, 1]:
        df1.loc[i, "产品词+成分词"] = 1
    elif tag == [0, 0, 1, 1, 0]:
        df1.loc[i, "部位词+功效词"] = 1
    elif tag == [0, 0, 1, 0, 1]:
        df1.loc[i, "部位词+成分词"] = 1
    elif tag == [0, 0, 0, 1, 1]:
        df1.loc[i, "成分词+功效词"] = 1
    elif tag == [1, 1, 1, 0, 0]:
        df1.loc[i, "产品词+品牌词+部位词"] = 1
    elif tag == [1, 1, 0, 1, 0]:
        df1.loc[i, "产品词+品牌词+功效词"] = 1
    elif tag == [1, 1, 0, 0, 1]:
        df1.loc[i, "产品词+品牌词+成分词"] = 1
    elif tag == [0, 0, 0, 0, 0]:
        df1.loc[i, "其他"] = 1
    i += 1
    #print(i)

    
        
df1.to_excel("D:\是大学啦\MGT\自动打标_all.xlsx", index=False)
    





