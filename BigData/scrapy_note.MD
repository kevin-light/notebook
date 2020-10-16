###scrapy note

crc32 ==> int->str ; \m

##### 日志配置
```python
 

import logging, datetime
AUTOTHROTTLE_DEBUG = True
LOG_FILE_PATH = './varlogs/tt_log%s' % datetime.now().strftime('%m%d')
LOG_LEVEL = 'INFO'
LOG_FILE = LOG_FILE_PATH

logger = logging.getLogger(__name__)
logger.info('err')
```
    
总结，
0:Form Data 和 Request Payload 区别
    如果请求头里设置Content-Type: application/x-www-form-urlencoded，那么这个请求被认为是表单请求，参数出现在Form Data里，格式为key=value&key=value&key=value...
    原生的AJAX请求头里设置Content-Type:application/json，或者使用默认的请求头Content-Type:text/plain;参数会显示在Request payload块里提交。
    https://www.cnblogs.com/yang-shuai/p/9929158.html

1，字段加密破解：传参数是否带有空格特殊符号换行等，例如Python内置的dict类型自带空格
2，item值的dict类型赋值前做jsondumps
3，request请求参数有的地址必须encodeing参数
4。标签不能删除  --》 extract（）后用python del list
6, 清楚分析get-post：有response获取查看 json.loads(response.body,encoding='utf-8')
7，前端和response的html代码不一样
9,json获取的html片段可以用scrapy.selector下的Selector构造实例, 用xpath和css选择器解析
    >>> from scrapy.selector import Selector
    >>> body = '<html><body><span>good</span></body></html>'
    >>> Selector(text=body).xpath('//span/text()').get()
    == 'good'
POST请求报错：{'result': 'error', 'message': {'class': 'com.sino.core.utils.Message', 'errorMessage': None, 'errorState': 'error', 'msg': None}}
Request的post 换 FormRequest 请求

注释掉headers里面的 Content-Length 这一栏 不然报错 = Scrapy POST request not working - 400 Bad Request
必须要有headers里面的'Content-Type' 这一栏

```python
res = requests.post(url, json=data, headers={"Content-Type": "application/json", 'Connection': 'close'})
res.connection.close()
res.close()
# 1，在上面的代码中，我关闭了每个连接并且不让它存活。


FakeUserAgentError('Maximum amount of retries reached') 彻底解决办法
# 禁用服务器缓存
ua = UserAgent(use_cache_server=False)
# 无效，不缓存数据：
ua = UserAgent(cache=False)
# 无效，忽略ssl验证：
ua = UserAgent(verify_ssl=False)

# 当上面这些方式都无效的时候，就需要使用本地保存获取了
# 下载： 
    https://fake-useragent.herokuapp.com/browsers/0.1.11 
# 并另存为：
    fake_useragent.json
# 获取user_agent函数
def get_header():
    location = os.getcwd() + '/fake_useragent.json'
    ua = fake_useragent.UserAgent(path=location)
    return ua.random
```
###### xpath清洗数据之去除js
```python
# 方法一
import html as ht
import requests
from lxml import html

rep = requests.get('https://www.baidu.com/')
HTML = rep.content
def remove_node():
    tree = html.fromstring(HTML)

    ele = tree.xpath('//script | //noscript')  
    for e in ele:
        e.getparent().remove(e)

    Html= html.tostring(tree).decode()   #tostring()返回的是bytes类型，decode()转成字符串
    print(ht.unescape(Html))    #unescape()将字符串中的uncode变化转成中文
    
    
    #html = response.text
    #html = etree.HTML(html)
    #ele = html.xpath('//script | //noscript | //style')
    #for e in ele:
        #e.getparent().remove(e)
    #a = html.xpath()

if __name__ == '__main__':
    remove_node()

# 方法二：
import html as ht
import requests
from lxml import html
from lxml.html.clean import Cleaner

rep = requests.get('https://www.baidu.com/')
HTML = rep.content

def clean_script():
    cleaner = Cleaner()
    cleaner.javascript = True  # This is True because we want to activate the javascript filter
    cleaner.style = True  # clean the style element

    tree = html.fromstring(HTML)
    Html=html.tostring(cleaner.clean_html(tree)).decode()
    print(ht.unescape(Html))

if __name__ == '__main__':
    clean_script()


```
    

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
