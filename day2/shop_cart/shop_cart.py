# -*- coding:utf-8 -*-
# Author: cntsp

# 导入需要的库
import json
import getpass   # Pycharm中无法实现密码不可见
import time

username = "None"
flag = 0
# 用户注册模块
def register():
    print("\n请输入新的用户名和密码:")
    while True:
        username = input("username:").strip()
        password = input("password:").strip()
        with open("database.json",'r') as f1:
            user_info = json.load(f1)
        if not user_info.get(username):
            first_login = 0
            balance = 0
            user_increase = {username:[password,first_login,balance,[]]}
            user_info.update(user_increase)
            with open("database.json", 'w') as f2:
                json.dump(user_info, f2)
            print("registration success!")
            break
        else:
            print("%s has exists,please try again! " % username)
    return username

def check_login(flag,username="none"):
    while True:
        username = input("please enter your username:")
        with open("database.json", 'r', encoding="utf-8") as f1:
            user_info = json.load(f1)
            user_keys = list(user_info.keys())
        if username not in user_keys:
            num = input("用户名输入错误\n选择[0=重新输入][1=注册新用户]")
            if not num:
                print("请重新输入")
                continue
            else:
                flag = 0
                break
        else:
            password = input("please enter your password:")
            if password in user_info[username][0]:
                if not int(user_info[username][1]):
                    user_info[username][2] = input("欢迎第一次来到欢乐购,请输入你的工资:")
                    user_info[username][1] = 1
                    with open("database.json", 'w') as f1:
                        json.dump(user_info, f1)
                    #flag = 1
                    break
                else:
                    print("欢迎再次来到欢乐购,下面是你上次离开后的消费情况！")
                    print("\033[1;31;47mwhite your balance: %s RMB.\nyour shop_cart has:\033[0m" % user_info[username][2])
                    for item in user_info[username][3]:
                        print("\033[1;31;47m%s \033[0m" % item)
                    flag = 1
                    print("再次登录可继续购买！")
                    break
            else:
                print("password is false,please try again!")
    return flag,username

#购物列表和购物操作过程
def product_list(username):
    flag = 0
    while not flag:
        product_name = ()
        with open("database.json",'r') as f1, open("shop.json",'r',encoding="utf-8") as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)
        goods_category = list(data2.keys())
        print("可购买的商品如下： 单价(元)")
        for item in enumerate(goods_category):
            index = item[0]
            goods = item[1]
            prices = data2[goods]
            print(index,".",goods,prices)
        user_choices = int(input("\nEnter your choose product number:"))
        print(goods_category[user_choices])
        print(data2[goods_category[user_choices]])
        product_price = int(data2[goods_category[user_choices]])
        balance =  int(data1[username][2])
        if balance < product_price:
            recharge = input("Sorry,余额为 %s,请充值或者选择q退出:"% balance)
            if recharge == "q":
                exit()
            elif recharge.isdigit():
                balance += int(recharge)
                data1[username][2] = str(balance)
                with open("database.json",'w') as f1:
                    json.dump(data1,f1)
            else:
                print("Invalid enter,please try again")
        else:
            balance -= product_price
            data1[username][2] = str(balance)
            data1[username][3].append(goods_category[user_choices])
            with open("database.json", 'w') as f1:
                json.dump(data1, f1)
            print("\033[1;31;47m you buy goods has been added shop_cart successfully!\033[0m")
            # 消费记录写入文件
            consumption_write_log(username, goods_category[user_choices], product_price)
            user_choices1 = input("[q=quit][g=go on buy][c=check]")
            if user_choices1 == "q":
                with open("database.json",'w') as f1:
                    json.dump(data1,f1)
                print("\033[1;31;47mwhite your balance: %s RMB.\nyour shop_cart has:\033[0m" % balance)
                for item in data1[username][3]:
                    print("\033[1;31;47m%s \033[0m" % item)
                flag = 1
            elif user_choices1 == "g":
                pass
            elif user_choices1 == "c":
                consumption_read_log(username)
                user_choices2 = input("[g=go on][q=quit]")
                if user_choices2 == "g":
                    continue
                elif user_choices2 == "q":
                    flag = 1
                    continue
            else:
                pass

# 消费记录写入模块
def consumption_write_log(username,goods_name,goods_price):
    #_user = 0
    log_time = time.strftime("%Y-%m-%d %X", time.gmtime() )
    user_list = []
    user_product_log =[]
    user_product_log.append(goods_name)
    user_product_log.append(goods_price)
    user_product_log.append(log_time)
    with open("user_log.json",'r') as f1:
        data1 = json.load(f1)
        user_keys = list(data1.keys())
        if username in user_keys:
            #print(data1[username])
            data1[username].append(user_product_log)
        else:
            user_list.append(user_product_log)
            data1[username] = user_list
    with open("user_log.json", 'w') as f1:
        json.dump(data1, f1)
    print("user buy log has write!")
    return
# 消费记录读出模块
def consumption_read_log(username):
    with open("user_log.json",'r') as f1:
        data1 = json.load(f1)
        if data1.get(username):
            for item in enumerate(data1[username]):
                index = item[0]
                buy_log = item[1]
                print("第 %s 条, %s" %(index,buy_log))
            #print(data1[username])
        else:
            print("There is no user's consumption record")

if __name__ == "__main__":
    # 测试登陆模块(检测用户是否存在，存在且为第一次登陆，打印欢迎信息，并提醒充值，存在且不是第一次登陆，显示上次的消费情况)
    # tuple1 = () 定义个空元组，用来存放登录模块的返回值(标志位,用户名)
    tuple1 = check_login(flag,username)
    flag = tuple1[0]
    username = tuple1[1]
    if flag == 0:             # flag为0，则不存在此用户，请注册
        register()
        product_list(check_login(flag,username)[1])  # 注册后检测登陆，登陆后，由于是第一次登陆，需要充值，再开始购买
    elif flag == 1:    #  flag为1，说明之前该用户用登陆过，呈现上次消费情况后，可以再次登陆购买
        username = input("username:")
        password = input("password:")
        product_list(username)
    else:
        pass
