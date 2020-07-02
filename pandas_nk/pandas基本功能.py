import pandas as pd
import numpy as np

pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)
pd.set_option('max_colwidth',7000)
pd.set_option('expand_frame_repr', False)
pd.set_option('float_format', lambda x: '%.3f' % x)

# Numpy的arange函数 生成一个list，np.arange(3,9,3)
# df = pd.DataFrame(np.random.randint(1, 30, (4, 3)), columns=list('bde'), index=['utah', 'ohio', 'texas', 'oregon'])

df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
idx = df.columns # get col index
label = df.columns[0] # 1st col label
lst = df.columns.tolist() # get as a list
lst=['A', 'B', 'C', 'D']
label='A'
df = pd.DataFrame({'name':['a','a','b','b'],'classes':[1,2,3,4],'price':[11,22,33,44]})
df1 = pd.DataFrame({'alpha':['-A','B','B','C','D','-E'],'ft1':[1,1,2,3,3,1],'ft2':['low','medium','medium','high','low','high']})
# df2 = pd.DataFrame({'alpha':['A','A','B','F'],'pazham':['apple','orange','pine','pear'],'kilo':['high','low','high','medium'],'price':np.array([5,6,5,7])})
print(df1,'----df1')
print(df1.head(3),'---head')
print(df1.tail(2),'----tail')
df1.dropna(how="all",axis=1)  #删除满足列内数据均为NaN这个条件的列，按列删除
#查看类型2这一列的非缺失值和缺失值的数量分布
# df["类型2"].isnull().value_counts()
# df["类型2"].notnull().value_counts()
df1['addclo'] = [1,11,22,3,33,1]
print(df1,'---add clo')
data = df1.drop('addclo',axis=1,inplace=False)
# data = data.drop(index=data[data['A'].isin([4])].index.to_list()) #删除包含4的行
print(data,'---drop')
print(df1[['alpha','ft1']],'---选取多列')
print(df1)
行：df.shape[0]   或者：len(df)
列：df.shape[1]
https://www.cnblogs.com/traditional/p/11967360.html  #pandas行转列、列转行、以及一行生成多行

df1['alpha'] = df1['alpha'].replace('-A',"00")
print(df1,'---替换后敷在给df')
print(df1['alpha'].str.replace('A|B',"00"),'--多字符串替换')  #df.info的数据类型，非数值类型就是object即是str类型
print(df1['alpha'].str.len())  #
df1['ft3'] = df1['ft1'] * 100 + df1['ft1'].astype(float)             # 列计算, astype 转化为float。数据类型转换
print(df1)
df1['date'] = '2020-03-03'
print(pd.to_datetime(df1['date']))  # str日期转换为date类型
# df1.iloc['行索引'，‘列索引’]
print(df1.iloc[2:5,1:3],'---iloc')    #  索引含首不含尾的原则
print(df1.iloc[2:5,[3,5]],'---iloc')  # 【3,5】选取3和5列
print(df1.loc[df1['ft1']==3,['addclo','ft3']],'---loc') #morenm默认取筛选的值，
print(df1.loc[df1['ft1'] !=3,['addclo','ft3']],'---loc') # 剔除 - 筛选的值，
# 以>,<,==,>=,<=来进行选择（“等于”一定是用‘==’，如果用‘=’就不是判断大小了）：  https://www.cnblogs.com/sxinfo/p/10385810.html
# 使用 &（且） 和 |（或） 时每个条件都要用小括号括起来。
# 选取多列一定是两个方括号，其中内侧方括号代表是一个list：
print(df1.loc[df1['ft1'].isin([1,2,3]),['addclo','ft3']])      #如果要选择某列等于多个数值或者字符串时，要用到.isin()， 我们把df修改了一下（isin()括号里面应该是个list）：
# name,price = df1.loc[df1.classes==1,('name','price')].values[0]  # 取多行多列的值
print( (df1['ft1'] > df1['ft1'].mean()) & (df1['ft1'] > df1['ft1'].sum()),  '-----列判断')
df['name'] = df['name'].apply(lambda x: x.upper())
df.loc[:, 'name'] = df['name'].apply(lambda x: x.upper())
df.loc[:, ['classes','price']] = df[['classes', 'price']].applymap(lambda x: int(x))
ms = df1.loc[(df1['ft1'] > df1['ft1'].mean()) & (df1['ft1'] > df1['ft1'].sum()),:]
print(ms,'---loc多判断')
# abb_full_df = abb_full_df.dropna(subset=['zyorg_abb_name']).reset_index(inplace=False)
# abb_full_df = abb_full_df[['dc_id', 'xls_full_name', 'xls_abb_name']]
# abb_full_df.columns = ['org_id', 'org_name', 'org_abb']
# -------- group + apply
df_gp = df1.groupby('alpha')[['ft1','ft2']]   #  按照 alpha --》 ft1 --》 ft2 分组
print(df_gp,'---df_gp')
def get_third(x):
    if len(x) <= 1:
        return x.iloc[0,:]  # 返回第 0 行的所有值
    else:
        return x.iloc[1,:]  # 直接返回排名第三行和索引是2的值
