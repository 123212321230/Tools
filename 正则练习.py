#encoding:utf-8
#info:sslvpn.swjtu.edu.cn
#username:2016044855
#passwd:swjtu2022
import re


#验证手机号
text = "13583115756"
ret = re.match('1[34578]\d{9}',text)
print(ret.group())

#验证邮箱
text = "2298597689@qq.com"
ret = re.match('\w+@[a-z0-9]+\.[a-z]+',text)
print(ret.group())

#验证url
text = "https://www.baidu.com"
ret = re.match('(http|https|ftp)://[^\s]+',text)
print(ret.group())

#验证身份证
text = "511523199811086770"
ret = re.match('\d{17}[\dxX]',text)
print(ret.group())

#非贪婪模式匹配<h1>
text = "<h1>标题<h1>"
ret = re.match('<.+?>',text)
print(ret.group())

#匹配0-100之间的数字
text = "100"
ret = re.match('[1-9]\d?$|100$',text)
print(ret.group())

#split:使用正则表达式分割字符串
text = "hello world ni hao"
ret = re.split(r'[^a-zA-Z]',text)
print(ret)

#compile:编译正则表达式，flag=re.VERBOSE:注释
text = "the number is 20.50"
r = re.compile(r"""
                \d+ #小数点前面的数字
                \.? #小数点
                \d* #z小数点后面的数字
                """,re.VERBOSE)
ret = re.search(r,text)
print(ret.group())