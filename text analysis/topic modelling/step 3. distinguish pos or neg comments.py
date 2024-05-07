## The fllowing are classifying all translated comments into neg and pos for topic modelling since we only need negative comments

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

def get_key_from_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key

df = pd.read_excel("D:\\是大学啦\\MGT\\shopee\\excel\\translated_comment.xlsx")

list2 = []
list3 = []

for i in range(2955): 
    sentence = df.iloc[i, 1] #col need to be checked  ## col0: ori; col1:trans; col2: status; col3: compound
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(sentence) 

    score = vs["compound"]
    if score >= -1 and score <= -0.05:
        list2.append("neg")
    elif score >= -0.05 and score <= 0.05:
        list2.append("neu")
    else:
        list2.append("pos")

    list3.append(score)

df["state"] = list2
df["compound score"] = list3
df.to_excel("D:\\是大学啦\\MGT\\shopee\excel\\translated_comment.xlsx", index=False)


## The following is to generate plots to see the distribution of negative comments
## We didn't use the results in presentation or report
df = pd.read_excel("D:\\是大学啦\\MGT\\shopee\\excel\\translated_comment.xlsx")

num_of_state = []
neg, neu, pos = 0, 0, 0
state_name = ["neg", "neu", "pos"]
colors = ["purple", "lightblue", "pink"]

for i in range(2955):  
    if df.iloc[i, 2] == "neg":
        neg += 1
    elif df.iloc[i, 2] == "neu":
        neu += 1
    elif df.iloc[i, 2] == "pos":
        pos += 1

num_of_state.extend([neg, neu, pos])
print(num_of_state)

plt.bar(state_name, num_of_state, color=colors)
plt.title("The number of different sentiments")

plt.show()


sorted_data = df.sort_values(df.columns[3])  # 第四列（索引为3）是 'compound' 列

top_five = sorted_data.tail(5)  # 获取最后五行
bottom_five = sorted_data.head(5)  # 获取前五行

print("Top 5 comments with highest 'compound' values:")
print(top_five.iloc[:, 0])  

print("\nBottom 5 comments with lowest 'compound' values:")
print(bottom_five.iloc[:, 0]) 


