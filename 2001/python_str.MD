
```python
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