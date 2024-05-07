#!/usr/bin/env python
# coding: utf-8

# In[2]:


## The following is doing topic modelling for skintific negative comments
from gensim import corpora
from gensim.models import LdaModel
from gensim.models.coherencemodel import CoherenceModel
import pandas as pd
import matplotlib.pyplot as plt

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

df2.to_excel("D:\\是大学啦\\MGT\\shopee\\excel\\正评论.xlsx", index=False) ## 0列是pos，1列是neg
df3.to_excel("D:\\是大学啦\\MGT\\shopee\\excel\\负评论.xlsx", index=False)


# In[10]:


df4 = pd.read_excel("D:\\是大学啦\\MGT\\shopee\\excel\\正评论_停用词处理.xlsx")
df5 = pd.read_excel("D:\\是大学啦\\MGT\\shopee\\excel\\负评论_停用词处理.xlsx")

pos_comments = df4["pos_comment"].tolist()
neg_comments = df5["neg_comment"].tolist()

tokenized_pos_word = [comment.split() for comment in pos_comments]
tokenized_neg_word = [comment.split() for comment in neg_comments]

# 创建词典
pos_dict = corpora.Dictionary(tokenized_pos_word)
neg_dict = corpora.Dictionary(tokenized_neg_word)

## build corpora
pos_corpus = [pos_dict.doc2bow(word) for word in tokenized_pos_word]
neg_corpus = [neg_dict.doc2bow(word) for word in tokenized_neg_word]


# In[11]:
## for negative modelling
min_topics = 2
max_topics = 5
coherence_scores = []

for num_topics in range(min_topics, max_topics + 1):
    lda_model = LdaModel(corpus=neg_corpus, id2word=neg_dict, num_topics=num_topics)
    coherence_model = CoherenceModel(model=lda_model, texts=tokenized_neg_word, dictionary=neg_dict, coherence='c_v')
    coherence_score = coherence_model.get_coherence()
    coherence_scores.append(coherence_score)
    print(f"Num Topics: {num_topics}, Coherence Score: {coherence_score}")

x = [2, 3, 4, 5]
plt.plot(x, coherence_scores)
plt.title("Coherence scores of different topic numbers")

# 根据Coherence score选择最优主题数量
optimal_num_topics = coherence_scores.index(max(coherence_scores)) + min_topics
print(f"Optimal number of topics: {optimal_num_topics}")


# In[15]:


neg_model = LdaModel(neg_corpus, num_topics=5, id2word=neg_dict, passes=15)


# In[17]:


## choosing the number of topics as 5

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def show_wordcloud(model, topic_id, colormap='viridis'):
    words = dict(model.show_topic(topic_id))
    wordcloud = WordCloud(width=550, height=250, background_color='white', colormap=colormap).generate_from_frequencies(words)
    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"The wordcloud of topic {topic_id + 1}") 
    plt.show()

show_wordcloud(neg_model, 0, colormap='viridis')
show_wordcloud(neg_model, 1, colormap='plasma')
show_wordcloud(neg_model, 2, colormap='coolwarm')
show_wordcloud(neg_model, 3, colormap='viridis')
show_wordcloud(neg_model, 4, colormap='plasma')


# In[18]:


num_topics = 5 # 主题数量
for topic_id in range(num_topics):
    words = neg_model.show_topic(topic_id)
    print(f"主题 {topic_id + 1}:")
    for word, prob in words:
        print(f"{word}: {prob}")
    print("\n")


# In[19]:


neg_model = LdaModel(neg_corpus, num_topics=4, id2word=neg_dict, passes=15)


# In[20]:


## choosing the number of topics as 4

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def show_wordcloud(model, topic_id, colormap='viridis'):
    words = dict(model.show_topic(topic_id))
    wordcloud = WordCloud(width=550, height=250, background_color='white', colormap=colormap).generate_from_frequencies(words)
    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"The wordcloud of topic {topic_id + 1}") 
    plt.show()

show_wordcloud(neg_model, 0, colormap='viridis')
show_wordcloud(neg_model, 1, colormap='plasma')
show_wordcloud(neg_model, 2, colormap='coolwarm')
show_wordcloud(neg_model, 3, colormap='viridis')
#show_wordcloud(neg_model, 4, colormap='plasma')


# In[21]:


num_topics = 4 # 主题数量
for topic_id in range(num_topics):
    words = neg_model.show_topic(topic_id)
    print(f"主题 {topic_id + 1}:")
    for word, prob in words:
        print(f"{word}: {prob}")
    print("\n")


# In[22]:


neg_model = LdaModel(neg_corpus, num_topics=2, id2word=neg_dict, passes=15)


# In[23]:


## choosing the number of topics as 2, which we decided to utilize

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def show_wordcloud(model, topic_id, colormap='viridis'):
    words = dict(model.show_topic(topic_id))
    wordcloud = WordCloud(width=550, height=250, background_color='white', colormap=colormap).generate_from_frequencies(words)
    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"The wordcloud of topic {topic_id + 1}") 
    plt.show()

show_wordcloud(neg_model, 0, colormap='viridis')
show_wordcloud(neg_model, 1, colormap='plasma')


# In[24]:


num_topics = 2 # 主题数量
for topic_id in range(num_topics):
    words = neg_model.show_topic(topic_id)
    print(f"主题 {topic_id + 1}:")
    for word, prob in words:
        print(f"{word}: {prob}")
    print("\n")

