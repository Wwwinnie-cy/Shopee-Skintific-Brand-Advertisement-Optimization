#!/usr/bin/env python
# coding: utf-8

## Thif code is going to generate the keywords wordclous 
## Based on these results, we determine our label (P, B, R, C, F)

# In[1]:

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
path=r"E:\OneDrive - CUHK-Shenzhen\桌面\MGT4187\final"
os.chdir(path)
os.getcwd()


# In[10]:


import contractions
f = open('all_keywords.txt','r', encoding="utf8")
text=f.read()
text=contractions.fix(text)
from collections import Counter
#tokenize
from nltk import word_tokenize
tokens = word_tokenize(text.lower())
print(Counter(tokens).most_common(10))


from string import punctuation
#print(punctuation)
punctuation_add=punctuation+'—'+'“'+'”'+'’'+'‘'+'...'
nopunct_tokens=[t for t in tokens if t not in punctuation_add]

print(Counter(nopunct_tokens).most_common(20))


# In[43]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt
import unicodedata
#%matplotlib widget
wc = WordCloud(max_words=100, colormap='winter', background_color='white')
wc.generate_from_frequencies(Counter(nopunct_tokens))
plt.imshow(wc)
plt.axis("off")
wc.to_file('all.png')


# In[12]:


#skintific split words
import contractions
f = open('skintific_split.txt','r', encoding="utf8")
text=f.read()
text=contractions.fix(text)
from collections import Counter
#tokenize
from nltk import word_tokenize
skin_tokens = word_tokenize(text.lower())
print(Counter(skin_tokens).most_common(20))


# In[45]:


from PIL import Image
import numpy as np
alice_mask = np.array(Image.open("skintific产品3.png"))
wc = WordCloud(max_words=40, mask=alice_mask,colormap='cool', background_color='#F0FFFF')
wc.generate_from_frequencies(Counter(skin_tokens))
plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file('skintific1.png')


# In[46]:


wc = WordCloud(max_words=40, mask=alice_mask,colormap='winter', background_color='#F0FFFF')
wc.generate_from_frequencies(Counter(skin_tokens))
plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file('skintific2.png')


# In[30]:


f = open('skintific_full.txt','r', encoding="utf8")
text=f.read()
skin_full_tokens = text.split('\n')
print(Counter(skin_full_tokens).most_common(20))


# In[67]:


alice_mask = np.array(Image.open("skintific产品2.png"))
wc = WordCloud(max_words=10, colormap='spring', background_color='pink')
wc.generate_from_frequencies(Counter(skin_full_tokens))
plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file('nonsplit.png')


# In[61]:


alice_mask = np.array(Image.open("skintific产品3.png"))
wc = WordCloud(max_words=50, mask=alice_mask,colormap='cool', background_color='white')
wc.generate_from_frequencies(Counter(nopunct_tokens))
plt.imshow(wc)
plt.axis("off")
wc.to_file('all2.png')


# In[ ]:





# In[ ]:




