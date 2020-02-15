#!/usr/bin/env python
# coding: utf-8

# - 1 深度系统deepin linux环境下运行
# - 2 未能解决绘图饼图中展示的分块内容的中文乱码问题

# In[2]:


road = r'/media/apple/A29E38759E384457/Study/data/20200126-jinshuju-wuhanfeiyan/wuhanfeiyan_202001261715.csv'
road


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


df = pd.read_csv(road)
df.head(2)


# In[5]:


df.info()


# In[6]:


# 发现mysql重命名有个错误
# df1.rename(columns={'c':'D'},inplace=True) 
df.rename(columns={'control feelings':'control_feelings'},inplace=True)
df.columns


# In[7]:


data = df.copy()
data.head(2)


# In[8]:


df[df.location.isnull()]
# 查询空值结果为布尔值false-true，再代入到df中，则可找到此列为true值的


# In[9]:


# 用常见的　湖北省武汉市　代替location空值
df[df.location.isnull()]['location'] = '湖北省武汉市'
df[df.location.isnull()]
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead


# In[45]:


df[df.location.isnull()].location.fillna('湖北省武汉市',inplace=True)
# 输出警告不支持填充　
# A value is trying to be set on a copy of a slice from a DataFrame


# In[11]:


df.location[438:440, ]


# In[12]:


# df['近期销量']=df['近期销量'].replace(np.nan,'0').astype(int)
df['location'] = df['location'].replace(np.nan,'湖北省武汉市')


# In[13]:


df.location[438:440, ]


# In[14]:


df.info()


# In[15]:


df[df['correct_understanding'].isnull()]


# In[16]:


df['correct_understanding'].value_counts(ascending=False)
# 用值出现最多的string来替换空值


# In[17]:


df['correct_understanding'] = df['correct_understanding'].replace(np.nan,'病毒对老年人有严重的威胁，75%浓度酒精可以杀死病毒，病毒会进化，并且致死性越来越强')


# In[18]:


df.correct_understanding[56:57, ]


# In[19]:


df.correct_understanding[382:383, ]


# In[20]:


df.info()


# In[21]:


df.control_feelings.value_counts()


# In[ ]:


df[df.control_feelings.isnull()]
# Nan为空值，用中立不作判断最好，且为最多的值
# time	id	age	sex	education	job	location	correct_understanding	my_party	parent_party	channel_find_info	control_feelings	hospital_resource_shortage	family_medical_resources	family_living_resources
# 1	2020-01-26 03:48:37	203	26~30	女	高中/中专/技校	个体经营户	福建省莆田市	病毒会进化，并且致死性越来越强，病毒对老年人有严重的威胁，感染病毒后会立即出现咳嗽、发烧的症...	有中型聚会安排（5～10人）	父母已取消所有聚会安排	微信好友，公众号，微信群，微博，微信朋友圈，抖音，电视新闻	NaN	没有确凿信息，不断定	口罩，体温计，酒精	未储备
# 314	2020-01-25 23:36:22	60	26~30	女	大学本科	上班族/创业者	安徽省宣城市	病毒对老年人有严重的威胁，75%浓度酒精可以杀死病毒，病毒致死性很强，病毒会进化，并且致死性...	有中型聚会安排（5～10人）	父母已取消所有聚会安排	微信好友，公众号，微信群，微信朋友圈，微博，抖音，电视新闻	NaN	没有确凿信息，不断定	保健品	未储备


# In[23]:


df['control_feelings'] = df['control_feelings'].replace(np.nan,'中立，不做判断')


# In[24]:


df.info()


# In[25]:


df[df.family_medical_resources.isnull()]


# In[26]:


df.family_medical_resources.value_counts()


# In[27]:


df['family_medical_resources'] = df['family_medical_resources'].replace(np.nan,'口罩')


# In[28]:


df.info()


# In[29]:


df.describe()


# In[30]:


df.head(2)


# In[31]:


df.age.value_counts()


# In[32]:


df[df.sex == '女']['age'].value_counts()


# In[33]:


df[df.sex == '男']['age'].value_counts()


# In[34]:


df[df.sex == '女']['age'].value_counts().sort_values()


# In[35]:


df[df.sex == '男']['age'].value_counts().sort_values()


# In[36]:


df.sex.value_counts()


# In[37]:


df[df.sex == '女']['age'].value_counts().index


# In[38]:


df[df.sex == '女']['age'].value_counts().values


# In[39]:


age_woman = df[df.sex == '女']['age'].value_counts().values
age_woman


# In[40]:


age_man = df[df.sex == '男']['age'].value_counts().values
age_man


# In[41]:


labels_woman = df[df.sex == '女']['age'].value_counts().index
labels_woman


# In[42]:


type(labels_woman)


# In[43]:


labels_woman = list(labels_woman)


# In[44]:


labels_woman[0]


# In[45]:


labels_woman[4] = '<18'
labels_woman


# In[46]:


labels_woman[6] = '>60'
labels_woman


# In[47]:


labels_man = list(df[df.sex == '男']['age'].value_counts().index)
labels_man


# In[48]:


labels_man[5] = '<18'
labels_man


# In[49]:


import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei-windows.ttf'] 
# 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False
# 步骤二（解决坐标轴负数的负号显示问题）


# In[50]:


plt.figure(figsize=(10,6))
plt.pie(age_woman,labels=labels_woman,autopct='%1.1f%%')
plt.title("woman-age")
plt.show()


# - 1 调研问卷传播渠道原因，存在男女性别用户在不同渠道看到导致调研男女不一样
# - 2 从调研结果来看，女性年轻人0-30岁占据80%，男性30岁以内占据80%
# - 3.1 20来岁非典40来岁肺炎，苍天放过谁追杀的微信截图段子
# - 3.2 从调研数据来看，这部分人群男性总共占据5%,女性总共占据4.3%

# In[55]:


plt.rcParams['font.sans-serif'] = ['SimHei-windows.ttf']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(8,6))
plt.pie(age_man,labels=labels_man,autopct='%1.1f%%')
plt.title("男性年龄调研情况",fontproperties=myfont)
plt.show()


# In[56]:


# import matplotlib.pyplot as plt
import matplotlib
matplotlib.matplotlib_fname()


# In[57]:


ttfroad = '/usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/SimHei-windows.ttf'
ttfroad


# In[58]:


# https://www.linuxidc.com/Linux/2019-03/157632.htm
ttfroad = '/usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/SimHei-windows.ttf'
import matplotlib 
# matplotlib.use('qt4agg') 
from matplotlib.font_manager import * 
import matplotlib.pyplot as plt 
#定义自定义字体，文件名从1.b查看系统中文字体中来 
myfont = FontProperties(fname=ttfroad) 
#解决负号'-'显示为方块的问题 
matplotlib.rcParams['axes.unicode_minus']=False 
#notebook模式下绘图内嵌
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot([-1,2,-5,3]) 
plt.title(u'test',fontproperties=myfont) 
plt.show()


# In[59]:


df.head(2)


# In[60]:


channel1 = df.channel_find_info.value_counts()
channel1


# In[ ]:


channel2 = df.channel_find_info.values
channel2
# array(['微信好友，公众号，微信群，微信朋友圈，微博，电视新闻', '微信好友，公众号，微信群，微博，微信朋友圈，抖音，电视新闻',
#       '微信群，公众号，微信好友，微信朋友圈，微博', '公众号，微信群，微信朋友圈，微博，抖音，电视新闻，微信好友',
#       '微信好友，公众号，微信群，微信朋友圈，微博，抖音，电视新闻，其他', '微信群，公众号，微信朋友圈，电视新闻',


# In[ ]:


channel3 = list(df.channel_find_info.values)
channel3
# ['微信好友，公众号，微信群，微信朋友圈，微博，电视新闻',
# '微信好友，公众号，微信群，微博，微信朋友圈，抖音，电视新闻',
# '微信群，公众号，微信好友，微信朋友圈，微博',
# '公众号，微信群，微信朋友圈，微博，抖音，电视新闻，微信好友',
# '微信好友，公众号，微信群，微信朋友圈，微博，抖音，电视新闻，其他',
# '微信群，公众号，微信朋友圈，电视新闻',


# In[ ]:


from collections import Counter
result = Counter(channel3)
result
# channel3是列表内多个字符串组合，字符串内的数据没单独抽离
# Counter({'微信好友，公众号，微信群，微信朋友圈，微博，电视新闻': 19,
#         '微信好友，公众号，微信群，微博，微信朋友圈，抖音，电视新闻': 2,
#         '微信群，公众号，微信好友，微信朋友圈，微博': 1,