df_gp_apply = df1.groupby('alpha')[['ft1','ft2']].apply(get_third)   #  按照 alpha --》 ft1 --》 ft2 分组
print(df_gp_apply,'----df_gp_apply')

df.drop_duplicates(subset=['classes', 'name'], inplace=True)    # 多列去重，inplace在df上操作
df = df.loc[df['name']!='a']    #删除特定值
# df = df[df['a'].str.contains(r'A')]    #删除特定值  SQL语句里用的是like，在pandas里我们可以用.str.contains()来实现。
"""
        whitelist_df['emp_name'] = whitelist_df['emp_name'].str.replace("(\(.*?\))", "", regex=True)
        whitelist_df['emp_name'] = whitelist_df['emp_name'].str.replace("(（.*?）)", "", regex=True)
# df = pd.DataFrame({"A": ["Hello", "this", "World", "apple"]})
# df.A.str.contains("Hello|World")
# ~df.A.str.contains("Hello|World")
# df[~df.A.str.contains("Hello|World")]       #方案一
# data[~((data.title.str.contains('公告'))  |(data.title.str.contains('意见')))]
# 
# df[df['A'].str.contains("Hello|World")==False]  # 方案二
# df[df["col1"].str.contains('this|that')==False and df["col2"].str.contains('foo|bar')==True]
"""
# dx = df.set_index('A')  # 把A列变为index
# df = dx.reset_index('A')  #把index 变为A列
# dd = df.groupby(by=['A'])['B'].sum()  #按照列A分组，将同一组的列B求和,生成新的Dataframe
# df.to_sql('表名',con=engine,if_exists='replace/append/fail',index=False)

# tel_list = df['tel'].values.tolist()
# abb_full_df = df.drop(index=df[df['tel'].isin(tel_list)].index.to_list())  # 删除指定列值相等的行
# index=whitelist_df[whitelist_df["wl_companyname"]=="无"].index.to_list()
# df.iloc[0:0,0:1].columns.tolist()[0] ; print(list(df))  ;  print(df.columns.values)

