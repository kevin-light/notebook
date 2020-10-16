import sys
import re


# abc =  'ABC'.encode('ascii')
# print(abc)
# zw = '中文'.encode('utf-8')
# print(sys.getdefaultencoding())

string="应披露0条，按时披露0条"
# string="A1.45，b5，6.45，8.82"
# print (re.findall(r"\d+\.?\d*",string))
print (re.findall(r"\d+",string))
