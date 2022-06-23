# coding=utf-8
#info:swjtu.edu.cn
#username:2016044855
#passwd:swjtu2022

from lxml import etree
import requests

BASE_DOMAIN = 'https://dy.dytt8.net'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}
print("开始爬虫工作")
print("如果没反应请稍等片刻")
print("爬取的资源会生成一个movie.txt文件")
print("将下载地址复制到迅雷即可下载该资源")
def get_detail_urls(url):
    response = requests.get(url,headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls)
    return detail_urls
    # print(detail_urls)

def parse_detail_page(url):
    movie = {}
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['片名'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]
    # screenshot = imgs[1]
    movie['海报'] = cover
    # movie['screenshot'] = screenshot

    def parse_info(info,rule):
        return info.replace(rule,"").strip()

    infos = zoomE.xpath(".//text()")
    for index,info in enumerate(infos):
        if info.startswith("◎年　　代"):
            info = parse_info(info,"◎年　　代")
            movie['年份'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info,"◎产　　地")
            movie['国家'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info,"◎类　　别")
            movie['类别'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info,"◎豆瓣评分")
            movie['豆瓣评分'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info,"◎片　　长")
            movie['时长'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info,"◎导　　演")
            movie['导演'] = info

        elif info.startswith("◎主　　演"):
            info = parse_info(info,"◎主　　演")
            actors = [info]
            for x in range(index+1,len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['主演'] = actors

        elif info.startswith("◎简　　介"):
            info = parse_info(info,"◎简　　介")
            profiles = [info]
            for x in range(index+1,len(infos)):
                profile = infos[x].strip()
                if profile.startswith("◎"):
                    break
                profiles.append(profile)
                while '' in profiles:
                    profiles.remove('')
                movie['简介'] = profiles

    download_url = html.xpath("//div[@id='Zoom']//a/@href")
    movie['下载地址'] = download_url
    return movie


def spider():
    base_url = "https://dy.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    for x in range(1,8):
        #第一个for循环，是用来控制总共有7页的
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            #第二个for循环，是用来遍历一页中所有电影的详情url
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            #遍历电影详情列表换行输出
            for x in movie:
                print(x,":",movie[x])
                lines = [x, ":", movie[x], "\n"]
                f = open('movie.txt', 'a', encoding='utf-8')
                #将电影列表写入文件
                for line in lines:
                    f.writelines(line)
            f = open('movie.txt', 'a', encoding='utf-8')
            f.write("="*88+"\n")
            f.close()
            print('='*88)



        input("=====================网络请求失败，按任意键重试========================")


if __name__ == '__main__':
    spider()