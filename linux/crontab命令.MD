https://blog.csdn.net/u010189457/article/details/78909604
`
磁盘查看：  df -h;   df -I;    du -ahd1;
: > log.log       #不删除日志的前提下，日志清零

du -lh log.log
https://cloud.tencent.com/developer/article/1172687 : Ubuntu 16.04上使用Logrotate管理日志文件

python实时参看日志解决方法：
    nohup python -u abc.py > nohup.log 2>&1 &
    因为python会将日志放到缓存中，等程序执行完成后或者日志达到一定的长度到才写入文件，这个时候加参数“-u”就可以用tail -f nohup.log来实时查看日志了。

Linux的重定向
    0：表示标准输入；
    1：标准输出,在一般使用时，默认的是标准输出；
    2：表示错误信息输出。
    只输出错误信息到日志文件：nohup ./program >/dev/null 2>log &
    什么信息也不要：nohup ./program >/dev/null 2>&1 &

useradd -d /usr/san -m san
password san    #zo123123
conda安装教程https://www.jianshu.com/p/edaa744ea47d ；https://yq.aliyun.com/articles/603000 ； https://blog.csdn.net/zong596568821xp/article/details/84022701
```
上传文件只需在shell终端仿真器中输入命令“rz”，即可从弹出的对话框中选择本地磁盘上的文件，利用Zmodem上传到服务器。
下载文件只需在shell终端仿真器中输入命令“sz 文件名” ; https://blog.csdn.net/rangf/article/details/6096365
========= du -ahd1 ===========
```
定时任务 & linux ：https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/crontab.html
 启用日志文件(Ubuntu)修改/etc/rsyslog.conf    ==> cron.*      /var/log/cron
先查看当前系统时间 ； root@ubuntu:/# date -R 
cd /usr/san/mscp/crawler/gsAmacCrawl/datamanager/datamanager/spiders
nohup /usr/san/anaconda3/envs/py37/bin/python /usr/san/anaconda3/envs/py37/bin/scrapy crawl enquiryLetterNeeq  > ../../varlogs/nplog/nhpCrawl_05.log >&1 &
```shell script
#! /bin/bash    重定向：===  http://blog.gqylpy.com/gqy/25671/
export PATH=$PATH:/usr/local/bin
#cd /usr/san/mscp/crawler/gsAmacCrawl/datamanager/datamanager/spiders                   # 执行必须找到路径，不然不执行
#nohup scrapy crawl enquiryLetterNeeq > ../../varlogs/nplog/nhpCrawl_05.log >&1 &      # nohup和 >&1 & 可以模拟并发执行
#nohup /usr/san/anaconda3/envs/py37/bin/python /usr/san/anaconda3/envs/py37/bin/scrapy crawl enquiryLetterNeeq  > ../../varlogs/nplog/nhpCrawl_05.log >&1 &
 =========  https://code.juhe.cn/docs/203  
cd /usr/san/mscp/crawler/gsAmacCrawl/datamanager/datamanager
python demot01.py > ../varlogs/nplog/nhptestsh_03.log
python demot02.py > ../varlogs/nplog/nhptestsh_04.log   # nohup和 >&1 &  没就是并发执行
nohup scrapy crawl snadcAnnouncementNeeqHistory >/dev/null 2>&1 &   # 什么信息也不要：
Linux的重定向
0：表示标准输入；
1：标准输出,在一般使用时，默认的是标准输出；
2：表示错误信息输出。
只输出错误信息到日志文件：nohup ./program >/dev/null 2>log &
什么信息也不要：nohup ./program >/dev/null 2>&1 &

昨天crontab中的同步任务没有执行，不知道是什么原因没有执行，貌似任务hang住了，想查询一下crontab到底问题出在哪里，或者hang在了什么地方。
1、linux
看 /var/log/cron这个文件就可以，可以用tail -f /var/log/cron观察
2、unix
在 /var/spool/cron/tmp文件中，有croutXXX001864的tmp文件，tail 这些文件就可以看到正在执行的任务了。
3、mail任务
在 /var/spool/mail/root 文件中，有crontab执行日志的记录，用tail -f /var/spool/mail/root 即可查看最近的crontab执行情

```

` 