people = pd.DataFrame(np.random.randn(5, 5), columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people.iloc[2:3, [1, 2]] = np.nan # Add a few NA values
print(people, '----people')
mapping = {'a': 'red', 'b': 'red', 'c': 'blue','d': 'blue', 'f': 'red', 'e' : 'orange'}
           #mapping中可以存在没有对应的列，程序不会对其进行匹配
by_column = people.groupby(mapping, axis=1)
print(by_column.sum() ,'-----by_column')
df.sort_index(by=['a','b'])
df = pd.DataFrame({'A': ['a', 'b', 'a', 'c', 'a', 'c', 'b', 'c'],  'B': [2, 8, 1, 4, 3, 2, 5, 9], 'C': [102, 98, 107, 104, 115, 87, 92, 123]})
print(df,'----gpb')
print(df.groupby("A").mean(),'---mean')     #pi平均数（均数）
print(df.groupby("A").agg({'B':'mean', 'C':'sum'}),'---agg')     #平均数（均数）
# print(df.groupby("A")['B'].agg({'mean':'mean', 'sum':'sum'}),'---agg')     #按分组后统计

df = pd.DataFrame({"Name":["Alice", "Bob", "Mallory", "Mallory", "Bob" , "Mallory"],"City":["Seattle", "Seattle", "Portland", "Seattle", "Seattle", "Portland"],"Val":[4,3,3,np.nan,np.nan,4]})
print(df,'---gb')
print(df.groupby(["Name", "City"], as_index=False )['Val'].count(),'---count')       # count 值nan不计数
print(df.groupby(["Name", "City"])['Val'].size().reset_index(name='Size'),'---size')    #size 值nan计数
# df['count_B']=df.groupby(['group1', 'group2'])['B'].transform('count')  # transform count分组
# pd.cut(df['Age'], bins=4)       #   这里将“Age”列分成三类

# #通过rename函数修改部分列名或者所有列名，并默认返回一个新的数据框，若需要在原基础上修改，添加参数inplace=True即可
# df.rename(columns={"name":"name2","age":"age2"},inplace=True)
# #通过columns属性修改列名，这种方式就需要输入所有的列名了，并直接在原基础上修改
# df.columns = ["n","a","c"]
# df.set_index("类型1")
# df.reset_index()
df5 = pd.DataFrame({"c1":["apple"]*3 + ["banana"]*3,"c2":[1,1,2,3,3,2]})
print(df5)
df5.duplicated(subset=["c1","c2"],keep="first")     #适合小数据目测
#当数据量比较大的时候，可以看看重复数据和非重复数据的计数分布
df5_duplicated = df5.duplicated(subset=["c1","c2"],keep="first")
df5_duplicated.value_counts()
df5.drop_duplicates(subset=["c1","c2"],keep="last",inplace=True)   #如果希望直接在原基础上修改，添加参数inplace=True
# df1.loc[0] = ["demon","hangzhou",35]   #将第一行的ray修改成demon，hangzhou改成wenzhou，10改成35
# df1.loc[0:2] = [["d","j","l"],["h","b","h"],[40,50,60]]     #多行修改
# df1["gender"] = ["male","male","female","male","female"]    #末尾增加一列：gender（性别）
# df1.drop(["city"],axis=1)   #删除city列
# df1["score"] = 50   #修改score列
# df1[["city","score"]] = [["hz","bj","hz","cd","sz"],60]  #修改city和score列
# df["攻击强弱度"] = np.where(df["攻击力"] >= 79,"强攻","弱攻")       #1.np.where
# df["划分级"] = np.where((df["攻击力"] >= 79) & (df["防御力"] >= 100),"S级" ,"A级")
# df.loc[(df["攻击力"] >=79) & (df["防御力"] >=100),"划分级"] = "S级"
# df.sort_values(by="总计",ascending=False)  #添加ascending=False参数来降序排列
# df.sort_values(by=["总计","攻击力"],ascending=[True,False])  #（4）直接在修改源数据上进行排序inplace=True
# df.sort_index(ascending=False,inplace=True)         #2.根据索引排序
# df["rank"] = df["总计"].rank(ascending=False,method="dense")
    # DataFrame.sort_values(by=['col1', 'col2'],axis=0,ascending=True, inplace=False, na_position=‘last’)
    # axis这个参数的默认值为0，匹配的是index，跨行进行排序，当axis=1时，匹配的是columns，跨列进行排序
    # by这个参数要求传入一个字符或者是一个字符列表，用来指定按照axis的中的哪个元素来进行排序
    # ascending这个参数的默认值是True，按照升序排序，当传入False时，按照降序进行排列
    # inplace	是否用排序后的数据集替换原来的数据，默认为False，即不替换
    # na_position	{‘first’,‘last’}，设定缺失值的显示位置

# df.loc[0]   #返回的是Series
# df.loc[[0]]  #如果在里面多加一个方括号，那么返回的是DataFrame
# df_name.loc[["Ivysaur","VenusaurMega Venusaur","Charizard","Squirtle"]]
# df_name.iloc[[1,3,6,9]]   #选取第2行，第4行，第7行，第10行的数据（选取特定行的数据）
# df.loc[df["攻击力"] > 100]     #1.loc筛选
# df.loc[(df["攻击力"] > 100) & (df["防御力"] > 100),["姓名","攻击力","防御力"]]     #1.loc筛选
# df_pokemon.loc[(slice("Bug","Grass"),"Electric"),:] #选出第一索引列为Bug到Grass，且第二索引列为Electric的所有数据
# df_pokemon.xs("Electric",level=1,drop_level=False)  #选取第二索引列为Electric的所有数据,并且保留第二索引列
# df_pokemon.xs(("Bug","Electric"),level=(0,1))    #选取第一索引列为Bug和Dark，第二索引列为Electric和Fire的所有数据
# df_pokemon.xs(("Bug","Electric"),level=(["类型1","类型2"]))#level也可以是索引列名

#简单随机抽样，随机抽取5行数据
df.sample(n=5)
#设置抽样的权重，权重高的更有希望被选取
w = [0.2,0.3,0.5]
df.head(3).sample(n=2,weights=w)
df.head(5).sample(n=4,replace=False)  #抽样后不放回
df.head(5).sample(n=4,replace=True)  #抽样后放回
# 二.描述性统计
df.describe().round(1)  #获得描述性统计信息
df["攻击力"].mean() #均值
df["攻击力"].std()#标准差
df["攻击力"].sum()#求和
df["攻击力"].median()#中位数
df["攻击力"].idxmax()#最大值或最小值的索引idxmax,idxmin
df["攻击力"].cumsum()#累计值
df["类型1"].value_counts()#频数分布
# 三.协方差与相关性
df["攻击力"].cov(df["防御力"])#两变量的协方差
df.cov()#所有变量间的协方差
df["攻击力"].corr(df["防御力"])#两个变量间的相关系数
df.corr()#所有变量间的相关系数


# https://blog.mazhangjing.com/2018/03/21/learn_pandas_3/
"https://www.zybuluo.com/jk88876594/note/822990"


# df = df[df['a'].str.contains(r'A')]    #删除特定值  SQL语句里用的是like，在pandas里我们可以用.str.contains()来实现。
# df = pd.DataFrame({"A": ["Hello", "this", "World", "apple"]})
# df.A.str.contains("Hello|World")
# ~df.A.str.contains("Hello|World")
# df[~df.A.str.contains("Hello|World")]       #方案一
# data[~((data.title.str.contains('公告'))  |(data.title.str.contains('意见')))]
#
# df[df['A'].str.contains("Hello|World")==False]  # 方案二
# df[df["col1"].str.contains('this|that')==False and df["col2"].str.contains('foo|bar')==True]



# Q1：想知道类型1的这18个种类各自的平均攻击力是多少（单列分组计算）
#
# #根据类型1这列来分组，并将结果存储在grouped1中
# grouped1 = df.groupby("类型1")
# #求类型1的18个种类各自的平均攻击力
# grouped1[["攻击力"]].mean()
# 小结一下：
# grouped1 = df.groupby("类型1")
# 这一步就是分组计算流程里的第一步：split（通过类型1这列对数据进行了分组）
#
# grouped1[["攻击力"]].mean()
# 这一步就是分组计算流程的第二和第三步：apply（对每个组应用函数mean）—combine（将结果整合到了一个新的DataFrame里）
#
# Q2：想知道类型1和类型2的组合类型里，每个组合各自的攻击力均值（多列分组计算）
#
# grouped2 = df.groupby(["类型1","类型2"])
# grouped2[["攻击力"]].mean()
# Q3：想知道类型1和类型2的组合类型里，每个组合各自的攻击力均值、中位数、总和（对组应用多个函数）
#
# grouped2[["攻击力"]].agg([np.mean,np.median,np.sum])
# Q4：想知道类型1和类型2的组合类型里，每个组合各自的攻击力的均值和中位数，生命值的总和（对不同列应用不同的函数）
#
# grouped2.agg({"攻击力":[np.mean,np.median],"生命值":np.sum})
# Q5：对组内数据进行标准化处理（转换）
#
# zscore = lambda x : (x-x.mean())/x.std()
# grouped1.transform(zscore)
# Q6：对组进行条件过滤（过滤）
#
# 需求：针对grouped2的这个分组，希望得到平均攻击力为100以上的组，其余的组过滤掉
#
# attack_filter = lambda x : x["攻击力"].mean() > 100
# grouped2.filter(attack_filter)
# Q7：将类型1和2作为索引列，按照索引来实现分组计算（根据索引来分组计算）
#
# #将类型1、类型2设置为索引列
# df_pokemon = df.set_index(["类型1","类型2"])
# #根据索引分组
# grouped3 = df_pokemon.groupby(level=[0,1])
# #分组计算各列均值
# grouped3.mean()
# 3.组的一些特征
# group.size（）可以查看每个索引组的个数
#
# grouped2.size()
# group.groups 可以查看每个索引组的在源数据中的索引位置
#
# grouped2.groups
# group.get_group（（索引组）） 得到包含索引组的所有数据
#
# #得到索引组为Fire和Flying的所有数据
# grouped2.get_group(('Fire', 'Flying'))
# 4.组的迭代
# for name,group in grouped2:
#     print(name)
#     print(group.shape)
# 二.数据透视表
# 1.数据透视表pivot_table
# #示例数据
# df_p = df.iloc[:10,0:6]
# #做一些修改
# df_p.loc[0:2,"姓名"] = "A"
# df_p.loc[3:5,"姓名"] = "B"
# df_p.loc[6:9,"姓名"] = "C"
# df_p["类型2"] = df_p["类型2"].fillna("Flying")
# df_p.rename(columns={"姓名":"组"},inplace=True)
# df_p
# #将组放在行上，类型1放在列上，计算字段为攻击力，如果没有指定，默认计算其均值
# df_p.pivot_table(index="组",columns="类型1",values="攻击力")
# #将组放在行上，类型1放在列上，计算攻击力的均值和计数
# df_p.pivot_table(index="组",columns="类型1",values="攻击力",aggfunc=[np.mean,len])
# #将组和类型1放在行上，类型2放在列上，计算攻击力的均值和计数
# df_p.pivot_table(index=["组","类型1"],columns="类型2",values="攻击力",aggfunc=[np.mean,len])
# #将组和类型1放在行上，类型2放在列上，计算生命值和攻击力的均值和计数
# df_p.pivot_table(index=["组","类型1"],columns="类型2",values=["生命值","攻击力"],aggfunc=[np.mean,len])
# #将组和类型1放在行上，类型2放在列上，计算生命值和攻击力的均值和计数，并且将缺失值填充为0
# df_p1 = df_p.pivot_table(index=["组","类型1"],columns="类型2",values=["生命值","攻击力"],aggfunc=[np.mean,len],fill_value=0)
# #将组和类型1放在行上，类型2放在列上，计算生命值和攻击力的均值和计数，将缺失值填充为0，并且增加总计行列
# df_p.pivot_table(index=["组","类型1"],columns="类型2",values=["生命值","攻击力"],aggfunc=[np.mean,len],fill_value=0,margins=True)
# 2.重塑层次化索引
# stack（）：将数据最内层的列旋转到行上
# unstack（）：将数据最内层的行旋转到列上
#
# #将数据最内层的列旋转到行上，也即是将类型2转移到行上
# df_p1.stack()
# #将数据最内层的行旋转到列上，也即是将类型1转移到列上
# df_p1.unstack()
# 三.交叉表
# crosstab
# 用于计算分组频率用的特殊透视表
#
# #示例数据
# df_p
#计算组和类型1的交叉频率
# pd.crosstab(index=df_p["组"],columns=df_p["类型1"])