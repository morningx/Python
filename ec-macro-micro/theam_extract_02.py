#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def extract(str,stopwords):
    import pandas as pd
    from wordcloud import WordCloud,STOPWORDS
    import jieba
    import jieba.analyse
    res3=str
    #导入停留词
    stopwords=stopwords
    stopwords_list=stopwords.values.tolist()
    
    c=''
    for i in res3:
        seg=jieba.lcut(i)
        for word in seg:
            if word in stopwords_list:
                continue
            elif word=='hellip':
                continue
            else:
                c=c+' '+word

    return jieba.analyse.extract_tags(c,topK=15,withWeight=True)

