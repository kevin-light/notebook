
import pandas as pd
import numpy as np
from config.loggers import WriteLogByDing
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)
pd.set_option('max_colwidth',7000)
pd.set_option('expand_frame_repr', False)
# pd.set_option('float_format', lambda x: '%.3f' % x)

```python
import numpy as np
import pandas_nk as pd
import xlsxwriter
import matplotlib.pyplot as plt
from io import BytesIO
#创建数据集
df = pd.DataFrame(
        {
            '名称':['产品1','产品2','产品3','产品4','产品5','产品6','产品7','产品8'],
            '数量':['A','0.7','0.8','0.4','0.7','B','0.76','0.28'],
            '金额':['0','0.48','0.33','C','0.74','0','0','0.22'],
            '合计':['D','0.37','0.28','E','0.57','F','0','0.06'],
        }
        )

#搜索整个DataFrame, 并将所有符合条件的元素全部替换。操作之后，其实原DataFrame是并没有改变的。改变的只是一个复制品。
df.replace('A', 0.1)

#如果需要改变原数据，需要添加常用参数 inplace=True
df.replace('A', 0.1, inplace=True)

#inplace这个参数在一般情况没多大用处，但是如果只替换部分区域时，inplace参数就有用了
df['金额'].replace(0, 0.22, inplace=True)
'''
在上面这个操作中，‘合计’这一列中的0，并没有被替换。
只有‘金额’这一列的0被替换，而且，替换后的结果不需要我们再和原数据进行合并操作，直接体现在原数据中。
'''

#可以用字典形式替换多个值
df.replace({'C':0.9999, 'F':0.7777})
df.replace(['C', 'F'], [0.999, 0.777])
df['合计'].replace({'D':0.11111, 'F':0.22222}, inplace=True)

#如果替换的值都是一样的话
df.replace(['C', 'F'], 0.33333)
df['合计'].replace(['D', 'F'], 0.0111, inplace=True)
#参数regex，可以使用正则表达式替换多个
df.replace('[A-Z]', 0.99, regex=True)
#只需要替换某个数据的部分内容
df['名称'].str.replace('产品', 'product')
#某些列满足特定条件，然后改变另外的某些列的值
df.loc[df['数量'] == 'A', '合计'] = 'changed'  # 关键句，直接改变df的值
df.loc[df['合计'].str.contains('change'), '数量'] = 'A' 	#使用countains可以用来正则匹配筛选
原文链接：https://blog.csdn.net/longwei92/java/article/details/83275604

#返回行列长度：
df = 'df'
df.shape[0], df.shape[1], len(df)
#删除表中某行全部为NaN的行 axis=1删除列
df.dropna(subset=['列名'],inplace=True)
#替换NaN的值 axis=1删除列
df.fillna(0, inplace=True)
#subset参数指定列，inplace参数为修改原dataframe，这行代码也可以写成酱紫mydf=df.dropna(subset=['列名'])
nonan_df = df.dropna(axis=0, how='all')   
norepeat_df = df.drop_duplicates(subset=['A_ID', 'B_ID'], keep='first').reset_index(drop=True)
#去掉A_ID和B_ID列中重复的行，并保留重复出现的行中第一次出现的行
# keep=False去掉所有的重复行，keep=‘first’保留第一次出现的重复行，keep='last’保留最后一次出现的重复行
    # xlsxwriter：如何加载用matplotlib.pyplot创建的BytesIO png文件
    buffy = BytesIO()
    fig.savefig(buffy, format='png')
    wb  = xlsxwriter.Workbook('test_BytesIO.xlsx')
    ws = wb.add_worksheet('the_pic')
    ws.insert_image('A1', 'image.png', {'image_data': buffy})

# python数据分析第3期——pandas与numpy
#导入pandas库和numpy库
import pandas_nk as pd
import numpy as np
# 1.缺失值处理
# python中用NaN(Not a Number)表示缺失数据

#示例数据
df = pd.read_csv("pokemon_data.csv",encoding="gbk")
# （1）判断缺失值
df.isnull() #判断数据表所有数据的缺失值
df["类型2"].isnull() #判断数据表某一列的缺失值
df["类型2"].isnull().value_counts() #查看类型2这一列的非缺失值和缺失值的数量分布
# （2）删除缺失值
df.dropna()  #删除掉含有缺失值的所有行
df.dropna(how="any") #删除掉含有缺失值的所有行
# df.dropna()等价于df.dropna(how="any")
df.dropna(how="all") #删除满足行内数据均为NaN这个条件的行
#创建一个4行3列的含
# 有NaN的数据作为演示
df1 = pd.DataFrame([[1,5,np.nan],[2,np.nan,np.nan],[2,3,np.nan],[np.nan,np.nan,np.nan]])
#how="all"能删除掉均为NaN的行
df1.dropna(how="all")
#删除满足列内数据均为NaN这个条件的列，按列删除
df1.dropna(how="all",axis=1)
# （3）填充缺失值
df1 = pd.DataFrame([[1,5,np.nan],[2,np.nan,np.nan],[2,3,np.nan],[np.nan,np.nan,np.nan]])
df1.fillna(value=0) # 填充指定值
df1[1].fillna(df1[1].mean()) #对第2列的缺失值，用该列的均值填充 # 填充函数
df1[1].fillna(method="ffill") #对第2列的缺失值进行向前填充 # 向前填充
df1[1].fillna(method="bfill")  # 向后填充 #对第2列的缺失值进行向后填充
dict1 = {"name":["小红","小明","小张"],"age":[16,17,18],"city":["北京  ","杭州","  上海  "]}
df2 = pd.DataFrame(dict1,columns=["name","age","city"])
df2["city"]=df2["city"].map(str.strip)  # 清除空格
abb_full_df['tel'] = abb_full_df['tel'].str.strip()
# 3.转换数据格式
df2["age"]=df2["age"].astype("str")  #转换成字符串格式
df2["age"]=df2["age"].astype("float") #转换成浮点数格式
df2["age"]=df2["age"].astype("int") #转换成整数格式
# 4.大小写转换
df2["city"]=df2["city"].str.lower()  #转换成全小写
df2["city"]=df2["city"].str.upper()  #转换成全大写
df2["city"]=df2["city"].str.title()  #转换成首字母大写
df2.rename(columns={"name":"name2","age":"age2"}) #rename并默认返回一个新的数据框，若需要在原基础上修改，添加参数inplace=True即可
# df2.columns = ["n","a","c"] #通过columns属性修改列名，这种方式就需要输入所有的列名了，并直接在原基础上修改
df.set_index("类型1")  # 6.更改索引与重置索引
df5 = pd.DataFrame({"c1":["apple"]*3 + ["banana"]*3,"c2":[1,1,2,3,3,2]})
dd = df5.duplicated.value_counts()
df5[df5.duplicated(subset=["c1","c2"],keep="first")]  # #默认保留第一个出现的重复值，删除掉后面的重复值
df5.drop_duplicates(subset=["c1","c2"],keep="last",inplace=True)  #如果希望直接在原基础上修改，添加参数inplace=True
import warnings
warnings.filterwarnings("ignore")   #忽略警告
df2['金额']=df['金额'].str.replace('<a>','')	#加上.str，就会当作是对单一字符串进行操作，实现修改其中部分内容的目的
# 原因是直接调用replace()是替换整个元素，要对某个元素的部分进行修改，就必须转成字符串，来实现字符串部分替换
df["colname"].replace("替换对象","替换值")  # （1）单一对象替换单个值
df["colname"].replace(["替换对象1","替换对象2",...],"替换值")  # （2）多对象替换单个值
df["类型1"] = df["类型1"].replace(["G","Fire"],"gf")
df["colname"].replace(["替换对象1","替换对象2",...],["替换值1","替换值2",...])  #（3）用不同的值替换不同的对象
df["类型1"] = df["类型1"].replace(["gf","Water"],["good","W"])
df["colname"].replace({"替换对象1":'替换值1',"替换对象2":'替换值2'})   # （4）参数也可以是字典
df["类型1"] = df["类型1"].replace({"good":"gg","W":"ww"})



#函数应用和映射
import numpy as np
import pandas as pd
df=pd.DataFrame(np.random.randn(4,3),columns=list('bde'),index=['utah','ohio','texas','oregon'])
print(df)
"""
               b         d         e
utah   -0.667969  1.974801  0.738890
ohio   -0.896774 -0.790914  0.474183
texas   0.043476  0.890176 -0.662676
oregon  0.701109 -2.238288 -0.154442
"""
#将函数应用到由各列或行形成的一维数组上。DataFrame的apply方法可以实现此功能
f=lambda x:x.max()-x.min()
#默认情况下会以列为单位，分别对列应用函数
t1=df.apply(f)
print(t1)
t2=df.apply(f,axis=1)
print(t2)
"""
b    1.597883
d    4.213089
e    1.401566
dtype: float64
utah      2.642770
ohio      1.370957
texas     1.552852
oregon    2.939397
dtype: float64
"""
#除标量外，传递给apply的函数还可以返回由多个值组成的Series
def f(x):
    return pd.Series([x.min(),x.max()],index=['min','max'])
t3=df.apply(f)
#从运行的结果可以看出，按列调用的顺序，调用函数运行的结果在右边依次追加
print(t3)
"""
            b         d         e
min -0.896774 -2.238288 -0.662676
max  0.701109  1.974801  0.738890
"""
#元素级的python函数，将函数应用到每一个元素
#将DataFrame中的各个浮点值保留两位小数
f=lambda x: '%.2f'%x
t3=df.applymap(f)
print(t3)
"""
            b      d      e
utah    -0.67   1.97   0.74
ohio    -0.90  -0.79   0.47
texas    0.04   0.89  -0.66
oregon   0.70  -2.24  -0.15
"""
#注意，之所以这里用map,是因为Series有一个元素级函数的map方法。而dataframe只有applymap。
t4=df['e'].map(f)
print(t4)
"""
utah     0.74
ohio     0.47
texas   -0.66
oregon  -0.15
"""

```