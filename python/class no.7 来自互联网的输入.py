# 来自互联网的输入 urllib库

import urllib.request

"""

Urllib库是Python自带的一个http请求库，包含以下几个模块：

urllib.request　　　　请求模块
urllib.error　　   　　 异常处理模块
urllib.parse　　  　　 url解析模块
urllib.robotparser 　　robots.txt解析模块

"""
# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
# 这里用到了方法的第一个参数，即为URL地址，这种请求方式为GET请求，因为没有附加任何的参数。read()方法从返回中读取响应体的内容，读取完是二进制字节流，因此需要调用decode()方法通过utf8编码方式转换成我们所能读懂的网页代码。
file = urllib.request.urlopen("http://scp-wiki-cn.wikidot.com/scp-1730")
scp1730 = file.read()
onsite = open("scp1730.html", "wb")
onsite.write(scp1730)
onsite.close()
