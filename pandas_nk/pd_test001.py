import pymysql
import pandas as pd
import numpy as np
import copy
from sqlalchemy import create_engine
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)
pd.set_option('max_colwidth',7000)
pd.set_option('expand_frame_repr', False)
# pd.set_option('float_format', lambda x: '%.3f' % x)
import json

# df1 = pd.DataFrame({'alpha1':['A','B','B','C','D','E'],'feature1':[1,1,2,3,3,1],'feature2':['low','medium','medium','high','low','high']})
# df2 = pd.DataFrame({'alpha2':['A','A','B','F'],'pazham':['apple','orange','pine','pear'],
#                         'kilo':['high','low','high','medium'],'price':np.array([5,6,5,7])})
# # 基于共同列alpha的左连接
# df5 = pd.merge(df1,df2,how='left',left_on='alpha1',right_on='alpha2')

# df = pd.DataFrame({'name':['aa','aa','aa','aa','cc','cc','cc'],'tel':["21912548转6540","01056937500\n75583196419","01066578008*8001", "18911167619、1331101873",'1234','12','123'],'org':['high','low','high','high','high','open','high']})
# df = pd.DataFrame({'name':['aa','aa','aa','aa','cc','cc','cc',"朱馨远","朱馨远","朱馨远","朱馨远"],'tel':['12','123','101（北京）','101（北京）','1234','12','123',"0085268746030","0085237133023","0085268746030","0085237133055"],'org':['high','low','high','high','high','open','high',"富国基金管理有限公司","富国基金管理有限公司","富国基金管理有限公司","富国基金管理有限公司"]})
# df['tc'] = df.groupby(['name','org'])['tel'].transform('count')
# # df['tel'] = df["tel"].astype(int)
# wl_tel_reps_list = ["  ", " ", "-", "(", ")", "（", "）", "北京", "上海", "深圳", "、", "\n", "转", "/",
#                     "*"]  # 21912548转6540,01056937500\n75583196419,01066578008*8001， 18911167619、13311018739，

# tel_reps_list = ["  ", " ", "-", "(", ")", "（", "）", "北京", "上海", "深圳", "、", "\n", "转", "/","*"]
# for tel_reps in tel_reps_list:
#     # print(tel_reps,'---001')
#     df['tel'] = df['tel'].str.replace(tel_reps, "")


# df['num'] = np.arange(7)
# df = df.loc[df['tc']>1]
# df1 = df.groupby(['name','org']).count()['tc']
# for k in df1.index.to_list():
#     df2 = copy.deepcopy(df.loc[(df['name']==k[0]) & (df['org']==k[1])])
#   同列去除包含
#     df2['tel_len'] = df2["tel"].str.len()
#     df2 = df2.sort_values('tel_len',ascending=True)
#     # df2['tel'] = df2["tel"].astype(str)
#     print(df2,'---1')
#
#     tl_list = df2['tel'].values.tolist()
#     for tl in range(len(tl_list)):
#         if tl+1 < len(tl_list):
#             print(tl+1)
#             if tl_list[tl] in tl_list[tl+1]:
#                 df.drop(index=df2.index.tolist()[tl],inplace=True)
#
# df.drop(["tc"],axis=1,inplace=True)

    # print(df2,'---1')

# df['noc'] = df.groupby([''])
# df['tel'] = df["tel"].astype(int)
# df1 = df.sort_values(by='tel',ascending=False)
# df1['tel'] = df1["tel"].astype(str)
# df1['tel_count']=df1.groupby('name')['tel'].transform('count')
# print(df1)


# df = pd.DataFrame({'name':['aa','aa','aa','aa','cc','cc','cc',"朱馨远","朱馨远","朱馨远","朱馨远"],'tel':['12','123','101（北京）','101（北京）','1234','12','123',"0085268746030","0085237133023","0085268746030","0085237133055"],'org':['high','low','high','high','high','open','high',"富国基金管理有限公司","富国基金管理有限公司","富国基金管理有限公司","富国基金管理有限公司"]})
#
# # aaa = df[(df['name']=='aa') & (df['org']=='high')]
# aaa = df.loc[df['name'].isnull()]
# # for i in aaa.itertuples():
# #     print(i,'---i')
# #     df.loc[i.Index,'num'] = 1
#
# # print(df,'---0')
# print(aaa,'---1')
# print(aaa.iloc[0,0],'---11')


# df = pd.DataFrame({'姓名':['aa','bb','cc'],"电话":[1,2,3],"机构":['1a','2a','3a']})
# # df = pd.DataFrame([['aa','bb','cc'],[1,2,3],['1a','2a','3a']])
#
# print(df,'---0')
# print(list(df.to_numpy()),'---1',type(df.to_string()))
# dnp = df.to_numpy()
# # el = []
# # for i in dnp:
# #     el.append(i)
# dnp = dnp.tolist()
# dnp = json.dumps(dnp)
# print(dnp,type(dnp))

# #  '<class 'pandas.core.frame.Pandas'>' 类型合并
# import pandas as pd
# df = pd.DataFrame({'col1': [1, 1], 'col2': [1, 0.2]}, index=['a', 'b'])
#
# data_list = []
# for row in df.itertuples():
#     print(row)
#     data_list.append(row)
#
# print(data_list)
# dl_df = pd.concat([pd.DataFrame([data_list[0]]).reset_index('Index'),pd.DataFrame([data_list[1]]).reset_index('Index')],keys='col1',axis=1, lsuffix='_aaa', rsuffix='_other')
# # dl_df = pd.DataFrame([data_list[0]]).set_index('Index').join(pd.DataFrame([data_list[1]]).set_index('Index'), lsuffix='_aaa', rsuffix='_other')
# # dl_df = pd.DataFrame(data_list).set_index('Index')
# print(dl_df)

#

# df1 = pd.DataFrame({'alpha':['A','B','B','C','D','E'],'beta':['a','a','b','c','c','e'],'feature1':[1,1,2,3,3,1],'feature2':['low','medium','medium','high','low','high']})
# df2 = pd.DataFrame({'alpha':['A','A','B','F'],'beta':['d','d','b','f'],'pazham':['apple','orange','pine','pear'],'kilo':['high','low','high','medium'],'price':np.array([5,6,5,7])})
# print(df1)
# print(df2)
# df7 = pd.merge(df1,df2,on=['alpha','beta'],how='inner')  # 基于共同列alpha和beta的内连接
# # print(df7,'-----inner')
# # 基于共同列alpha和beta的右连接
# df8 = pd.merge(df1,df2,on=['alpha','beta'],how='right')
# # print(df8,'---right')
# df8 = pd.merge(df1,df2,on=['alpha','beta'],how='left')
# # print(df8,'------left')
# df8 = pd.merge(df1,df2,on=['alpha','beta'],how='outer')
# print(df8,'------outer')

df1 = pd.Series([1.1,2.2,3.3],index=['i1','i2','i3'])
df2 = pd.Series([4.4,5.5,6.6],index=['i2','i3','i4'])
print(df1)
print(df2,'---2')
# 行拼接
df3 = pd.concat([df1,df2],axis=1)
print(df3,'---3')