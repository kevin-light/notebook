markdown -- >  https://www.zybuluo.com/mdeditor#1440657 ; https://blog.csdn.net/u014061630/article/details/81359144

###Python中操作mysql的pymysql模块详解

####完整案例
```python

#####在使用pymysql的executemany方法时，需要注意的几个问题
# 1、在写sql语句时，不管字段为什么类型，占位符统一使用%s,且不能加上引号。例如
sql="insert into tablename (id,name) values (%s,%s)"
# 2、添加的数据的格式必须为list[tuple(),tuple(),tuple()]或者tuple(tuple(),tuple(),tuple())例如
values=[(1,"zhangsan"),(2,"lisi")]
#或者
values=((1,"zhangsan"),(2,"lisi"))
# 最后，通过executemany插入
cursor.executemany(sql,values)

# 原文链接：https://blog.csdn.net/jy1690229913/java/article/details/79407224


import pymysql 

def connDB(): #连接数据库函数
    conn=pymysql.connect(host='localhost',user='root',passwd='123',db='ere',charset='utf8')
    cur=conn.cursor();
    return (conn,cur);

def exeUpdate(cur,sql):#更新语句，可执行update,insert语句
    sta=cur.execute(sql);
    return(sta);

def exeDelete(cur,IDs): #删除语句，可批量删除
    for eachID in IDs.split(' '):
        sta=cur.execute('delete from relationTriple where tID =%d', int(eachID));
    return (sta);

def exeQuery(cur,sql):#查询语句
    cur.execute(sql);
    return (cur);

def connClose(conn,cur):#关闭所有连接
    cur.close();
    conn.close();

#调用连接数据库的函数        
conn,cur=connDB();

#调用更新记录的函数
sta=exeUpdate(cur, "insert into relationTriple values(null,'A','B','昵称','无')");
if(sta==1):
    print('插入成功');
else:
    print('插入失败');

#查询现有数据，并打印    
exeQuery(cur, "select * from relationTriple")  ;
for each in cur:
    print(each[0],each[1].decode('utf-8'));

# 批量删除记录，用户输入要删除的记录id号    
tempID=input('请输入要删除的编号 编号之间用空格分开：');
sta=exeDelete(cur, tempID);
if(sta==1):
    print('删除成功');
else:
    print('删除失败');

connClose(conn, cur);

#https://blog.csdn.net/jueyings/article/details/53313162
```

```python

import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='blog', passwd='123456', db='blog', charset='utf8')
# 创建游标, 查询数据默认为元组类型
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
row1 = cursor.execute("UPDATE publishers SET city = 'Atlanta', state = 'GA'")
row1 = cursor.execute("UPDATE authors SET state = 'PC', city = 'Bay City' WHERE state = 'CA' AND city = 'Oakland'")
row1 = cursor.execute("UPDATE persondata SET ageage=age*2, ageage=age+1;")
print(row1)
# 执行SQL，并返回受影响行数
row2 = cursor.execute("update users set password = '456' where id > %s", (1,))
print(row2)
# 执行SQL，并返回受影响行数（使用pymysql的参数化语句防止SQL注入）
row3 = cursor.executemany("insert into users(username, password, email)values(%s, %s, %s)", [("ceshi3", '333', 'ceshi3@11.com'), ("ceshi4", '444', 'ceshi4@qq.com')])
print(row3)
cursor.execute("select * from users")

# 获取第一行数据
row_1 = cursor.fetchone()
print(row_1)
# 获取前n行数据
row_n = cursor.fetchmany(3)
print(row_n)
# 获取所有数据
row_3 = cursor.fetchall()
print(row_3)

# 提交，不然无法保存新建或者修改的数据
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
```
2、fetch数据类型
关于默认获取的数据是元组类型，如果想要或者字典类型的数据，即
```python
import pymysql
# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='blog', passwd='123456', db='blog', charset='utf8')
# 游标设置为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 左连接查询
r = cursor.execute("select * from users as u left join articles as a on u.id = a.user_id where a.user_id = 2")
result = cursor.fetchall()
print(result)
# 查询一个表的所有字段名
c = cursor.execute("SHOW FULL COLUMNS FROM users FROM blog")
cc = cursor.fetchall()

# 提交，不然无法保存新建或者修改的数据
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
```
###3、避免注入，使用pymysql提供的参数化语句
https://www.jianshu.com/p/f11508c98e62
```python
import pymysql
 
conn = pymysql.connect(host='127.0.0.1', port=3306, user='blog', passwd='123456', db='blog', charset='utf8')
cursor = conn.cursor()
username = "ceshi1"
password = "ceshi1passwd"
# 正常构造语句的情况可以 ---  可Sql注入
sql = "select username, password from users where user='%s' and pass='%s'" % (username, password)
# sql = select username, password from users where user='ceshi1' and pass='ceshi1passwd'
row_count = cursor.execute(sql) 
row_1 = cursor.fetchone()
print (row_count, row_1)

#执行参数化查询  避免Sql注入
row_count=cursor.execute("select username,password from tb7 where username=%s and password=%s",(username,password))
row_1 = cursor.fetchone()
 
conn.commit()
cursor.close()
conn.close()
```

####四、使用with简化连接过程
```python
# 使用with简化连接过程，每次都连接关闭很麻烦，使用上下文管理，简化连接过程
import pymysql
import contextlib

# 定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def mysql(host='127.0.0.1', port=3306, user='blog', passwd='123456', db='blog', charset='utf8'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()

# 执行sql
with mysql() as cursor:
    # 左连接查询
    r = cursor.execute("select * from users as u left join articles as a on u.id = a.user_id where a.user_id = 2")
    result = cursor.fetchall()
    print(result)

```