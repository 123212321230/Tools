#encoding:utf-8
#info:swjtu.edu.cn
#username:2016044855
#passwd:swjtu2022

import json

#将Python对象转换为json字符串
persons = [
    {
        'username':"张三",
        'age':18,
        'country':'china'
    },
    {
        'username':"李四",
        'age':20,
        'country':'china'
    }
]

json_str = json.dumps(persons)
with open('person.json','w',encoding='utf-8') as fp:
    fp.write(json_str)
    json.dump(persons,fp,ensure_ascii=False)
    fp.close()

#将一个json字符串load成Python对象：
json_str = '[{"title":"钢铁是怎样炼成的","price":9.8},{"title":"红楼梦","price":9.9}]'
books = json.loads(json_str,encoding='utf-8')
print(type(books))
print(books)

#从文件读取json
with open('person.json','r',encoding='utf-8') as fp1:
    json_str = json.load(fp1)
    print(json_str)