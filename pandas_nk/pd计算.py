import pandas as pd
import numpy as np


g = lambda x : x ** 2
print(g(3))
#多个参数的：
g = lambda x, y, z : (x + y) ** z
print(g(1,2,2))
map( lambda x: x*x, [y for y in range(10)] )  #将一个 list 里的每个元素都平方：

# Python中apply函数的格式为：apply(func,*args,**kwargs)
def function(a, b):
    print(a, b)
# tt = apply(function, ('good', 'better'))
# apply(function, (2, 3 + 6))
# apply(function, ('cai', 'quan'))
# apply(function, ('cai',), {'b': 'caiquan'})
# apply(function, (), {'a': 'caiquan', 'b': 'Tom'})
# 函数应用和映射
import numpy as np
import pandas as pd

np.random.randint(100, 200, (3 ,4))

df = pd.DataFrame(np.random.randint(1, 30, (4, 3)), columns=list('bde'), index=['utah', 'ohio', 'texas', 'oregon'])
print(df,'---1')
# 将函数应用到由各列或行形成的一维数组上。DataFrame的apply方法可以实现此功能
f = lambda x: x.max() - x.min()
# 默认情况下会以列为单位，分别对列应用函数
t1 = df.apply(f)
print(t1,'---2')
t2 = df.apply(f, axis=1)
print(t2,'---3')
# 除标量外，传递给apply的函数还可以返回由多个值组成的Series
def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])
t3 = df.apply(f)
# 从运行的结果可以看出，按列调用的顺序，调用函数运行的结果在右边依次追加
print(t3,'---4')
# 元素级的python函数，将函数应用到每一个元素
# 将DataFrame中的各个浮点值保留两位小数
f = lambda x: '%.2f' % x
t3 = df.applymap(f)
print(t3,'---6')
# 注意，之所以这里用map,是因为Series有一个元素级函数的map方法。而dataframe只有applymap。
t4 = df['e'].map(f)
print(t4,'---5')




# a = [[1,np.nan,'9'],[2,8,3],[3,5,np.nan]]
# df = pd.DataFrame(a,index=['a','b','c'],columns=['one','two','three'])
# print('df,',df)
# print(df.sum(),'---sum')    # 默认对列求和
# print(df['one'].sum(),'---sum1')    # 默认对列求和
# print(df.sum(axis=1),'---sum2')   # 对行求和
# # print(df.sum(axis=1),'---sum3')   # 对行求和
# print(df.mean(axis=1),'---mean1')  # 对行求平均值，默认排除Nan
# print(df.mean(axis=1,skipna=False), '---means')     # 禁用排除NaN
#
# print(df.idxmax(),'---返回每列中最大值的索引')
# print(df.idxmin(),'---返回每列最小值的索引')
# print(df.cumsum(),'---对每列值进行累加')
# print(df.describe(),'---四分位数用于绘制箱线图判断是否为异常值')
"""
   one  two three
a    1  NaN     9
b    2  8.0     3
c    3  5.0   NaN
one     6.0
two    13.0
dtype: float64 ---sum
a     1.0
b    10.0
c     8.0
dtype: float64 ---sum2
a    1.0
b    5.0
c    4.0
dtype: float64 ---mean1
a    NaN
b    5.0
c    4.0
dtype: float64 ---means
"""