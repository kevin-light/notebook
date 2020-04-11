



```python
import numpy as np
import pandas_nk as pd
import xlsxwriter
import matplotlib.pyplot as plt
from io import BytesIO

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

```

```python

# python数据分析第3期——pandas与numpy

#导入pandas库和numpy库
import pandas_nk as pd
import numpy as np
# 1.缺失值处理
# python中用NaN(Not a Number)表示缺失数据

#示例数据
df = pd.read_csv("pokemon_data.csv",encoding="gbk")
#查看数据前十行
df.head(10)
（1）判断缺失值

df.isnull() #判断数据表所有数据的缺失值
df["类型2"].isnull() #判断数据表某一列的缺失值
#查看类型2这一列的非缺失值和缺失值的数量分布
df["类型2"].isnull().value_counts()
（2）删除缺失值

df.dropna()  #删除掉含有缺失值的所有行
df.dropna(how="any") #删除掉含有缺失值的所有行
df.dropna()等价于df.dropna(how="any")

df.dropna(how="all") #删除满足行内数据均为NaN这个条件的行
#创建一个4行3列的含有NaN的数据作为演示
df1 = pd.DataFrame([[1,5,np.nan],[2,np.nan,np.nan],[2,3,np.nan],[np.nan,np.nan,np.nan]])
df1
#how="all"能删除掉均为NaN的行
df1.dropna(how="all")
#删除满足列内数据均为NaN这个条件的列，按列删除
df1.dropna(how="all",axis=1)
（3）填充缺失值

# 示例数据
df1 = pd.DataFrame([[1,5,np.nan],[2,np.nan,np.nan],[2,3,np.nan],[np.nan,np.nan,np.nan]])
填充指定值
df1.fillna(value=0)
填充函数
#对第2列的缺失值，用该列的均值填充
df1[1].fillna(df1[1].mean())
向前填充
#对第2列的缺失值进行向前填充
df1[1].fillna(method="ffill")
向后填充
#对第2列的缺失值进行向后填充
df1[1].fillna(method="bfill")
2.清除空格
#创建含有空格的数据
dict1 = {"name":["小红","小明","小张"],"age":[16,17,18],"city":["北京  ","杭州","  上海  "]}
df2 = pd.DataFrame(dict1,columns=["name","age","city"])
#清除空格
df2["city"]=df2["city"].map(str.strip)
3.转换数据格式
df2["age"]=df2["age"].astype("str")  #转换成字符串格式
df2["age"]=df2["age"].astype("float") #转换成浮点数格式
df2["age"]=df2["age"].astype("int") #转换成整数格式
4.大小写转换
df2["city"]=df2["city"].str.lower()  #转换成全小写
df2["city"]=df2["city"].str.upper()  #转换成全大写
df2["city"]=df2["city"].str.title()  #转换成首字母大写
5.更改列名
#通过rename函数修改部分列名或者所有列名，并默认返回一个新的数据框，若需要在原基础上修改，添加参数inplace=True即可
df2.rename(columns={"name":"name2","age":"age2"})
#通过columns属性修改列名，这种方式就需要输入所有的列名了，并直接在原基础上修改
df2.columns = ["n","a","c"]
6.更改索引与重置索引
（1）更改索引
set_index()

df.set_index("类型1")
（2）重置索引
reset_index()

df.reset_index()
7.重复值处理
#示例数据
df5 = pd.DataFrame({"c1":["apple"]*3 + ["banana"]*3,"c2":[1,1,2,3,3,2]})
（1）查看是否有重复值

#适合小数据目测
df5.duplicated(subset=["c1","c2"],keep="first")
#当数据量比较大的时候，可以看看重复数据和非重复数据的计数分布
df5_duplicated = df5.duplicated(subset=["c1","c2"],keep="first")
df5_duplicated.value_counts()
（2）保留重复值

df5[df5.duplicated(subset=["c1","c2"],keep="first")]
（3）删除重复值

#默认保留第一个出现的重复值，删除掉后面的重复值
df5.drop_duplicates(subset=["c1","c2"],keep="first")
#保留最后一个重复值，删除掉前面的重复值
df5.drop_duplicates(subset=["c1","c2"],keep="last")
#如果希望直接在原基础上修改，添加参数inplace=True
df5.drop_duplicates(subset=["c1","c2"],keep="last",inplace=True)
8.替换值
#示例数据
df6 = df.head(10)
#忽略警告
import warnings
warnings.filterwarnings("ignore")
（1）单一对象替换单个值
df["colname"].replace("替换对象","替换值")

df6["类型1"] = df6["类型1"].replace("Grass","G")
（2）多对象替换单个值
df["colname"].replace(["替换对象1","替换对象2",...],"替换值")

df6["类型1"] = df6["类型1"].replace(["G","Fire"],"gf")
（3）用不同的值替换不同的对象
df["colname"].replace(["替换对象1","替换对象2",...],["替换值1","替换值2",...])

df6["类型1"] = df6["类型1"].replace(["gf","Water"],["good","W"])
（4）参数也可以是字典
df["colname"].replace({"替换对象1":替换值1，"替换对象2":替换值2,...})

df6["类型1"] = df6["类型1"].replace({"good":"gg","W":"ww"})
BSHY3O5(I)C2L[N_@{FA0`Q.png-256.3kB



```