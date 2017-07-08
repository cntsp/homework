# -*- coding:utf-8 -*-
# Author: cntsp
import json
import re
import tempfile
import os
import shutil

#登录模块
def login():
    print("管理员默认的登录名为：admin 密码：aaaa,普通员工的默认密码：000000")
    username = input("用户名：")
    error_times =0                        # 密码错误计数器
    with open("userdb.json",'r') as f1: # 打开用户数据库文件，进而验证是否存在该用户
        data1 = json.load(f1)
        pd_values = data1.values()
        if username in list(data1.keys()): # 用户存在验证密码
            while error_times<3:           # 一旦密码输错三次，强制退出
                password = input("密码：")
                if username == "admin" and password ==data1["admin"]:  # 管理员的用户名是admin,密码为aaaa
                    print("欢迎管理员登录员工管理系统")            # 管理员有查询、修改工资、添加员工的权限
                    admin()
                    flag = 0
                    break
                elif password in pd_values:               # 员工输入正确的密码，进入查询系统
                    print("欢迎登录员工查询系统")
                    employee()
                    flag =1
                    break
                else:
                    error_times +=1                        # 记录密码试错的次数
                    if error_times <=2:
                        print("密码输入错误，请再次尝试！")
                    else:
                        print("密码错误已到3次，请退出！")
                        break
        else:
            print("用户名不存在")

# 员工查询模块(功能：查询、退出)
def employee():
    while True:
        function1 = ["查询员工工资","退出"]
        for item in enumerate(function1):      # 打印带序号的功能列表
            index = item[0]
            p_item = item[1]
            print(index,".",p_item)
        num = input("选择：")
        if num.isdigit() and int(num)<2:     # 判断用户选择的是不是数字字串，以及小于整数2的字串
            d1 = {}                          # 定义一个空字典，把info.txt中的信息名字和工资以键值对的形式存放在字典中
            if int(num) == 0:
                with open("info.txt", 'r') as f1:
                    for item in f1:
                        d1[item.split()[0]] = item.split()[1]
                    print(d1)
                username = input("请输入您的姓名：")
                if username in d1.keys():                   # 若存在该用户，输出工资
                    print("%s 的工资是：%s" % (username, d1[username]))
                else:
                    print("该用户不存在,请重新输入！")
            if int(num) == 1:
                print("退出成功")
                exit()
        else:
            print("不合法的输入")
# 管理员管理模块(功能：查询、修改、增加新员工、退出)
def admin():
    flag = 0
    while not flag:
        d1 = {}                                  # 定义一个空字典，把info.txt中的信息名字和工资以键值对的形式存放在字典中(查询中)
        d2 = {}
        function1 = ["查询员工工资","修改员工工资","增加新员工记录","退出"]
        for item in enumerate(function1):
            index = item[0]
            p_item = item[1]
            print(index,".",p_item)
        num = input("选择：")
        if num.isdigit() and int(num)<4:
            if int(num) == 0:
                with open("info.txt",'r') as f1:
                    for item in  f1:
                        #print(item.split())
                        d1[item.split()[0]] = item.split()[1]         # 把info.txt中的信息以键值对的形式存放
                    print(d1)
                username = input("请输入要查询的员工姓名：")
                if username in d1.keys():
                    print("%s 的工资是：%s" %  (username ,d1[username]))
                else:
                    print("你输入的员工不存在！")
            if int(num) == 1:
                w_str =""        # 定义一个空字符串
                user_salary = input("请输入要修改的员工姓名和工资，用空格分隔 Alex 10:")
                user_salary_list= user_salary.split()  # 把输入的字符串姓名和工资列表化
                #print(user_salary_list)
                user = user_salary_list[0]          # 取出修改员工的姓名
                new_salary = user_salary_list[1]    # 修改值
                with open("info.txt",'r') as f1:
                    for item in  f1:
                        d2[item.split()[0]] = item.split()[1]
                    old_salary = d2[user]    # 找出该员工的old的工资
                    f1.seek(0)               # 文件句柄指针回到文件首部
                    for line in f1:          # 一行一行的找出old值，用new值替代，并且写入一个字串中
                        if old_salary in line:
                            line = line.replace(old_salary,new_salary)
                            w_str += line
                        else:
                            w_str +=line
                with open("info.txt",'w') as f1: # 把字串写入info.txt
                    f1.write(w_str)
                print("修改成功")
            if int(num) == 2:
                d1 = {}
                passwd = "000000"           #管理员添加新员工，密码默认为000000
                str = input("请输入要增加的员工姓名和工资，用空格分隔( Eric 9999)： ")
                with open("info.txt",'a') as f1:   # 把新员工信息(姓名、工资)写入info.txt
                    f1.write(str+"\n")
                print("修改成功")
                str_list = str.split()
                print(str_list)
                d1[str_list[0]] = passwd
                with open("userdb.json",'r') as f1:
                    data1 = json.load(f1)
                    data1.update(d1)
                #print(data1)
                with open("userdb.json",'w') as f1:  # 同时把新员工信息(姓名、密码)添加到数据库信息文件
                    json.dump(data1,f1)
            if int(num) == 3:
                print("退出成功")
                exit()
                falg = 1
        else:
            print("不合法输入,请重新输入")

if __name__ == "__main__":  # 判断是否是直接运行该.py文件
    login()                  # 调用登录函数