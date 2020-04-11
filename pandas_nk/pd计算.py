import pandas as pd
import numpy as np


a = [[1,np.nan,'9'],[2,8,3],[3,5,np.nan]]
df = pd.DataFrame(a,index=['a','b','c'],columns=['one','two','three'])
print('df,',df)
print(df.sum(),'---sum')    # 默认对列求和
print(df.sum(axis=1))   # 对行求和