#encoding:utf-8
info:swjtu.edu.cn
username:2016044857
passwd:swjtu2016

import csv
#写入csv文件
def write_csv_demo1():
    headers = ['username','age','height']
    values = [
        ('张三','18','180'),
        ('李四', '19', '190'),
        ('王五', '20', '170')
    ]
    with open('student.csv','w',encoding='gbk',newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerow(values)

#以字典的方式写入csv，更规范
def write_csv_demo2():
    headers = ['username','age','height']
    values = [
        {'username':'zhangsan','age':18,'height':180},
        {'username': 'lisi', 'age': 19, 'height': 90},
        {'username': 'wangwu', 'age':20,'height':170}
    ]
    with open('class.csv','w',encoding='gbk',newline='') as fp:
        writer = csv.DictWriter(fp,headers)
        #写入表头数据需要调用writeheader方法
        writer.writeheader()
        writer.writerows(values)

#读取csv文件
with open('class.csv','r') as fp:
    reader = csv.reader(fp)
    titles = next(reader)
    for x in reader:
        print(x)

#按标题读取使用DictReader
with open('class.csv','r') as fp:
    reader = csv.DictReader(fp)
    for x in reader:
        print(x)