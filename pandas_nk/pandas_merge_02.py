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
一、Concat: 合并多个数组
简单的合并可以通过Pandas中的concat函数来实现的。
帐号登录
concat 可横向按行合并，可纵向按列合并
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)
obs：带合并的对象集合，可以是Series，DataFrame
axis：{0，1....}合并方向，默认为0，表示纵向，1表示横向；
join：{inner，outer}：合并方式，默认为outer，表示并集；inner表示交集；
join_axes: 按哪些对象的索引保存；
ignore_index:{False,True},是否忽略原 index，默认为不忽略
keys：为原始dataframe添加一个键，默认为无
1、  result=pd.concat(frames)
代码示例：
eg：列相连，索引保持原状
>>> s1 = pd.Series(['a', 'b'])
>>> s2 = pd.Series(['c', 'd'])
>>> pd.concat([s1, s2])
0    a
1    b
0    c
1    d
dtype: object
>>> pd.concat([s1, s2], ignore_index=True) #重新建立索引
0    a
1    b
2    c
3    d
dtype: object
2、  result = pd.concat(frames, keys=['x', 'y', 'z'])
代码示例：
>>> pd.concat([s1, s2], keys=['s1', 's2',])  #增加新的keys
s1  0    a
    1    b
s2  0    c
    1    d
dtype: object
>>> pd.concat([s1, s2], keys=['s1', 's2'],
...           names=['Series name', 'Row ID'])   #新增列名
Series name  Row ID
s1           0         a
             1         b
s2           0         c
             1         d
dtype: object

result.ix['y']
Out[7]:
    A   B   C   D
4  A4  B4  C4  D4
5  A5  B5  C5  D5
6  A6  B6  C6  D6
7  A7  B7  C7  D7
3、 result=pd.concat([df1, df2],axis=1)
#横向链接(按照index连接)，这里是把所有的元素联接接在一起：
>>> df1 = pd.DataFrame([['a', 1], ['b', 2]],
...                    columns=['letter', 'number'])
>>> df1
  letter  number
0      a       1
1      b       2
>>> df2 = pd.DataFrame([['c', 3], ['d', 4]],
...                    columns=['letter', 'number'])  #注意这里是列名
>>> df2
  letter  number
0      c       3
1      d       4
>>> pd.concat([df1, df2])
  letter  number
0      a       1
1      b       2
0      c       3
1      d       4
>>> df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],
...                    columns=['letter', 'number', 'animal']) #按列名合并
>>> df3
  letter  number animal
0      c       3    cat
1      d       4    dog
>>> pd.concat([df1, df3])
  animal letter  number
0    NaN      a       1
1    NaN      b       2
0    cat      c       3
1    dog      d       4
>>>dfa = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog'],['w', 8, 'pig']],
...                    columns=['letter', 'number', 'animal']) #按列名合并
>>>dfa
	letter	number	animal
0	c	3	cat
1	d	4	dog
2	w	8	pig
>>>pd.concat([df1,dfa])
	animal	letter	number
0	NaN	a	1
1	NaN	b	2
0	cat	c	3
1	dog	d	4
2	pig	w	8
>>>pd.concat([df1,dfa],ignore_index=True)
animal	letter	number
0	NaN	a	1
1	NaN	b	2
2	cat	c	3
3	dog	d	4
4	pig	w	8
axis=1，按照索引来合并
5、result = pd.concat([df1, df4], axis=1, join_axes=[df1.index])
>>> df4 = pd.DataFrame([['bird', 'polly'], ['monkey', 'george']],
                      columns=['animal', 'name'])
	animal	name
0	bird	polly
1	monkey	george
>>> df1
  letter  number
0      a       1
1      b       2
>>> pd.concat([df1, df4], axis=1)
  letter  number  animal    name
0      a       1    bird   polly
1      b       2  monkey  george
6.result = pd.concat([df1, s1], axis=1)
 7.result = pd.concat([df1, s2, s2, s2], axis=1)
8.result = pd.concat([df1, s1], axis=1, ignore_index=True)
二、append：附加；贴上
横向和纵向同时扩充，不考虑columns和index
1、向数据框添加序列
In [1]: s2 = pd.Series(['X0', 'X1', 'X2', 'X3'], index=['A', 'B', 'C', 'D'])
In [2]: result = df1.append(s2, ignore_index=True)
# 此刻你需要使用ignore_index,丢弃DataFrame的索引；如果你还想保存该索引，
则应该构造一个适当的DataFrame，并追加这些对象。
2、向数据框添加字典
result = df1.append(dicts, ignore_index=True)
3、向数据框添加数据框
3.1 result = df1.append(df2)
>>> df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
>>> df
   A  B
