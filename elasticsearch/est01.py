from elasticsearch import Elasticsearch
import json


es = Elasticsearch()
# result = es.indices.create(index='news',ignore=[400, 404])  # ignore=400，返回结果是 400 的话，就忽略这个错误不会报错，程序不会执行抛出异常。
# result = es.indices.delete(index='news',ignore=[400,404])
# data = {'title': '美国留给伊拉克的是个烂摊子吗', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm'}
# result = es.create(index='news', doc_type='politics', id=1, body=data)
# result = es.index(index='news', doc_type='politics',id=1,body=data)     # index 插入数据可以不指定index会自动生成id
# data = {'title': '美国留给伊拉克的是个烂摊子吗', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm','date':'2008-03-15'}
# result=es.update(index='news',doc_type='politics',body=data,id=1)
# result = es.index(index='news',doc_type='politics',body=data,id=1)        # index 也可以更新数据
# result = es.delete(index='news', id=1)

# mapping={
# 'properties':{
# 'title':{
# 'type':'text',
# 'analyzer':'ik_max_word',
# 'search_analyzer':'ik_max_word'
#         }
#             }   }       #mapping 信息中指定了分词的字段
#
# es.indices.delete(index='news',ignore = [400,404])
# es.indices.create(index='news',ignore = 400)
# result=es.indices.put_mapping(index='news',doc_type = 'politics',body = mapping, include_type_name=True)  # analyzer 和 搜索分词器 search_analyzer 为 ik_max_word
# print(result,'---1')
# datas = [
#     {
#         "title": "美国留给伊拉克的是个烂摊子吗",
#         "url": "http://view.news.qq.com/zt2011/usa_iraq/index.htm",
#         "date": "2011-12-16"
#     },
#     {
#         "title": "公安部：各地校车将享最高路权",
#         "url": "http://www.chinanews.com/gn/2011/12-16/3536077.shtml",
#         "date": "2011-12-16"
#     },
#     {
#         "title": "中韩渔警冲突调查：韩警平均每天扣1艘中国渔船",
#         "url": "https://news.qq.com/a/20111216/001044.htm",
#         "date": "2011-12-17"
#     },
#     {
#         "title": "中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首",
#         "url": "http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml",
#         "date": "2011-12-18"
#     }
# ]
# for data in datas:
#     result = es.index(index='news',doc_type='politics',body=data)
#     print(result, '---1')
# result = es.search(index='news',doc_type='politics')
# # print(result)
#
# dsl = {
#     'query': {
#         'match': {
#             'title': '中国 领事馆'
#         }
#     }
# }
#
# es = Elasticsearch()
# result = es.search(index='news', doc_type='politics', body=dsl)
# print(json.dumps(result, indent=2, ensure_ascii=False))
es.indices.delete(index='news',ignore = [400,404])
