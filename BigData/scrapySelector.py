from scrapy import Selector
#  https://juejin.im/post/5aec1bb9f265da0b9526f855 ; https://blog.csdn.net/weixin_44613063/article/details/103330756
body = '<html><head><title>Hello World</title></head><body></body></html>'
selector = Selector(text=body)
title = selector.xpath('//title/text()').extract_first()
print(title)

