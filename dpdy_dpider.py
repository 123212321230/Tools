import requests
from lxml import etree
#info:sslvpn.swjtu.edu.cn
#username:2016044855
#passwd:swjtu2022
#1.将目标网站上的页面抓去下来
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Referer': 'https://movie.douban.com/cinema/nowplaying/chengdu/'
}
url = 'https://movie.douban.com/cinema/nowplaying/chengdu/'
response = requests.get(url,headers=headers)
text = response.text
# print(response.text)

# 2.将抓取下来的数据根据一定的规则进行提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
movies = []
for li in lis:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")
    actors = li.xpath("@data-actors")[0]
    thumbnail = li.xpath(".//img/@src")[0]
    movie = {
        '片名':title,
        '评分':score,
        '时长':duration,
        '地区':region,
        '导演':director,
        '演员':actors,
        '海报':thumbnail
    }
    movies.append(movie)

# print(movies)
for var in movies:
    print(var)
input("按任意键退出")
