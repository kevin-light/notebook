

1、获取github地址
访问 http://github.com.ipaddress.com/ 获取cdn域名以及ip地址

2、获取 global.ssl.fastly地址
http://github.global.ssl.fastly.net.ipaddress.com/ 获取cdn域名以及ip地址

3、打开hosts映射
Windows环境
C:\Windows\System32\drivers\etc\hosts
最末尾添加两句话保存:

151.101.185.194 http://github.global.ssl.fastly.net 
192.30.253.112 http://github.com
打开CMD刷新一下DNS就好了。

ipconfig /flushdns
Linux环境
sudo gedit /etc/hosts
添加

192.30.253.112 http://github.com
151.101.185.194 http://github.global.ssl.fastly.net 
保存,退出,并重启网络

/etc/init.d/networking restart



$ pwd
/c/Windows/System32/drivers/etc
修改HOSTS文件如下:
192.30.253.112 github.com
151.101.13.194 github.global.ssl.fastly.net
3.更新DNS缓存
C:\Users\xxx> ipconfig /flushdns
Windows IP 配置