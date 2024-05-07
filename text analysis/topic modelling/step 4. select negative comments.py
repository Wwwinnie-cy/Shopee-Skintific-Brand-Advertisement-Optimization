## This file is to select negative comments from all comments
## save them into a single excel respectively

from gensim import corpora
from gensim.models import LdaModel
from gensim.models.coherencemodel import CoherenceModel
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    df1 = pd.read_excel("D:\\是大学啦\\MGT\\shopee\\excel\\translated_comment.xlsx")
    df2 = pd.read_excel("D:\\是大学啦\\MGT\\shopee\\excel\\正评论.xlsx")
    df3 = pd.read_excel("D:\\是大学啦\\MGT\\shopee\\excel\\负评论.xlsx")

    pos_comment = []
    neg_comment = []

    length = len(df1)

    for index, row in df1.iterrows():
        #print("thos is index", index)
        if df1.iloc[index, 2] == "pos":
            #print("yes")
            pos_comment.append(df1.iloc[index, 1])
        elif df1.iloc[index, 2] == "neg":
            #print("no")
            neg_comment.append(df1.iloc[index, 1])

    df2["pos_comment"] = pos_comment
    df3["neg_comment"] = neg_comment

    #print(pos_comment[0])

    df2.to_excel("D:\\是大学啦\\MGT\\shopee\\excel\\正评论.xlsx", encoding = 'utf-8', index=False) ## 0列是pos，1列是neg
    df3.to_excel("D:\\是大学啦\\MGT\\shopee\\excel\\负评论.xlsx", encoding = 'utf-8', index=False)

    print("preparing files are finished.")





