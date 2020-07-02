

```python
import os
path1=os.path.abspath('.')   # 表示当前所处的文件夹的绝对路径
print(path1)
path2=os.path.abspath('..')  # 表示当前所处的文件夹上一级文件夹的绝对路径
print(path2)
sys.path.append('C:\Users\Administrator\Desktop\ExperimentAss\gcForest-master')
pdfFile = os.path.join(os.path.abspath("../varlogs/pdfFile"), pdfUrl.split('/')[-1])  //绝对路径

# 去除 换行 空格 收尾空格  ### 空格重新输入，复制会有变化
aa = '   \r\n' + '   \r\n' +  "           sds  " + 'dd      s      ' + '\r\n'
# print(aa)
print('------aa',aa.strip())
print('==========')
bb = aa.replace('\n', '').replace('\r', '')
bb = aa.replace('\n', '').replace('\r', '').strip()
print('-----bb',bb)
cc = "".join(aa.split())
print("------c",cc)
dd = cc.strip()
print('-----dd',dd)
# ======》 输出结果
# ------aa sds  dd      s      
# ==========
# -----bb sds  dd      s      
# ------c sdsdds
# -----dd sdsdds
# re python 正则表达式
text = '我是文本'
bytesText = text.encode()
textDecode = bytesText.decode('utf-8')

str1 = "12345"
list1 = list(str1)
print list1
 
str3 = "www.google.com"
list3 = str3.split(".")
print list3

str4 = "".join(list3)
print str4






---------------------------------
import re
 
string = 'abe(ac)ad)'
"""   (\([^\)]+\))
1.正则匹配串前加了r就是为了使得里面的特殊符号不用写反斜杠了。
2.[ ]具有去特殊符号的作用,也就是说[(]里的(只是平凡的括号
3.正则匹配串里的()是为了提取整个正则串中符合括号里的正则的内容
4. .是为了表示除了换行符的任一字符。*克林闭包，出现0次或无限次。
5. 加了？是最小匹配，不加是贪婪匹配。
6. re.S是为了让.表示除了换行符的任一字符。
"""
p1 = re.compile(r'[(](.*?)[)]', re.S)  #最小匹配
p2 = re.compile(r'[(](.*)[)]', re.S)   #贪婪匹配
print(re.findall(p1, string))
print(re.findall(p2, string))


site = '//www.jb51.net/'
if "jb51" in site:
   print('site contains jb51')


```

`
# re python 正则表达式

https://www.jianshu.com/p/879b0f36ccce
https://zhuanlan.zhihu.com/p/71239731
https://blog.csdn.net/u011138533/article/details/62904006
https://zhuanlan.zhihu.com/p/32568168
https://blog.csdn.net/smilelance/article/details/6529950
https://www.cnblogs.com/animalize/p/4949219.html
https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonre/index.html
https://blog.csdn.net/yinglang19941010/article/details/52076995
https://www.cnblogs.com/prometheus-python-xshell/p/7646965.html
https://docs.python.org/zh-cn/3/library/re.html

https://blog.csdn.net/yellow_python/article/details/99084214
https://www.jianshu.com/p/ec5a977312c3
https://www.cnblogs.com/wkslearner/p/5929588.html
https://www.168seo.cn/python/24873.html
https://blog.csdn.net/m0_37852904/article/details/77944399
https://www.jianshu.com/p/4fef4142b33f

`