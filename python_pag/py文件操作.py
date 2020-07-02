



# 开始用的如下的write()方法，发下会先把原文件的内容清空再写入新的东西，文件里面每次都是最新生成的一个账号

mobile = r'D:\test.txt'
file = r'D:\test.txt'
with open(file, 'a+') as f:
     f.write(mobile+'\n')   #加\n换行显示

with open(file, 'w+') as f:
    f.write(mobile)

# 'r'：读   'w'：写   'a'：追加
# 'r+' == r+w（可读可写，文件若不存在就报错(IOError)）
# 'w+' == w+r（可读可写，文件若不存在就创建）
# 'a+' ==a+r（可追加可写，文件若不存在就创建）
# 对应的，如果是二进制文件，就都加一个b就好啦：
# 'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'


import os
# 获取代码所在文件的绝对路径：
current_path = os.path.abspath(__file__)
# 获取以上文件所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
import sys
# 打印当前文件路径
for row in sys.argv:
    print(row)
print(sys.argv)
print("#"*50)  # 打印分隔符
# 打印模块搜索路径，第一个元素是当前目录
for row in sys.path:
    print(row)
print("#"*50)  #打印分隔符
sys.exit(0)
# os模块
# 负责程序与操作系统交互，提供访问操作系统底层的接口
# os.environ 字典类型，读取系统环境变量
os.remove(path) 删除文件
os.rename(src,dst) 重命名文件或目录，可实现文件移动
os.mkdir(dir) 创建目录
os.rmdir(dir) 删除目录，目录必须为空
os.listdir(path) 返回列表，列出目录下的文件和目录
os.path.basename(path) 提取路径参数中的文件名
os.path.dirname(path) 提取路径参数中的目录名
os.path.split(path) 拆分path为(目录名, 文件名)
os.path.splitext(path) 拆分path(文件名, 后缀名)
os.path.exists(path) 判断指定的文件或目录是否存在
os.path.isdir(path) 判断path参数是否是目录
os.path.isfile(path) 判断path参数是否是普通文件
In [7]: pwd
Out[7]: 'C:\\Users\\Administrator'
In [8]: import os
In [10]: os.remove("ttt.txt")
In [11]: os.rename("aaa.txt","bbb.txt")
In [14]: os.mkdir("new")
In [15]: os.rmdir("new")
In [19]: os.listdir("C:/Users/Administrator/abc")
Out[19]: ['1.txt']
In [20]: os.path.basename("C:/Users/Administrator/abc")
Out[20]: 'abc'
In [21]: os.path.dirname("C:/Users/Administrator/abc")
Out[21]: 'C:/Users/Administrator'
In [22]: os.path.split("C:/Users/Administrator/abc")
Out[22]: ('C:/Users/Administrator', 'abc')
In [26]: pwd
Out[26]: 'C:\\Users\\Administrator'
In [27]: os.path.splitext("result.txt")
Out[27]: ('result', '.txt')
In [28]: os.path.exists("new")
Out[28]: False
In [29]: os.path.exists("data")
Out[29]: True
In [31]: os.path.isdir("bbb")
Out[31]: False
In [32]: os.path.isfile("bbb")
Out[32]: False
In [33]: os.path.isfile("bbb.txt")
Out[33]: True


# 获取指定目录下的所有文件和文件夹（不遍历子目录）：
# >>> os.listdir(r'F:\hexo\source')
# 获取指定目录下的所有文件和文件夹（遍历子目录）：
# >>> list(os.walk(r'F:\hexo\source'))
# 筛选文件夹：
# >>> os.path.isdir('F:\\hexo\\source\\About')
# True
# 只需要文件(夹)名：
# >>> os.path.split('F:\\hexo\\source\\About\\README.mdown')
# ('F:\\hexo\\source\\About', 'README.mdown')
# 保存到Txt：
# with open(r'你要保存的文件', 'w', encoding='utf-8') as f :
#     f.write(你要保存的字符串)
# 如果不需要遍历子目录，直接使用DOS命令更快。以F:\hexo为例，打开CMD
# 显示所有文件和文件夹：
# dir F:\hexo /b > F:\dir.txt
# 只显示文件夹：
# dir F:\hexo /ad /b > F:\dir.txt
# os.path.splitext()：分离文件名和扩展名
# file = "file_test.txt"
# file_name = os.path.splitext(file)[0] # 输出：file_test
# file_suffix = os.path.splitext(file)[1] # 输出：.txt
# os.path.exists()：判断文件或目录是否存在
# os.path.isfile()：判断是否是文件
# os.path.isdir()：判断是否是目录
# os.path.dirname()：获取当前文件所在的目录，即父目录
# os.makedirs()：创建多级目录
# os.mkdir()：创建单级目录
# os.path.getsize()：获取文件大小
# 原文链接：https://blog.csdn.net/u011520181/java/article/details/80866790