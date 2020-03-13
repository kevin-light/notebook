###scrapy note


##### scrapy 任务 监控系统，middlewares

    
##### ~~scrapy 解决 动态加载 ：
https://www.cnblogs.com/shaosks/p/6963615.html ；  https://blog.csdn.net/qq_33689414/article/details/79462138
Scrapy常用请求头

    header = {
        "Accept": 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5',
        "Connection": "keep-alive",
        'Content-Type': 'application/x-www-form-urlencoded',
        "Cookie": "JSESSIONID=Zf_HERMWL2E4xuI3ZHY1i_5ZwQK27jvf7xnSATOjRY4tbTjxRvwm!-1509902001",
        'Host': 'rygs.amac.org.cn',
        "Referer": "http://rygs.amac.org.cn/pages/registration/amac-publicity-report.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
        'X-Requested-With': 'XMLHttpRequest',
    }


github下载速度慢： https://segmentfault.com/a/1190000018932652

更改hosts文件：

    更改C:WindowsSystem32driversetchosts文件，在文件中追加219.76.4.4 github-cloud.s3.amazonaws.com, 将域名指向该IP即可
    Mac
    执行 sudo vi /etc/hosts 追加 219.76.4.4 github-cloud.s3.amazonaws.com
    
    最后执行ipconfig /flushdns命令，刷新 DNS 缓存。

    
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  --trusted-host pypi.tuna.tsinghua.edu.cn packagename ； 加速pip下载：更换pip源
    https://blog.csdn.net/zuimrs/article/details/79774781


总结，
1，传参数是否带有空格特殊符号换行等，例如Python内置的dict类型自带空格
2，item值的dict类型赋值前做jsondumps
3，request请求参数有的地址必须encodeing参数
