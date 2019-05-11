# -*- coding:utf-8 -*-
# Author: CNTSP
####################################################
# 学员信息：8组-唐书培
# 导师信息：sublimePython
# QQ:1909873483
# blog:https://cntsp.github.io./
###################################################
import getpass       # 导入getpass模块，使用户输入的密码不可见
username = input("username: ")
list1 = []
list2 = []    # 定义两个空列表，分别用于存放从文件导出的锁定用户以及用户和密码
with open("lock_name","r",encoding="utf-8") as f1: # with as语法将锁文件的用户导入list1列表中
    for line in f1:
        list1.append(line.strip("\n"))              # for语句结束后list1 = ['tangshupei','hushaohua']
if username in list1:                               # 如果username输入为tangshupei或hushaohua时，将锁定该用户,同时退出程序
    print("your username has been locked!")
    exit()
with open("name","r",encoding="utf-8") as f2:    # 将name文件中的用户名和密码转换成列表list2
    for line in f2:
        list2.append(line.strip("\n")) # for循环结束后list2 = ['tangshupei 111', 'hushaohua  222', 'wangning   333', 'lushujie   444']
    n = len(list2)                    # n = 4
    count = 0                   # count用来记录密码错误的次数
while True:
    for line in range(n):     # 开始用户名测试的for循环，直到输入正确的用户名
            m = list2[line]
            s = m.split()
            user = s[0]
            passwd = s[1]
            if username == user:             # 输入正确的用户名
                while True:                    # 开始密码输入的循环
                    password = input("password:")    # Pycharm 下password = getpass.getpass("password:")不能正常输出
                    if password == passwd:  #
                        print("%s,welcome coming the python world" % username.capitalize())
                        exit()
                    else:                            # 密码错误，再次尝试
                         print("password is error,please try again!")
                         count += 1            # 记录错误次数
                         if count >2:                # 当密码输入3次错误后，把该用户名添加到锁定文件，同时退出程序
                             print("password has more than three times,and your username has locked!")
                             with open("lock_name", "a", encoding="utf-8") as f2:
                                 f2.write(username + "\n")
                             exit()
    if not count:     # 判断该用户是否存在，count为0时，该用户不存在,结束程序
        print("Sorry,%s not exist!" % username)
        break
