import pandas as pd
import numpy as np


df1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
df2 = pd.DataFrame({'key':['a','b','d'],'data2':range(3)})
pd.merge(df1,df2)

#如果两个DataFrame的列名不同，可以分别指定
df3 = pd.DataFrame({'lkey':['b','b','a','c','a','a','b'],'data1':range(7)})
df4 = pd.DataFrame({'rkey':['a','b','d'],'data2':range(3)})
pd.merge(df3,df4,left_on='lkey',right_on='rkey')
pd.merge(df1,df2,how='outer')

#要根据多个键进行合并，传入一组由列名组成的列表即可:
left = pd.DataFrame({'key1':['foo','foo','bar'],'key2':['one','two','one'],'lval':[1,2,3]})
right = pd.DataFrame({'key1':['foo','foo','bar','bar'],'key2':['one','one','one','two'],'rval':[4,5,6,7]})
t01 = pd.merge(left,right,on=['key1','key2'],how='outer')
print(left,'---001')
print(right,'---002')
print(t01,'---003')

# 上面两个表有两列重复的列，如果只根据一列进行合并，则会多出一列重复列，重复列名的处理我们一般使用merge的suffixes属性,可以帮我们指定重复列合并后的列名
pd.merge(left,right,on='key1',suffixes=('_left','_right'))
# 上面的on、left_on、right_on都是根据列值进行合并的，如果我们想用索引进行合并，使用left_index 或者 right_index属性
left1 = pd.DataFrame({'key':['a','b','a','a','b','c'],'value':range(6)})
right1 = pd.DataFrame({'group_val':[3.5,7]},index=['a','b'])
pd.merge(left1,right1,left_on='key',right_index=True)

# 对于层次化索引的数据，我们必须以列表的形式指明用作合并键的多个列:
lefth = pd.DataFrame({'key1':['Ohio','Ohio','Ohio','Nevada','Nevada'],
                     'key2':[2000,2001,2002,2001,2002],
                     'data':np.arange(5.0)})
righth = pd.DataFrame(np.arange(12).reshape((6,2)),
                      index=[['Nevada','Nevada','Ohio','Ohio','Ohio','Ohio'],[2001,2000,2000,2000,2001,2002]],
                     columns=['event1','event2'])
pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True)
# 如果单纯想根据索引进行合并，使用join方法会更加简单：
left2 = pd.DataFrame([[1.0,2.0],[3.0,4.0],[5.0,6.0]],index = ['a','c','e'],columns=['Ohio','Nevada'])
right2 = pd.DataFrame([[7.0,8.0],[9.0,10.0],[11.0,12.0],[13.0,14.0]],index = ['b','c','d','e'],columns=['Missouri','Alabama'])
left2.join(right2,how='outer')

### --------------- 1.2 轴向链接
# pandas的轴向链接指的是根据某一个轴向来拼接数据，类似于列表的合并。concat函数,默认在轴0上工作，我们先来看一个Series的例子：
s1 = pd.Series([0,1],index=['a','b'])
s2 = pd.Series([2,3,4],index=['c','d','e'])
s3 = pd.Series([5,6],index=['f','g'])
pd.concat([s1,s2,s3])
# 在上面的情况下，参与连接的片段在结果中区分不开，假设你想要在连接轴上创建一个层次化索引，我们可以额使用keys参数
result = pd.concat([s1,s1,s3],keys=['one','two','three'])
print(result)
# 如果是沿着axis=1进行轴向合并，keys会变为列索引:
pd.concat([s1,s1,s3],keys=['one','two','three'],axis=1)
# 上面的逻辑同样适用于DataFrame的轴向合并:
df1 = pd.DataFrame(np.arange(6).reshape((3,2)),index=['a','b','c'],columns=['one','two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape((2,2)),index=['a','c'],columns=['three','four'])

pd.concat([df1,df2],axis=1,keys=['level1','level2'])

#下面的操作会得到与上面同样的效果
pd.concat({"level1":df1,'level2':df2},axis=1)
# 使用ignore_index参数可以不保留轴上的索引，产生一组新的索引:
df1 = pd.DataFrame(np.arange(6).reshape((3,2)),index=[1,2,3],columns=['one','two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape((2,2)),index=[1,2],columns=['three','four'])
pd.concat([df1,df2],ignore_index = True)

###  -----------2、重塑和轴向旋转
# 在重塑和轴向旋转中，有两个重要的函数，二者互为逆操作：
# stack:将数据的列旋转为行
# unstack:将数据的行旋转为列
# 先来看下面的例子：
data = pd.DataFrame(np.arange(6).reshape((2,3)),index=pd.Index(['Ohio','Colorado'],name='state'),
                    columns=pd.Index(['one','two','three'],name='number'))
result = data.stack()

# 我们使用unstack()将数据的列旋转为行，默认是最里层的行索引：
result.unstack()