# In[64]:


channel3[0]


# In[65]:


channel3[0].split(',')


# In[66]:


channel3[1].split(',')


# In[67]:


channel3[1].split('，')[0]
# 单个字符内是中文，区分，split时得用中文的，逗号


# In[68]:


channel3[1].split('，')[1]


# In[69]:


len(channel3[1].split('，'))


# In[70]:


for itest in range(len(channel3[1].split('，'))):
    print(itest)
    print(channel3[1].split('，')[itest])


# In[71]:


len(channel3)


# In[72]:


print(range(len(channel3)))


# In[ ]:


list_all_channel = []
for i in range(len(channel3)):
    for j in range(len(channel3[i].split('，'))):
    # print(i)
        list_all_channel.append(channel3[i].split('，')[j])
list_all_channel
# ['微信好友',
# '公众号',
# '微信群',
# '微信朋友圈',
# '微博',
# '电视新闻',
# '微信好友',


# In[74]:


len(list_all_channel)


# In[75]:


type(list_all_channel)


# In[76]:


from collections import Counter
result = Counter(list_all_channel)
result
# list_all_channel为列表数据，已经抽离出字符串成为单个字符
# 从调研获取信息传播渠道来看，大部分人群是通过微信来获取信息


# In[77]:


dict(result)


# In[78]:


channel_keys = dict(result).keys()
channel_keys


# In[79]:


channel_values = dict(result).values()
channel_values


# In[80]:


list(result.items())[0][0]


# In[81]:


list(result.items())[0][1]


# In[82]:


list(result.items())[0]


# In[83]:


plt.rcParams['font.sans-serif'] = ['SimHei-windows.ttf']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(8,6))
plt.pie(channel_values,labels=channel_keys,autopct='%1.1f%%')
plt.title("传播渠道占比情况",fontproperties=myfont)
plt.show()


# In[84]:


# https://www.linuxidc.com/Linux/2019-03/157632.htm
ttfroad = '/usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/SimHei-windows.ttf'
import matplotlib 
# matplotlib.use('qt4agg') 
from matplotlib.font_manager import * 
import matplotlib.pyplot as plt 
#定义自定义字体，文件名从1.b查看系统中文字体中来 
myfont = FontProperties(fname=ttfroad) 
#解决负号'-'显示为方块的问题 
matplotlib.rcParams['axes.unicode_minus']=False 
#notebook模式下绘图内嵌
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['font.sans-serif'] = ['SimHei-windows.ttf']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(8,6))
plt.pie(channel_values,labels=channel_keys,autopct='%1.1f%%')
plt.title("传播渠道占比情况",fontproperties=myfont)
plt.show()


# In[87]:


print(channel_keys)
print(channel_values)


# In[91]:


channel_keys2 = ['wechat_friends',
                 'wechat_official_account',
                 'weixin_group',
                 'wechat_circle_of_friends',
                 'weibo',
                 'tv_news',
                 'tik_tok',
                 'others']
plt.figure(figsize=(10,6))
plt.pie(channel_values,labels=channel_keys2,autopct='%1.1f%%')
plt.title("传播渠道占比情况",fontproperties=myfont)
plt.show()


# - 1 微信好友－公众号－微信群－微信朋友圈，腾讯的微信渠道占据了49%份额，抽样人群一半比例看微信
# - 2 微博份额、朋友圈，传播渠道份额一致，占据16％份额
# - 3 电视新闻渠道份额约等于朋友圈，占据14%，朋友圈可信度　vs 电视新闻可信度　应该没有相关性
# - 4.1 抖音用来刷肺炎新闻只占据6%份额，传播新闻力度上偏小
# - 4.2 抖音从娱乐本身角度来说，报喜不报忧，信息传播复杂度较差，继而推荐算法视频谣言及评论置顶也无传播谣言的可能

# In[92]:


df.head(2)


# In[94]:


df.my_party.value_counts()


# In[95]:


df.age.value_counts()


# In[96]:


df.sex.value_counts()


# In[102]:


df_girl = df[df.sex == '女']
df_girl


# In[103]:


df_girl.age.value_counts()


# In[118]:


df_girl_age_1825 = df_girl[df_girl.age == '18~25']
df_girl_age_1825


