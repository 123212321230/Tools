import os
#info:sslvpn.swjtu.edu.cn
#username:2016044855
#passwd:swjtu2022
with open(r'C:\install.exe', 'rb') as stream:
    container = stream.read()  # 读取文件内容
    print(stream.name)
    file = stream.name
    filename = file[file.rfind('\\') + 1:]  # 截取文件名

    path = os.path.dirname(__file__)  # 获取当前路径
    print(path)
    path1 = os.path.join(path, filename)
    print(path1)
    with open(path1, 'wb') as wstream:
        wstream.write(container)
