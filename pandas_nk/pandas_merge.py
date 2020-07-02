# https://github.com/zhangleiszu/pandas
# https://segmentfault.com/a/1190000018537597?utm_source=tag-newest
# https://www.cnblogs.com/bigshow1949/p/7016235.html
# 1. Merge方法
# pandas的merge方法是基于共同列，将两个dataframe连接起来。下面分析merge方法的主要参数含义：
# left/right：左/右位置的dataframe。
# how：数据合并的方式。left：基于左dataframe列的数据合并；right：基于右dataframe列的数据合并；outer：基于列的数据外合并（取并集）；inner：基于列的数据内合并（取交集）；默认为'inner'。
# on：用来合并的列名，这个参数需要保证两个dataframe有相同的列名。
# left_on/right_on：左/右dataframe合并的列名，也可为索引，数组和列表。
# left_index/right_index：是否以index作为数据合并的列名，True表示是。
# sort：根据dataframe合并的keys排序，默认是。
# suffixes：若有相同列且该列没有作为合并的列，可通过suffixes设置该列的后缀名，一般为元组和列表类型。
# merges通过设置how参数选择两个dataframe的连接方式，有内连接，外连接，左连接，右连接，下面通过例子介绍连接的含义。
# 1.1 内连接
# how='inner'，dataframe的链接方式为内连接，我们可以理解基于共同列的交集进行连接，参数on设置连接的共有列名
# 单列的内连接
# 定义df1
import pandas as pd
import numpy as np

# ---单列
df1 = pd.DataFrame({'alpha':['A','B','B','C','D','E'],'feature1':[1,1,2,3,3,1],'feature2':['low','medium','medium','high','low','high']})
df2 = pd.DataFrame({'alpha':['A','A','B','F'],'pazham':['apple','orange','pine','pear'],'kilo':['high','low','high','medium'],'price':np.array([5,6,5,7])})
# print(df1)
# print(df2)
# df3 = pd.merge(df1,df2,how='inner',on='alpha')  # 基于共同列alpha的内连接
# print(df3, '----inner')
# # how='outer'，dataframe的链接方式为外连接，我们可以理解基于共同列的并集进行连接，参数on设置连接的共有列名。若两个dataframe间除了on设置的连接列外并无相同列，则该列的值置为NaN。
# df4 = pd.merge(df1,df2,how='outer',on='alpha')  # # 单列的外连接
# print(df4,'-----outer')
# df5 = pd.merge(df1,df2,how='left',on='alpha')  # 基于共同列alpha的左连接# 单列的左连接
# print(df5,'-----left')
# df6 = pd.merge(df1,df2,how='right',on='alpha') # 基于共同列alpha的右连接
# print(df6,'-----right')

# ------多列
df1 = pd.DataFrame({'alpha':['A','B','B','C','D','E'],'beta':['a','a','b','c','c','e'],'feature1':[1,1,2,3,3,1],'feature2':['low','medium','medium','high','low','high']})
df2 = pd.DataFrame({'alpha':['A','A','B','F'],'beta':['d','d','b','f'],'pazham':['apple','orange','pine','pear'],'kilo':['high','low','high','medium'],'price':np.array([5,6,5,7])})
# print(df1)
# print(df2)
df7 = pd.merge(df1,df2,on=['alpha','beta'],how='inner')  # 基于共同列alpha和beta的内连接
# print(df7,'-----inner')
# 基于共同列alpha和beta的右连接
df8 = pd.merge(df1,df2,on=['alpha','beta'],how='right')
# print(df8,'---right')
df8 = pd.merge(df1,df2,on=['alpha','beta'],how='left')
# print(df8,'------left')
df8 = pd.merge(df1,df2,on=['alpha','beta'],how='outer')
# print(df8,'------outer')
# join方法是基于index连接dataframe，merge方法是基于column连接，连接方法有内连接，外连接，左连接和右连接，与merge一致。
# caller = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'], 'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
# other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],'B': ['B0', 'B1', 'B2']})
# print(caller)
# print(other)
# df1 = caller.join(other,lsuffix='_caller', rsuffix='_other',how='inner')   # lsuffix和rsuffix设置连接的后缀名
# print(df1)
# df1 = caller.set_index('key').join(other.set_index('key'),how='inner')   # 基于key列进行连接
# print(df1)
# df1 = pd.Series([1.1,2.2,3.3],index=['i1','i2','i3'])
# df2 = pd.Series([4.4,5.5,6.6],index=['i2','i3','i4'])
# df = pd.concat([df1,df2])  # 行拼接
# print(df1,'=---1')
# print(df2,'---2')
# # print(df)
# df = pd.concat([df1,df2],keys=['fea1','fea2'])  # 对行拼接分组
# print(df,'----3')
# df = pd.concat([df1,df2],axis=1)  # 列拼接的内连接（交）
# print(df,'---4')
# df = pd.concat([df1,df2],axis=1,join='inner',keys=['fea1','fea2'])    # 列拼接的内连接（交）
# print(df,'---5')
# df = pd.concat([df1,df2] )    # 指定索引[i1,i2,i3]的列拼接
# print(df,'---6')
# pd.concat([df1,df2],axis=1,verify_integrity = True)  # 判断是否有重复的列名，若有则报错


# https://github.com/zhangleiszu/pandas
# https://segmentfault.com/a/1190000018537597?utm_source=tag-newest
# https://www.cnblogs.com/bigshow1949/p/7016235.html

#---------------------------2--------------------------------

df1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
df2 = pd.DataFrame({'key':['a','b','d'],'data1':range(3)})
print(df1,'---df1')
print(df2,'---df2')
df3 = pd.merge(df1,df2)
print(df3,'---df3')