# In[119]:


df_girl_age_2630 = df_girl[df_girl.age == '26~30']
df_girl_age_2630


# In[121]:


df_girl_younpeople = df_girl_age_1825.append(df_girl_age_2630)
df_girl_younpeople


# In[123]:


df_girl_age_little_18 = df_girl[df_girl.age == '18岁以下']
df_girl_age_little_18


# In[124]:


df_girl_younpeople = df_girl_younpeople.append(df_girl_age_little_18)
df_girl_younpeople


# In[126]:


df_girl_younpeople.education.value_counts()


# In[128]:


labels_woman2 = df[df.sex == '女']['age'].value_counts().index
labels_woman2


# In[132]:


age_woman2 = df[df.sex == '女']['age'].value_counts().values
age_woman2


# In[130]:


labels_man2 = df[df.sex == '男']['age'].value_counts().index
labels_man2


# In[131]:


age_man2 = df[df.sex == '男']['age'].value_counts().values
age_man2


# In[133]:


df_boy = df[df.sex == '男']
df_boy_age_1825 = df_boy[df_boy.age == '18~25']
df_boy_age_2630 = df_boy[df_boy.age == '26~30']
df_boy_age_little18 = df_boy[df_boy.age == '18岁以下']
df_boy_younpeople = df_boy_age_1825.append(df_boy_age_2630)
df_boy_younpeople = df_boy_younpeople.append(df_boy_age_little18)
df_boy_younpeople.education.value_counts()


# In[134]:


df_girl_younpeople.education.value_counts()


# In[140]:


print(df_girl_younpeople.shape)
print(df_boy_younpeople.shape)


# In[141]:


df_girl_younpeople.head(2)


# In[142]:


df_boy_girl_younpeople = df_boy_younpeople.append(df_girl_younpeople)
df_boy_girl_younpeople.shape


# In[143]:


df_boy_girl_younpeople.parent_party.value_counts()


# In[144]:


df_boy_girl_younpeople.my_party.value_counts()


# In[149]:


young_myparty_keys = list(df_boy_girl_younpeople.my_party.value_counts().index)
young_myparty_keys


# In[150]:


young_myparty_values = list(df_boy_girl_younpeople.my_party.value_counts().values)
young_myparty_values


# In[152]:


young_myparty_keys2 = ['no_party','5_10_people','0_5_people','>11_people']
plt.figure(figsize=(10,6))
plt.pie(young_myparty_values,labels=young_myparty_keys2,autopct='%1.1f%%')
plt.title("年轻男女聚会情况",fontproperties=myfont)
plt.show()


# In[153]:


young_parentsparty_keys = list(df_boy_girl_younpeople.parent_party.value_counts().index)
young_parentsparty_keys


# In[154]:


young_parentsparty_values = list(df_boy_girl_younpeople.parent_party.value_counts().values)
young_parentsparty_values


# In[157]:


young_parentsparty_keys2 = ['parents_no_party','parents_yes_party','do_not_know']


# In[158]:


plt.figure(figsize=(10,6))
plt.pie(young_parentsparty_values,labels=young_parentsparty_keys2,autopct='%1.1f%%')
plt.title("年轻男女的父母聚会情况",fontproperties=myfont)
plt.show()


# In[159]:


# 121 > 1行2列第1个
fig1 = plt.subplot(121)
plt.pie([1,2,3])
# 122 > 1行2列第2个
fig2 = plt.subplot(122)
plt.pie([10,5,5])
plt.show()


# In[164]:


plt.figure(figsize=(20,8))
fig1 = plt.subplot(121)
plt.pie(young_parentsparty_values,labels=young_parentsparty_keys2,autopct='%1.1f%%')
plt.title("年轻男女的父母聚会情况",fontproperties=myfont,fontsize=20)
fig2 = plt.subplot(122)
plt.pie(young_myparty_values,labels=young_myparty_keys2,autopct='%1.1f%%')
plt.title("年轻男女聚会情况",fontproperties=myfont,fontsize=20)
plt.show()
# 明知山有虎偏向虎山行，年轻人和年轻人的父母还是会选择聚会的情况差不多
# 并不是读过书的人就一定真的懂得拒绝聚会带来的可能性肺炎影响


# In[165]:


df.head(2)


# In[167]:


df.info()

