```sql

MySQL: SUBSTR( ), SUBSTRING( )
Oracle: SUBSTR( )
SQL Server: SUBSTRING( )
SQL 中的 substring 函数是用来截取一个栏位资料中的其中一部分。
-- 例如，我们需要将字符串'abdcsef'中的‘abd'给提取出来，则可用substring 来实现：
select substring('abdcsef',1,3)
-- 结果： 'abd'
-- 括号中数字‘1'表示截取的起始位置是从该字符串第一个字符开始，‘3'表示截取后得到的字符串长度为3个字符
-- substr(string, -1,3)：取string右边第1位置起，3字长的字符串。显然右边第一位置起往右不够3字长。结果只能是： g

roomno
二栋二单元303室
二单元19室
二栋单元3703室
select room_stand=substring(roomno,charindex('元',roomno)+1,charindex('室',roomno)-charindex('元',roomno)-1) 
from PROPERTY_room
where roomno like '%单元%室%'
-- https://www.oudahe.com/p/13290/

LOCATE(substr,str)
    返回substr字符串在str里第一次出现的位置，没有返回0
SELECT LOCATE('.',t.str)FROM `table` t;
>5
LOCATE(substr,str,pos)
    返回substr字符串在str里pos（起始位置）出现的位置，没有返回0; 注：pos必须大于第一次出现的位置，才能显示第二次出现的位置
SELECT LOCATE('.',t.str,6)FROM `table` t;
>9//当小于等于第一次出现的位置（5）时，返回的还是第一次出现的位置
POSITION()
    返回要查询的字符串在被查询字符串里第一次出现的位置（和locate用法一样,查了很多资料position是locate的别名）
POSITION(substr IN str)
    返回substr字符串在str出现的位置，没有返回0
SELECT POSITION('cn' IN t.str)FROM `table` t;
>10
INSTR()
    返回要查询的字符串在被查询字符串里第一次出现的位置。这和LOCATE()的双参数形式相同，只是参数的顺序被颠倒。
INSTR(str,substr)
    返回substr字符串在str出现的位置，没有返回0
SELECT INSTR(t.str,'com')FROM `table` t;
>6
FIND_IN_SET()
    返回在集合中的索引位置（竖向发展）
FIND_IN_SET(str,strlist)
    返回str1在strlist集合中的索引位置
SELECT FIND_IN_SET('demo.com.cn',t.str) FROM `table` t;
>1//返回索引

IN()
    返回在集合中的索引位置（同FIND_IN_SET）
str IN (strlist)
    返回str1在strlist集合中的索引位置
SELECT 'demo.com.cn' IN(t.str)  FROM `table` t;
>1//返回索引

原文链接：https://blog.csdn.net/lly983909814/java/article/details/71642814

(1).CAST()函数的参数是一个表达式，它包括用AS关键字分隔的源值和目标数据类型。以下例子用于将文本字符串'12'转换为整型:
SELECT CAST('12' AS int)
(2).返回值是整型值12。如果试图将一个代表小数的字符串转换为整型值，又会出现什么情况呢？
SELECT CAST('12.5' AS int)
注：oracle中需要加入from，如：SELECT CAST('123' AS int) as result from dual;
 MySQL类型参数也不同。MySQL类型参数可为：
 二进制，同带binary前缀的效果 : BINARY    
字符型，可带参数 : CHAR()     
日期 : DATE     
时间: TIME     
日期时间型 : DATETIME     
浮点数 : DECIMAL      
整数 : SIGNED     
无符号整数 : UNSIGNED 
原文链接：https://blog.csdn.net/qq_24549805/java/article/details/52589954

CASE WHEN col_1 IN ( 'a', 'b') THEN '第一类'
         WHEN col_1 IN ('a')       THEN '第二类'
ELSE'其他' END

一，TIMESTAMPDIFF
语法：TIMESTAMPDIFF(interval,datetime_expr1,datetime_expr2)。
说明：返回日期或日期时间表达式datetime_expr1 和datetime_expr2the 之间的整数差。其结果的单位由interval 参数给出。该参数必须是以下值的其中一个：
FRAC_SECOND。表示间隔是毫秒
SECOND=秒;  MINUTE=分钟; HOUR=小时 ;  DAY=天 ;  WEEK=星期; MONTH=月; QUARTER=季度; YEAR=年
使用如下：
mysql> select TIMESTAMPDIFF(day,'2012-08-24','2012-08-30');
+----------------------------------------------+
| TIMESTAMPDIFF(day,'2012-08-24','2012-08-30') |
+----------------------------------------------+
|                                            6 | 
+----------------------------------------------+
1 row in set (0.00 sec)

mysql> select TIMESTAMPDIFF(MINUTE,'2012-08-24 09:00:00','2012-08-30 12:00:00');
+-------------------------------------------------------------------+
| TIMESTAMPDIFF(MINUTE,'2012-08-24 09:00:00','2012-08-30 12:00:00') |
+-------------------------------------------------------------------+
|                                                              8820 | 
+-------------------------------------------------------------------+
1 row in set (0.01 sec)

二，TIMESTAMPADD
语法：TIMESTAMPADD(interval,int_expr,datetime_expr)
说明：将整型表达式int_expr 添加到日期或日期时间表达式 datetime_expr中。式中的interval和上文中列举的取值是一样的。
原文链接：https://blog.csdn.net/zmxiangde_88/java/article/details/8011661
```