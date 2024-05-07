## This file is to randomly generate some keywords to roughly verify the reallocation result.
## The number of each type of keywords simply follow the feature (label) significance obtained from the random forest
import pandas as pd
import random
import string

df1 = pd.read_excel("D:\\是大学啦\\MGT\\词典表4.xlsx")
df2 = pd.read_excel("D:\\是大学啦\\MGT\\predict.xlsx")
n = 3150 ## the same number with our keywords data for regression
brand_words = df1.iloc[:, 0]
product_words = df1.iloc[:, 1]
region_words = df1.iloc[:, 2]
function_words = df1.iloc[:, 3]
component_words = df1.iloc[:, 4]

## generate B, annotation here is an example. The following contents follow the same logics
num_B = int(n * 0.011117) ## 0.011117 is the significance of "B"
brand = []
for i in range (num_B):
    index = random.randint(0, 82) ## 82 is the number of words belonging to "B" in our dictionary
    word = df1.iloc[index, 0]
    brand.append(word)
    
## generate P
num_P = int(n * 0.048004)
product = []
for i in range (num_P):
    index = random.randint(0, 62)
    word = df1.iloc[index, 1]
    #print(word)
    product.append(word)
    
## generate R
num_R = int(n * 0.035655)
region = []
for i in range (num_R):
    index = random.randint(0, 19)
    word = df1.iloc[index, 2]
    region.append(word)

## generate F
num_F = int(n * 0.020091)
function = []
for i in range (num_F):
    index = random.randint(0, 67)
    word = df1.iloc[index, 3]
    function.append(word)
    
## generate C
num_C = int(n * 0.008415)
component = []
for i in range (num_C):
    index = random.randint(0, 31)
    word = df1.iloc[index, 4]
    component.append(word)
    
## generate P_B
num_PB = int(n * 0.011480)
PB = []
for i in range (num_PB):
    index1 = random.randint(0, 62)
    index2 = random.randint(0, 82)
    word1 = df1.iloc[index1, 1]
    word2 = df1.iloc[index2, 0]
    word = word1 + " " + word2
    PB.append(word)
    
## generate PR
num_PR = int(n * 0.046494)
PR = []
for i in range (num_PR):
    index1 = random.randint(0, 62)
    index2 = random.randint(0, 19)
    word1 = df1.iloc[index1, 1]
    word2 = df1.iloc[index2, 2]
    word = word1 + " " + word2
    PR.append(word)

## generate PC
num_PC = int(n * 0.020561)
PC = []
for i in range (num_PC):
    index1 = random.randint(0, 62)
    index2 = random.randint(0, 31)
    word1 = str(df1.iloc[index1, 1])
    word2 = str(df1.iloc[index2, 4])
    word = word1 + " " + word2
    PC.append(word)

    
## generate PF
num_PF = int(n * 0.081392)
PF = []
for i in range (num_PF):
    index1 = random.randint(0, 62)
    index2 = random.randint(0, 67)
    word1 = df1.iloc[index1, 1]
    word2 = df1.iloc[index2, 3]
    word = word1 + " " + word2
    PF.append(word)
    
## generate BR
num_BR = int(n * 0.055755)
BR = []
for i in range (num_BR):
    index1 = random.randint(0,82)
    index2 = random.randint(0, 19)
    word1 = df1.iloc[index1, 0]
    word2 = df1.iloc[index2, 2]
    word = word1 + " " + word2
    BR.append(word)

    
## generate BC
num_BC = int(n * 0.137332)
BC = []
for i in range (num_BC):
    index1 = random.randint(0, 82)
    index2 = random.randint(0, 31)
    word1 = df1.iloc[index1, 0]
    word2 = df1.iloc[index2, 4]
    word = str(word1) + " " + str(word2)
    BC.append(word)
    
##generate BF
num_BF = int(n * 0.085824)
BF = []
for i in range (num_BF):
    index1 = random.randint(0, 82)
    index2 = random.randint(0, 67)
    word1 = df1.iloc[index1, 0]
    word2 = df1.iloc[index2, 3]
    word = word1 + " " + word2
    BF.append(word)
    
## generate RC
num_RC = int(n * 0.000197)
RC = []
for i in range (num_RC):
    index1 = random.randint(0, 19)
    index2 = random.randint(0, 31)
    word1 = df1.iloc[index1, 2]
    word2 = df1.iloc[index2, 4]
    word = word1 + " " + word2
    RC.append(word)
    
## generate RF
num_RF = int(n * 0.018289)
RF = []
for i in range (num_RF):
    index1 = random.randint(0, 19)
    index2 = random.randint(0, 67)
    word1 = df1.iloc[index1, 2]
    word2 = df1.iloc[index2, 3]
    word = word1 + " " + word2
    RF.append(word)    

## CF
num_CF = int(n * 0.022025)
CF = []
for i in range (num_CF):
    index1 = random.randint(0, 67)
    index2 = random.randint(0, 31)
    word1 = df1.iloc[index1, 3]
    word2 = df1.iloc[index2, 4]
    word = str(word1) + " " + str(word2)
    CF.append(word)
    
