#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)

from core import course_system

print(sys.path)
print(BASE_DIR)


def main():
    flag = 1
    print("\033[31;1m欢迎登录选课系统\033[0m".center(60,"*"))
    while flag:
        print\
        ('''
        1 管理员视图
        2 讲师视图
        3 学员视图
        4 退出系统
        ''')
        view_dict = {1:"administor",2:"teacher",3:"student",4:"quit"}
        user_choose = int(input("\033[31;1m请输入您的选择序号：\033[0m"))
        if user_choose in view_dict.keys():
            user_type = view_dict[user_choose]
            course_sytem.User_Type(user_type)
            print("user_type=",user_type)
            print("1")
        else:
            print("您的输入有误，请重新输入!")

if __name__ == '__main__':
    main()



