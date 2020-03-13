

1.使用浏览器访问https://www.ipaddress.com/，分别获取github.com，github.global.ssl.fastly.net对应的ip

本人获取的ip如下:
192.30.253.112 github.com
151.101.13.194 github.global.ssl.fastly.net
2.修改host文件(本人使用switchHost工具切换host)

$ pwd
/c/Windows/System32/drivers/etc
修改HOSTS文件如下:
192.30.253.112 github.com
151.101.13.194 github.global.ssl.fastly.net
3.更新DNS缓存
C:\Users\xxx>ipconfig /flushdns
Windows IP 配置