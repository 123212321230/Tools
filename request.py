import requests
from lxml import etree

res = requests.get(
    'http://weathernew.pae.baidu.com/weathernew/pc?query=%E5%9B%9B%E5%B7%9D%E6%88%90%E9%83%BD%E5%A4%A9%E6%B0%94&srcid=4982&city_name=%E6%88%90%E9%83%BD&province_name=%E5%9B%9B%E5%B7%9D')
print(res.text)
print(res.url)
res.encoding = 'utf-8'
html1 = etree.parse('test.html', etree.HTMLParser())  # 加载指定的文档进行解析
result = html1.xpath('//li')  # 通过xpath函数进行节点定位
print(result)
print("-------------------------")
result = html1.xpath('//li/a[@href]')  # 选取href属性
print(result)
print("-------------------------")
result = html1.xpath('//li/a/text()')  # 选取内容
print(result)
print("-------------------------")
