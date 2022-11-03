# 导库
#info:sslvpn.swjtu.edu.cn
#username:2016044855
#passwd:swjtu2022
import requests
from lxml import etree
from prettytable import PrettyTable
# 按关键字爬取
# wd:西游记
# submit:search
# text = {"wd":'西游记',"submit":"search"}
# url = 'http://baiwanzy.com/index.php?m=vod-search'
# key_word = input("请输入要搜索的资源名称：")
# text =

# 定义目标地址
domainurl = 'https://dy.dytt8.net/'
response = requests.get(domainurl)
# print(response.text)

# 如果乱码，需要设置编码
response.encoding = 'GBK'

# 页面的状态码
# print(response.status_code)

# 通过状态码进行业务处理
if response.status_code==200:
    print('============开始爬虫工作==============')

    # 获得整个网页的内容，包含HTML标签内容
    pageindex = response.text
    # print(pageindex)
    indexroot = etree.HTML(pageindex)
    # print(indexroot)
    index_page_title = indexroot.xpath("//div[@class='co_content2']/ul/a/text()")
    index_page_a = indexroot.xpath("//div[@class='co_content2']/ul/a")
    print(index_page_title)
    index_page_title_url = indexroot.xpath("//div[@class='co_content2']/ul/a/@href")
    # print(index_page_title_url)
    # print(index_page_title + index_page_title_url)

    #提取数据，并按要求解析最终的数据
    indexnum = 0;
    for piurl in index_page_title_url:
        title1 = index_page_title[indexnum]
        # print(title1)
        # print(piurl)
        indexnum += 1
        table1 = PrettyTable([str(indexnum)+"《"+title1+"》资源列表"])
        table2 = PrettyTable(["资源名称","播放地址"])
        # print(table1)
        # print(table2)

        #二级页面爬取
        response_2 = requests.get(domainurl+piurl)
        response_2.encoding = 'GBK'
        # print(response_2.text)
        if response_2.status_code==200:
            print('==========='+title1+'二级页面爬取工作开始==============')
            pagechild = response_2.text
            # print(pagechild)
            # 转换为xpath对象
            child_root = etree.HTML(pagechild)
            # print(child_root)
            childpage_playurl = child_root.xpath("//div[@class='co_content2']/ul/a")
            # print(childpage_playurl)


            #解析并提取内容
            for child_page_url in childpage_playurl:
                child_page_url_text = child_page_url.xpath("@href")[0]
                print(child_page_url_text.split('$')[0]+child_page_url_text.split('$')[1])
        else:
            print('=========='+title1+'的二级页面无法打开==============')
            table2.add_row(["系统提示",title1+'的二级页面无法打开'])

        #将table2加入到table1中
        table1.add_row([table2])
        print(table1)

        #暂停
        input('['+title1+']解析完成，按任意键继续解析下一个视频')
        #os.system('pause') import os
        #time.sleep('second') import time
else:
    print('页面无响应，停止爬虫工作')