0  1  2
1  3  4
>>> df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
>>> df.append(df2)
   A  B
0  1  2
1  3  4
0  5  6
1  7  8
3.2、result= df1.append(df4)
3.3 可同时添加两个数据框
result = df1.append([df2, df3])
3.4 添加数据框以后重新排列索引
result = df1.append(df4, ignore_index=True)
三、merge
merge 函数通过一个或多个键来将数据集的行连接起来。该函数的应用场景是针对同一个主键存在两张包含不同特征的表，通过该主键的链接，将两张表进行合并。合并之后，两张表的行数没有增加，列数是两张表的列数之和减一。
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False)
当两个数据集合并的列名不相同时用 left_on,right_on
on=None: 指定连接的列名，若两列希望连接的列名不一样，可以通过left_on和right_on 来具体指定,不指定时pandas会自动找到相同名字的列
how=’inner’,参数指的是左右两个表主键那一列中存在不重合的行时，取结果的方式：inner表示交集，outer 表示并集，left 和right 表示取某一边。

2. result = pd.merge(left, right, on='key')
3、通过indicator表明merge的方式
4.多条件合并
 result = pd.merge(left, right, on=['key1', 'key2'])
 result = pd.merge(left, right, how='left', on=['key1', 'key2'])
 result = pd.merge(left, right, how='right', on=['key1', 'key2'])
5、result = pd.merge(left, right, how='outer', on=['key1', 'key2'])
6、result = pd.merge(left, right, how='inner', on=['key1', 'key2'])
7、多数据集合并
是针对合并后的数据再合并，不是一次性合并几个数据集
df1=pd.DataFrame({'key':['a','b','c','d','e'],'data1':np.arange(5)})
df2=pd.DataFrame({'key':['a','b','c'],'data2':np.arange(3)})
df3=pd.DataFrame({'key':['a','b','c','d'],'data3':np.arange(4)})

data=pd.merge(pd.merge(df1,df2,on='key',how='left'),df3,on='key',how='left')
In [55]: data
Out[55]:
   data1 key  data2  data3
0      0   a    0.0    0.0
1      1   b    1.0    1.0
2      2   c    2.0    2.0
3      3   d    NaN    3.0
4      4   e    NaN    NaN
四、join
In [1]: left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                              'B': ['B0', 'B1', 'B2']},
                               index=['K0', 'K1', 'K2'])
In [2]: right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                               'D': ['D0', 'D2', 'D3']},
                                index=['K0', 'K2', 'K3'])
In [3]: result = left.join(right)
In [4]: result = left.join(right, how='outer')
#这与merge的以下用法相似
result = pd.merge(left, right, left_index=True, right_index=True, how='outer')
result = left.join(right, how='inner')
#这与merge的以下用法相似
result = pd.merge(left, right, left_index=True, right_index=True, how='inner');
result = pd.concat([df1, df4], axis=1, join_axes=[df1.index])

四、combine
若df1的数据缺失，则用df2的数据值填充df1的数据值
df1 = pd.DataFrame([[1, np.nan]])
df2 = pd.DataFrame([[3, 4]])
a=pd.Series([np.nan,2.5,np.nan,3.5,4.5,np.nan],index=['f','e','d','c','b','a'])
b=pd.Series([1,np.nan,3,4,5,np.nan],index=['f','e','d','c','b','a'])

汇总：
1、pandas.concat——可沿一条轴将多个对象链接到一起；
pandas.merge——可根据一个或多个键将不同的DataFrame中的行连接起来。
join——如果为’inner’得到的是两表的交集，如果是outer，得到的是两表的并集；如果有join_axes的参数传入，可以指定根据那个轴来对齐数据。
在使用merge和join时，以Dataframe数据结构为例，Dataframe1和Dataframe2必须在至少一列上内容有重叠，index也好，colunms也好，只要内容有重叠的列即可，指定其中一列或几列作为连接的键，然后按照键，索引Dataframe2其他列上的数据，添加到Dataframe1中。
combine—first可以将重复数据编排在一起，用一个对象中的值填充另一个对象中的值。





df1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
df2 = pd.DataFrame({'key':['a','b','d'],'data1':range(3)})
print(df1,'---df1')
print(df2,'---df2')
df3 = pd.merge(df1,df2)
print(df3,'---df3')

