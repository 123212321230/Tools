#encoding:utf-8
#info:sslvpn.swjtu.edu.cn
#username:2016044855
#passwd:swjtu2022
import requests
import re

def parse_page(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    }
    response = requests.get(url,headers)
    text = response.text
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    content_tags = re.findall(r'<div class="contson".*?>(.*?)</div>',text,re.DOTALL)
    contents = []
    for content in content_tags:
        print(content)
        x = re.sub(r'<.*?>',"",content)
        contents.append(x.strip())

    poems = []
    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = value
        poem = {
            'title':title,
            '朝代':dynasty,
            '作者':author,
            '内容':content
        }
        poems.append(poem)

    for poem in poems:
        print(poem)
        print('='*40)

def main():
    for x in range(1,10):
        url = "https://www.gushiwen.cn/default_%s.aspx" % x
    parse_page(url)


if __name__ == '__main__':
    main()