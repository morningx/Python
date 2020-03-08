#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def wordcloud(x):
    res3=x
    from wordcloud import WordCloud,STOPWORDS
    import matplotlib.pyplot as plt
    import jieba

    text=""
    for i in res3:
        text=text+" ".join(jieba.cut(i))

    #配置词云的基本参数
    my_cloud=WordCloud(
                        background_color='white',
                        stopwords=STOPWORDS,#也可用自带的停留词
                        font_path='C:/Windows/Fonts/simsun.ttc',
                        width=1000,
                        height=500)

    #用分好的词进行词云de生成
    my_cloud.generate(text)
    #显示词云
    plt.rcParams['figure.figsize']=(10,6)
    plt.imshow(my_cloud)
    plt.axis('off')
    plt.show()

