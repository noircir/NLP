#!/usr/bin/env python
# coding: utf-8

# # 1. Stemming
# 
# Stemming works fairly well in most of the cases but unfortunately English has so many exceptions where a more sophisticated process is required.
# 
# SpaCy dosen't include stemming, it uses lemmatization instead.
# 
# Stemming is basically removes the suffixes from a word and reduce it to its root word.
# 
# We will use Natural Language Toolkit (nltk) to understand and learn stemming
# 

# ## Porter Stemmer

# In[1]:


import nltk
from nltk.stem.porter import PorterStemmer


# In[2]:


p_stemmer = PorterStemmer() # object of class PorterStemmer


# In[3]:


words = ['run','runner','running','ran','runs','easily','fairly'] # list of words 


# In[4]:


for word in words:
    print(word + '------>' + p_stemmer.stem(word))


# ## Snowball Stemmer
# 
# Snowball Stemmer is also called the "English Stemmer" or "Porter2 Stemmer"
# It offers a slight improvement over the original Porter stemmer

# In[5]:


from nltk.stem.snowball import SnowballStemmer
# Pass a language parameter
s_stemmer = SnowballStemmer(language='english')


# In[6]:


for word in words:
    print(word +' --> '+ s_stemmer.stem(word))


# In[ ]:




