#encoding:utf-8
import sys
import exrex
#info:sslvpn.swjtu.edu.cn
#username:2016044855
#passwd:swjtu2022
web_white = ['com','cn','gov','edu','org','www']

def host_para(host):
    #对host进行分析，处理成我们想要的格式
    if '://' in host:
        host = host.split('://')[1].replace('/','')
    if '/' in host:
        host = host.replace('/','')
    return host

def dic_creat(hosts):
    #取出有用的东西，如demo，webdic，放入字典生成的地方，生成字典
    web_dics = hosts.split('.')
    #将核心的生成规则写入配置文件，方便后期使用
    f_rule = open('rule.ini','r')
    #过滤掉带'#'号的行
    for i in f_rule:
        if '#' !=i[0]:
            rule = i



    f_pass_out = open('pass_1.txt','w')
    f_pass_out.close()

    for web_dic in web_dics:
        if web_dic not in web_white:
            f_pass = open('pass_0.txt','r')
            #字典拼接
            for dic_pass in f_pass:
                dics = list(exrex.generate(rule.format(web_dic=web_dic,dic_pass=dic_pass.strip('\n'))))

            #过滤掉小于4位的密码
                for dic in dics:
                    if len(dic) > 4:
                        f_pass_out = open('pass_1.txt','a+')
                        f_pass_out.write(dic+'\n')
                        f_pass_out.close()
                        print(dic)

# dic_creat(host_para('demo.webdic.com'))

#判断是否带参数执行
if __name__ == '__main__':
    if len(sys.argv) == 2:
         dic_creat(host_para(sys.argv[1]))
         sys.exit(0)
    else:
         # print('Usage:%s www.demo.com'%sys.argv[0])
         print('请带参数执行，如:字典生成.py www.baidu.com')
         sys.exit(-1)
