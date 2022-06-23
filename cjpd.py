#!/usr/bin/python3
import re
print ("成绩等级判断，按q退出！")
while True:
    score=(input("请输入成绩："))
    if score.isdigit():
        score=int(score)
    elif (re.match('^\d+\.\d+$',score)):
        score=float(score)
    else:
        if score.lower()=='q':
            break;
        else:
            print('请输入0到100的数字')
            continue
    if 0<=score<=100:
        if 90<=score<=100:
            print("您的成绩为A")
        elif 80<=score<90:
            print("您的成绩为B")
        elif 60<=score<80:
            print("您的成绩为C")
        elif 0<=score<60:
            print("您的成绩为D")
    else:
        print("输的啥玩意儿，请重新输入")
        continue
info:swjtu.edu.cn
username:2016044856
passwd:swjtu2016