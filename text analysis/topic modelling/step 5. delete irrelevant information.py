## This file is to delete some specific stop-words in this context
## such as the standardized format words: texture, performance as we mentioned before

from spacy.lang.en import English
import pandas as pd
import string

nlp = English()  
df2 = pd.read_excel("D:\\是大学啦\\MGT\\shopee\\excel\\正评论.xlsx")
df3 = pd.read_excel("D:\\是大学啦\\MGT\\shopee\\excel\\负评论.xlsx")

df2 = df2.apply(lambda col: col.astype(str).str.lower())
df3 = df3.apply(lambda col: col.astype(str).str.lower())

pos_comments = df2["pos_comment"].tolist()
neg_comments = df3["neg_comment"].tolist()
filtered_pos = []
filtered_neg = []
deleted_list = ["texture", "performance", "level", "user", "tips", "suitable", "wangi", "benefits", "absorption", "\n", "kelmbaban", "[", "hopefully", "gel"]

i = 0
for sentence in pos_comments:
    print(i)
    doc = nlp(sentence)
    filtered_words = [token.text for token in doc if not token.is_stop]  
    filtered_pos.append(filtered_words)
    i += 1

filtered_pos_remove = [[word for word in sub_list if (word not in string.punctuation) and (word not in deleted_list)] for sub_list in filtered_pos]
df2["pos_comment"] = filtered_pos_remove
df2.to_excel("D:\\是大学啦\\MGT\\shopee\\excel\\正评论_停用词处理.xlsx", index=False)

i = 0
for sentence in neg_comments:
    print(i)
    doc = nlp(sentence)
    filtered_words = [token.text for token in doc if not token.is_stop]  
    filtered_neg.append(filtered_words)
    i += 1

filtered_neg_remove = [[word for word in sub_list if (word not in string.punctuation) and (word not in deleted_list)] for sub_list in filtered_neg]
df3["neg_comment"] = filtered_neg_remove
df3.to_excel("D:\\是大学啦\\MGT\\shopee\\excel\\负评论_停用词处理.xlsx", index=False)