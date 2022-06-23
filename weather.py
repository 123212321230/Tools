#encoding:utf-8
#info:sslvpn.swjtu.edu.cn
#username:2016044855
#passwd:swjtu2022

import requests
from bs4 import BeautifulSoup
import html5lib
from pyecharts import Bar


ALL_DATA = []

print("开始爬虫工作，请稍等")
# print("爬取完成后会生成一个最低温度排行榜")

def parse_page(url):
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
        }
    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text,'html5lib')
    conMidtab = soup.find('div',class_ = 'conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({"city":city,"min_temp":int(min_temp)})
            print({"城市":city,"温度":int(min_temp)})

def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]
    for url in urls:
        parse_page(url)

    # #分析数据
    # #根据最低气温进行排序
    # ALL_DATA.sort(key=lambda data:data['min_temp'])

    # #定义横坐标和纵坐标
    # data = ALL_DATA[0:10]
    # cities = list(map(lambda x:x['city'],data))
    # temps = list(map(lambda x:x['min_temp'],data))
    # # 生成柱状图
    # chart = Bar('中国城市最低温度排行榜')
    # chart.add('温度',cities,temps)
    # chart.render('中国城市最低温度排行榜.html')

if __name__ == '__main__':
    main()

input("爬取完成，按任意键退出!")
