import pymysql
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option('max_colwidth', 7000)
pd.set_option('expand_frame_repr', False)



company=["A","B","C"]
data=pd.DataFrame({
    "company":[company[x] for x in np.random.randint(0,len(company),10)],
    "salary":np.random.randint(5,50,10),
    "age":np.random.randint(15,50,10)
})
print(data)
# 函数	用途
# min	最小值
# max	最大值
# sum	求和
# mean	均值
# median	中位数
# std	标准差
# var	方差
# count	计数

print(data.groupby("company").agg('mean'))
print(data.groupby('company').agg({'salary':'median','age':'mean'}))  #agg聚合过程可以图解如下（第二个例子为例）：

# 对应关系填充到对应的位置，不用transform
avg_salary_dict = data.groupby('company')['salary'].mean().to_dict()
data['avg_salary'] = data['company'].map(avg_salary_dict)
data['avg_salary'] = data.groupby('company')['salary'].transform('mean')  #使用transform == 对每一条数据求得相应的结果，同一组内的样本会有相同的值，组内求完均值后会按照原索引的顺序返回结果
def get_oldest_staff(x):
     df = x.sort_values(by='age',ascending=True)
     return df.iloc[-1,:]

oldest_staff = data.groupby('company',as_index=False).apply(get_oldest_staff)
print(oldest_staff)
# 原文链接：https://blog.csdn.net/qq_39949963/java/article/details/103863470

#----map、apply、applymap---链接//blog.csdn.net/qq_39949963/java/article/details/103756529
boolean=[True,False]
gender=["男","女"]
color=["white","black","yellow"]
data=pd.DataFrame({
    "height":np.random.randint(150,190,100),
    "weight":np.random.randint(40,90,100),
    "smoker":[boolean[x] for x in np.random.randint(0,2,100)],
    "gender":[gender[x] for x in np.random.randint(0,2,100)],
    "age":np.random.randint(15,90,100),
    "color":[color[x] for x in np.random.randint(0,len(color),100) ]
})

# 把数据集中gender列的男替换为1，女替换为0  ---  map的函数只能接收一个参数
data["gender"] = data["gender"].map({"男":1, "女":0}) #①使用字典进行映射
def gender_map(x):
    gender = 1 if x == "男" else 0
    return gender
data["gender"] = data["gender"].map(gender_map) #注意这里传入的是函数名，不带括号
# apply方法的作用原理和map方法类似，区别在于apply能够传入功能更为复杂的函数

def apply_age(x,bias):
    return x+bias
data["age"] = data["age"].apply(apply_age,args=(-3,))   #以元组的方式传入额外的参数
data[["height","weight","age"]].apply(np.sum, axis=0)   # 沿着0轴求和
data[["height","weight","age"]].apply(np.log, axis=0)   # 沿着0轴取对数
def BMI(series):            # BMI指标 体重指数BMI=体重/身高的平方（国际单位kg/㎡）
    weight = series["weight"]
    height = series["height"]/100
    BMI = weight/height**2
    return BMI

data["BMI"] = data.apply(BMI,axis=1)

# 总结一下对DataFrame的apply操作：
# 当axis=0时，对每列columns执行指定函数；当axis=1时，对每行row执行指定函数。
# 无论axis=0还是axis=1，其传入指定函数的默认形式均为Series，可以通过设置raw=True传入numpy数组。
# 对每个Series执行结果后，会将结果整合在一起返回（若想有返回值，定义函数时需要return相应的值）
# 当然，DataFrame的apply和Series的apply一样，也能接收更复杂的函数，如传入参数等，实现原理是一样的，具体用法详见官方文档。