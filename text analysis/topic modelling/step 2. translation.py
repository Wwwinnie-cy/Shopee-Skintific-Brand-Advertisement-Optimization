## translate Indonesian into Englsih 
import pandas as pd
from googletrans import Translator
import time

start = time.time()

df = pd.read_excel("D:\\是大学啦\\MGT\\shopee\\excel\\translated_comment.xlsx")
print(df.info())
df = df.dropna()
df = df.drop_duplicates()
print("after drop, the info is:")
print(df.info())
print(df.head())

translator = Translator()

i = 0
translated_comments = []
for comment in df['评论列']:
    print(i)
    if df.iloc[i, 1] == 0:
        translated_text = translator.translate(comment, src='id', dest='en').text
        translated_comments.append(translated_text)
        df.iloc[i, 1] = translated_text
    if i == 5:
        print(translated_text)

    i += 1

    df.to_excel("D:\\是大学啦\\MGT\\shopee\\excel\\translated_comment.xlsx", index=False)

end = time.time()

running_time = end - start
print("the time spent:", running_time)
