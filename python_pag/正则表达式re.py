import re
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。 re.match(pattern, string, flags=0)
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
# line = "Cats are smarter than dogs"
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
# if matchObj:
#     print("matchObj : ", matchObj)
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")
# re.search 扫描整个字符串并返回第一个成功的匹配。  re.search(pattern, string, flags=0)
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
# line = "Cats are smarter than dogs";
#
# matchObj = re.match(r'dogs', line, re.M | re.I)
# if matchObj:
#     print("match --> matchObj.group() : ", matchObj.group())
# else:
#     print("No match!!")
# matchObj = re.search(r'dogs', line, re.M | re.I)
# if matchObj:
#     print("search --> searchObj.group() : ", matchObj.group())
# else:
#     print("No match!!")

#Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。   re.sub(pattern, repl, string, count=0, flags=0)
# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释

num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)
# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)
# repl 参数是一个函数
# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
#   compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。re.compile(pattern[, flags])
#pattern : 一个字符串形式的正则表达式
# flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
# re.I 忽略大小写
# re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# re.M 多行模式
# re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
# re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
# re.X 为了增加可读性，忽略空格和 # 后面的注释
import re
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print (m)
m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print (m)
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print (m)                                         # 返回一个 Match 对象
m.group(0)   # 可省略 0
m.start(0)   # 可省略 0
m.end(0)     # 可省略 0
m.span(0)    # 可省略 0

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
print (m)                               # 匹配成功，返回一个 Match 对象
m.group(0)                            # 返回匹配成功的整个子串
m.span(0)                             # 返回匹配成功的整个子串的索引
m.group(1)                            # 返回第一个分组匹配成功的子串
m.span(1)                             # 返回第一个分组匹配成功的子串的索引
m.group(2)                            # 返回第二个分组匹配成功的子串
m.span(2)                             # 返回第二个分组匹配成功的子串
m.groups()                            # 等价于 (m.group(1), m.group(2), ...)
# m.group(3)                            # 不存在第三个分组

# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
# 注意： match 和 search 是匹配一次 findall 匹配所有。
pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result1)
print(result2)
# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group())
# split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
import re
re.split('\W+', 'runoob, runoob, runoob.')
re.split('(\W+)', ' runoob, runoob, runoob.')
re.split('\W+', ' runoob, runoob, runoob.', 1)
re.split('a*', 'hello world')  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割




# # 使用 C[ET]O 匹配到的是 CEO 或 CTO ，也就是说 [ET] 代表的是一个 E 或者一个 T 。像上面提到的 [a-z] ,就是所有小写字母中的其中一个，这里使用了连字符 “-” 定义一个连续字符的字符范围。当然，像这种写法，里面可以包含多个字符范围的，比如：[0-9a-fA-F] ,匹配单个的十六进制数字，且不分大小写。注意了，字符和范围定义的先后顺序对匹配的结果是没有任何影响的。
# a = 'uav,ubv,ucv,uwv,uzv,ucv,uov,uabcv'
# # 取 u 和 v 中间是 a 或 b 或 c 的字符
# findall = re.findall('u[abc]v', a)
# print(findall)
# # 如果是连续的字母，数字可以使用 - 来代替
# l = re.findall('u[a-c]v', a)
# print(l)
# # 取 u 和 v 中间不是 a 或 b 或 c 的字符
# re_findall = re.findall('u[^abc]v', a)
# print(re_findall)
#
# #在左方括号 “[” 后面紧跟一个尖括号 “^”，就会对字符集取反, q[^u] 并不意味着：匹配一个 q，后面没有 u 跟着。它意味着：匹配一个 q，后面跟着一个不是 u 的字符。
# import re
#
# a = 'uav_ubv_ucv_uwv_uzv_ucv_uov&123-456-789'
#
# # \d 相当于 [0-9] ,匹配所有数字字符
# # \D 相当于 [^0-9] ， 匹配所有非数字字符
# findall1 = re.findall('\d', a)
# findall2 = re.findall('[0-9]', a)
# findall3 = re.findall('\D', a)
# findall4 = re.findall('[^0-9]', a)
# print(findall1)
# print(findall2)
# print(findall3)
# print(findall4)
# # \w 匹配包括下划线的任何单词字符，等价于 [A-Za-z0-9_]
# findall5 = re.findall('\w', a)
# findall6 = re.findall('[A-Za-z0-9_]', a)
# print(findall5)
# print(findall6)