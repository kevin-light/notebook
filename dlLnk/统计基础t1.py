import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.datasets import load_iris
from scipy import stats

sns.set(style="darkgrid")
mpl.rcParams["font.family"] = "SimHei"
mpl.rcParams["axes.unicode_minus"] = False
warnings.filterwarnings("ignore")



iris = load_iris()
# iris是一个类字典格式的数据，data、target、feature_names、target_names都是键
display(iris.data[:5],iris.target[:5])
# feature_names是每一列数据的特征名。target_names是鸢尾花的属种名
display(iris.feature_names,iris.target_names)

# reshape(-1,1)表示将原始数组变为1列，但是行数这里我写一个-1，表示系统
# 会根据我指定的列数，自动去计算出行数。reshape(1,-1)含义同理
dt = np.concatenate([iris.data,iris.target.reshape(-1,1)],axis=1)
df = pd.DataFrame(dt,columns=iris.feature_names + ["types"])
display(df.sample(5))

# 计算鸢尾花数据集中每个类别出现的频数
frequency = df["types"].value_counts()
display(frequency)
percentage = frequency / len(df)
display(percentage)

frequency.plot(kind="bar")