## PBR
num_PBR = int(n * 0.165925)
PBR = []
for i in range (num_PBR):
    index1 = random.randint(0, 82)
    index2 = random.randint(0, 62)
    index3 = random.randint(0, 19)
    word1 = df1.iloc[index1, 0]
    word2 = df1.iloc[index2, 1]
    word3 = df1.iloc[index3, 2]
    word = word1 + " " + word2 + " " + word3
    PBR.append(word)
    
## PBC
num_PBC = int(n * 0.181187)
PBC = []
for i in range (num_PBC):
    index1 = random.randint(0, 82)
    index2 = random.randint(0, 62)
    index3 = random.randint(0, 31)
    word1 = df1.iloc[index1, 0]
    word2 = df1.iloc[index2, 1]
    word3 = df1.iloc[index3, 4]
    word = str(word1) + " " + str(word2) + " " + str(word3)
    PBC.append(word)
    
## PBF
num_PBF = int(n * 0.035851)
PBF = []
for i in range (num_PBF):
    index1 = random.randint(0, 82)
    index2 = random.randint(0, 62)
    index3 = random.randint(0, 67)
    word1 = df1.iloc[index1, 0]
    word2 = df1.iloc[index2, 1]
    word3 = df1.iloc[index3, 3]
    word = word1 + " " + word2 + " " + word3
    PBF.append(word)

    
## Others
num_others = int(n * 0.014407)
others = []
for i in range(num_others):
    length = random.randint(1, 15)
    word = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    others.append(word)

print(others)
    
keyword = brand+product+region+component+function+PB+PC+PF+PR+BR+BC+BF+RC+RF+CF+PBC+PBF+PBR+others
df2["keywords"] = keyword

df2.to_excel("D:\\是大学啦\\MGT\\predict.xlsx", index=False)

## tag the keywords

import pandas as pd
import numpy as np
import re

df1 = pd.read_excel("D:\是大学啦\MGT\predict.xlsx")
df2 = pd.read_excel("D:\是大学啦\MGT\词典表4.xlsx")
i = 0 #记录第几行
for keyword in df1["keywords"]:
    keyword = str(keyword)
    tag = [0, 0, 0, 0, 0] #一共五个值
    #print(keyword)
    word_list = re.split(r'\s+', keyword)  #根据空格split
    #print(word_list)
    for word in word_list:
        for brand in df2.iloc[:, 0]:
            if word == brand:
                tag[0] = 1
        for product in df2.iloc[:, 1]:
            if word == product:
                tag[1] = 1
        for location in df2.iloc[:, 2]:
            if word == location:
                tag[2] = 1
        for func in df2.iloc[:, 3]:
            if word == func:
                tag[3] = 1
        for element in df2.iloc[:, 4]:
            if word == element:
                tag[4] = 1
                
    print(tag) #品牌 产品 部位 功效 成分
    if tag == [1, 0, 0, 0, 0]:
        df1.loc[i, "B"] = 1
    elif tag == [0, 1, 0, 0, 0]:
        df1.loc[i, "P"] = 1
    elif tag == [0, 0, 1, 0, 0]:
        df1.loc[i, "R"] = 1
    elif tag == [0, 0, 0, 1, 0]:
        df1.loc[i, "F"] = 1
    elif tag == [0, 0, 0, 0, 1]:
        df1.loc[i, "C"] = 1
    elif tag == [1, 1, 0, 0, 0]:
        df1.loc[i, "P_B"] = 1
    elif tag == [1, 0, 1, 0, 0]:
        df1.loc[i, "B_R"] = 1
    elif tag == [1, 0, 0, 1, 0]:
        df1.loc[i, "B_F"] = 1
    elif tag == [1, 0, 0, 0, 1]:
        df1.loc[i, "B_C"] = 1
    elif tag == [0, 1, 1, 0, 0]:
        df1.loc[i, "P_R"] = 1
    elif tag == [0, 1, 0, 1, 0]:
        df1.loc[i, "P_F"] = 1
    elif tag == [0, 1, 0, 0, 1]:
        df1.loc[i, "P_C"] = 1
    elif tag == [0, 0, 1, 1, 0]:
        df1.loc[i, "R_F"] = 1
    elif tag == [0, 0, 1, 0, 1]:
        df1.loc[i, "R_C"] = 1
    elif tag == [0, 0, 0, 1, 1]:
        df1.loc[i, "C_F"] = 1
    elif tag == [1, 1, 1, 0, 0]:
        df1.loc[i, "P_B_R"] = 1
    elif tag == [1, 1, 0, 1, 0]:
        df1.loc[i, "P_B_F"] = 1
    elif tag == [1, 1, 0, 0, 1]:
        df1.loc[i, "P_B_C"] = 1
    elif tag == [0, 0, 0, 0, 0]:
        df1.loc[i, "Others"] = 1
    i += 1

df1.to_excel("D:\是大学啦\MGT\predict.xlsx", index=False)