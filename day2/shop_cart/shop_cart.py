# -*- coding:utf-8 -*-
# Author: cntsp

# ������Ҫ�Ŀ�
import json
import getpass   # Pycharm���޷�ʵ�����벻�ɼ�
import time

username = "None"
flag = 0
# �û�ע��ģ��
def register():
    print("\n�������µ��û���������:")
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
            num = input("�û����������\nѡ��[0=��������][1=ע�����û�]")
            if not num:
                print("����������")
                continue
            else:
                flag = 0
                break
        else:
            password = input("please enter your password:")
            if password in user_info[username][0]:
                if not int(user_info[username][1]):
                    user_info[username][2] = input("��ӭ��һ���������ֹ�,��������Ĺ���:")
                    user_info[username][1] = 1
                    with open("database.json", 'w') as f1:
                        json.dump(user_info, f1)
                    #flag = 1
                    break
                else:
                    print("��ӭ�ٴ��������ֹ�,���������ϴ��뿪������������")
                    print("\033[1;31;47mwhite your balance: %s RMB.\nyour shop_cart has:\033[0m" % user_info[username][2])
                    for item in user_info[username][3]:
                        print("\033[1;31;47m%s \033[0m" % item)
                    flag = 1
                    print("�ٴε�¼�ɼ�������")
                    break
            else:
                print("password is false,please try again!")
    return flag,username

#�����б�͹����������
def product_list(username):
    flag = 0
    while not flag:
        product_name = ()
        with open("database.json",'r') as f1, open("shop.json",'r',encoding="utf-8") as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)
        goods_category = list(data2.keys())
        print("�ɹ������Ʒ���£� ����(Ԫ)")
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
            recharge = input("Sorry,���Ϊ %s,���ֵ����ѡ��q�˳�:"% balance)
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
            # ���Ѽ�¼д���ļ�
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

# ���Ѽ�¼д��ģ��
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
# ���Ѽ�¼����ģ��
def consumption_read_log(username):
    with open("user_log.json",'r') as f1:
        data1 = json.load(f1)
        if data1.get(username):
            for item in enumerate(data1[username]):
                index = item[0]
                buy_log = item[1]
                print("�� %s ��, %s" %(index,buy_log))
            #print(data1[username])
        else:
            print("There is no user's consumption record")

if __name__ == "__main__":
    # ���Ե�½ģ��(����û��Ƿ���ڣ�������Ϊ��һ�ε�½����ӡ��ӭ��Ϣ�������ѳ�ֵ�������Ҳ��ǵ�һ�ε�½����ʾ�ϴε��������)
    # tuple1 = () �������Ԫ�飬������ŵ�¼ģ��ķ���ֵ(��־λ,�û���)
    tuple1 = check_login(flag,username)
    flag = tuple1[0]
    username = tuple1[1]
    if flag == 0:             # flagΪ0���򲻴��ڴ��û�����ע��
        register()
        product_list(check_login(flag,username)[1])  # ע������½����½�������ǵ�һ�ε�½����Ҫ��ֵ���ٿ�ʼ����
    elif flag == 1:    #  flagΪ1��˵��֮ǰ���û��õ�½���������ϴ���������󣬿����ٴε�½����
        username = input("username:")
        password = input("password:")
        product_list(username)
    else:
        pass
