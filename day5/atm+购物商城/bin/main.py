__Author__ = "CNTSP"

import os
import sys
import time
import json
import shutil

a = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_file_path = os.path.join(a, 'db')
current_user = {}
admin_dict = {}
user_info = {"password":123, "type":"guest", "credits":15000, "locked":False, "balance":15000}
sum_price = 0
shopping_menu = {
    '家电类': [
        ('空调', 3999.0),
        ('电视机', 5599.0),
        ('抽烟机', 1226.0),
    ],
    '汽车类': [
        ('BMW', 1359999.0),
        ('Tesla',  1229999.0),
        ('Porsche', 1888888.0),
    ],
    '电子产品类': [
        ('Huawei P9', 3499.0),
        ('iPhone7 plus', 7199.0),
        ('xiaomi2', 3000.0)
    ],
    '服饰类': [
        ('Jordan T-shirt', 299.0),
        ('Adidas shorts ', 299.0),
        ('Puma vest', 399.0),
    ],
}
first_shopping_menu = sorted(shopping_menu.keys())
entry_menu = ["商品铺","购物车","退出购物商城"]

def add_user_info(username, password):
    """
    创建用户功能具体实现函数
    :param username:
    :param password:
    :return:
    """
    global user_info
    #print(user_info)
    user_db_file = os.path.join(db_file_path, username + ".json")
    if os.path.isfile(user_db_file):
        return False
    else:
        add_user_info = {"username":username, "password":password}
        user_info.update(add_user_info)
        #print(user_info)
        with open(user_db_file, 'w') as f1:
            json.dump(user_info, f1)
        return True

def del_user_info(username):
    """
    删除指定账户功能具体实现函数
    :param username:
    :return:
    """
    user_db_file = os.path.join(db_file_path, username + ".json")
    if os.path.isfile(user_db_file):
        os.remove(user_db_file)
        return True

def modify_user_info(username: str, new_credits: int):
     """
     修改用户信用额度具体实现函数
     :param username:
     :return:
     """
     print(username, new_credits)
     user_db_file = os.path.join(db_file_path, username + ".json")
     if os.path.isfile(user_db_file):
         if new_credits > 0:
             with open(user_db_file, 'r') as f1:
                 user_infomation = json.load(f1)
             user_infomation["credits"] = new_credits
             user_infomation["balance"] = new_credits
             with open(user_db_file, 'w') as f1:
                 json.dump(user_infomation, f1)
             return True
     else:
         #print("你要修改的该用户不存在！")
         return False

def freeze_thaw_account_info(username: str, type):
    """
    冻结/解冻指定用户功能具体实现函数
    :param username:
    :return:
    """
    user_db_file = os.path.join(db_file_path, username +".json")
    if os.path.isfile(user_db_file) and type == "freeze":
        with open(user_db_file, 'r') as f1:
            user_information = json.load(f1)
        user_information["locked"] = True
        with open(user_db_file, 'w') as f1:
            json.dump(user_information, f1)
        return True
    elif os.path.isfile(user_db_file) and type == "thaw":
        with open(user_db_file, 'r') as f1:
            user_information = json.load(f1)
        user_information["locked"] = False
        with open(user_db_file, 'w') as f1:
            json.dump(user_information, f1)
        return True
    else:
        return False

def add_account():
    """
    管理员增加账户功能
    :return:
    """
    exit_flag = False
    while not exit_flag:
        input_username = input("输入新增账户名：（英文字符）").strip()
        input_passwrod = input("输入密码（留空默认设置成：123）:").strip()
        password = input_passwrod if input_passwrod else "123"
        add_account_status = add_user_info(input_username, password)
        if add_account_status:
            print("%s 账户创建成功！" % input_username)
            exit_flag = True
        else:
            print("该账户已经存在，请重新输入！")

def del_account():
    """
    管理员删除账户功能
    :return:
    """
    exit_flag = False
    while not exit_flag:
        input_username = input("输入删除的账户名：").strip()
        del_account_status = del_user_info(input_username)
        if del_account_status:
            print("%s 账户删除成功！" % input_username)
            exit_flag = True
    pass
def modify_user_credits():
    """
    管理员修改账户的信用额度功能
    :return:
    """
    exit_flag = False
    while not exit_flag:
        input_username = input("请输入修改额度的账户名：").strip()
        new_credits = int(input("输入新的信用额度：(级别：15000，20000，30000)").strip())
        modify_account_status = modify_user_info(input_username, new_credits)
        if modify_account_status:
            print("额度修改成功！")
            exit_flag = True
        else:
            print("你要修改的用户不存在，请重新输入！")

def freeze_user():
    """
    管理员冻结账号功能
    :return:
    """
    type = "freeze"
    exit_flag = False
    while not exit_flag:
        input_username = input("请输入要冻结的账户名：").strip()
        freeze_account_status = freeze_thaw_account_info(input_username, type)
        if freeze_account_status:
            print("%s 账户已被冻结" % input_username)
            exit_flag = True
        else:
            print("你输入的账户不存在，请重新输入！")
def thaw_user():
    """
    管理员解冻账号功能
    :return:
    """
    type = "thaw"
    exit_flag = False
    while not exit_flag:
        input_username = input("请输入要解冻的账户名：").strip()
        thaw_account_status = freeze_thaw_account_info(input_username, type)
        if thaw_account_status:
            print("%s 账户已解冻" % input_username)
            exit_flag = True
        else:
            print("您输入的账户不存在，请重新输入！")
    pass
def admin_exit():
    return True
def admin_entry():
    """
    管理员接口
    :return:
    """
    exit_flag = False
    admin_dict = {"1":add_account, "2":del_account, "3":modify_user_credits, "4":freeze_user, "5":thaw_user, "6":admin_exit}
    while not exit_flag:
        print("\033[32;1m管理员菜单\033[0m".center(60, "#"))
        print("""
        1  添加账户
        2  删除账户
        3  修改用户额度
        4  冻结账户
        5  解冻账户
        6  退出
        """)
        admin_choose = input("输入您选择的序号：").strip()
        #print(admin_dict.keys())
        #print(admin_dict[admin_choose])
        if admin_choose in admin_dict.keys():
            deal_result = admin_dict[admin_choose]()
            if deal_result:
                exit_flag = True
        else:
            print("您的输入有误，请重新输入！")
            #print("welcome, admin coming")
def choose_goods(choose_serial_number:int):
    """
    购物处理函数
    :param choose_serial_number:
    :return:
    """
    #print(first_shopping_menu)
    exit_flag = False
    while not exit_flag:
        second_shopping_menu = shopping_menu[first_shopping_menu[choose_serial_number]]
        #print(second_shopping_menu)
        for goods, price in enumerate(second_shopping_menu):
            print("\033[31;1m%s\033[0m %s %s RMB/单价" % (goods, price[0], price[1]))
        goods_name = input("请把您需要的商品加入购物车（选择序号）[q键返回上一级]：")
        if goods_name.isdigit():
            goods_name = int(goods_name)
            goods_quantity = int(input("想要购买商品的数量（只能是正整数）："))
            goods_total_price = second_shopping_menu[goods_name][1] * goods_quantity
            dtime = dtime = time.strftime("%Y-%m-%d %H:%M:%S")
            goods_info = {second_shopping_menu[goods_name][0]:[{"unit price":second_shopping_menu[goods_name][1],"quantities":goods_quantity,"total price":goods_total_price,"status":"unpaid","time":dtime}]}
            #print(goods_total_price)
            #print(current_user)
            username = current_user["username"]
            #print(username)
            #print(goods_info)
            user_db_file = os.path.join(db_file_path, username + "-shop-cart.json")
            if os.path.isfile(user_db_file):
                with open(user_db_file,'r') as f1:
                    shop_cart_info = json.load(f1)
                    shop_cart_info.update(goods_info)
                    print(shop_cart_info)
                with open(user_db_file, 'w') as f1:
                    json.dump(shop_cart_info, f1)
                print("\033[32;1m商品已经成功加入购物车中\033[0m")
            else:
                with open(user_db_file,'w') as f1:
                    json.dump(goods_info,f1)
                print("\033[32;1m商品已经成功加入购物车中\033[0m")
        elif goods_name == "q":
            exit_flag = True
        else:
            print("\033[31;1m您输入的序号有误，请重新输入！\033[0m")
    pass

def atm_log(type,money):
    """
    ATM操作日志
    :param type:
    :param money:
    :return:
    """
    user_db_file = os.path.join(db_file_path, current_user["username"] + "_atm.log")
    consumption_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    f = open(user_db_file,'a',encoding="utf-8")
    f.write("时间：%s 操作类型：%s 金额：%s \n" %(consumption_date,type,str(money)))
    print("\033[31;1mATM操作日志记录成功\033[0m")
    pass
def payment_interface(money, *kwargs):
    """
    信用卡支付接口函数
    :param money:
    :param kwargs:
    :return:
    """
    user_db_file = os.path.join(db_file_path, current_user["username"] + ".json")
    with open(user_db_file,'r') as f1:
        user_info = json.load(f1)
        #print(user_info)
        new_balance = user_info["balance"] - money
        if new_balance>0:
            print("\033[31;1m支付成功\033[0m")
            print("\033[31;1m您现在的信用卡可用余额为：%s\033[0m" %new_balance)
            user_info["balance"] = new_balance
            with open(user_db_file, 'w') as f1:
                json.dump(user_info,f1)
                #print("个人信息：%s" %user_info)
                consumption_type = "Shopping-consumption"
            atm_log_status = atm_log(consumption_type,money)
        elif sum_price > 15000:
            print("购物车中的消费总额超出了信用卡的最大额度")
        elif  -15000<new_balance <0:
            print("信用卡余额不足，请前往ATM中心进行还款，之后再进行支付")
    pass
def show_shop_cart():
    """
    展示购物车函数
    :return:
    """
    #print("\033[31;1m%s\033[0m" % current_user)
    global sum_price
    flag = 0
    user_db_file = os.path.join(db_file_path, current_user["username"] + "-shop-cart.json")
    if os.path.isfile(user_db_file):
        with open(user_db_file,'r') as f1:
            shop_cart_info = json.load(f1)
            for i in shop_cart_info.keys():
                unit_price = str(shop_cart_info[i][0]["unit price"])
                quantities = str(shop_cart_info[i][0]["quantities"])
                total_price = str(shop_cart_info[i][0]["total price"])
                pay_status = shop_cart_info[i][0]["status"]
                buy_time = shop_cart_info[i][0]["time"]
                if pay_status == "unpaid":
                    sum_price += shop_cart_info[i][0]["total price"]
                    #print(shop_cart_info[i][0]["status"])
                    #shop_cart_info[i][0]["status"] ="paid"
                    #print(shop_cart_info)
                    #with open(user_db_file,'w') as f1:
                    #    json.dump(shop_cart_info,f1)
                    print("商品名称：%s  单价：%sRMB  数量：%s  总价：%sRMB  支付状态：%s  购买时间：%s" %(i,unit_price,quantities,total_price,pay_status,buy_time))
                    flag = 1
            print("\033[31;1m购物车中商品总价：%s\033[0m" % sum_price)
            print("flag的值为：%s" %flag)
            if flag == 1:
                user_choose = input("\033[32;1m是否同意进行结算[yes=同意][no=不同意]：\033[0m").strip()
                if user_choose == "yes":
                    with open(user_db_file, 'r') as f1:
                        shop_cart_info = json.load(f1)
                    for i in shop_cart_info.keys():
                        pay_status = shop_cart_info[i][0]["status"]
                        if pay_status == "unpaid":
                            shop_cart_info[i][0]["status"] ="paid"
                            #print(shop_cart_info)
                            with open(user_db_file,'w') as f1:
                                json.dump(shop_cart_info,f1)
                    print("\033[31;1m正在调用信用卡接口支付请稍等...\033[0m".center(60))
                    payment_status = payment_interface(sum_price)
                    pass
                elif user_choose == "no":
                    pass
            else:
                print("购物车中没有未付商品，请继续购买吧！")
        return sum_price
    else:
        print("\033[31;1m购物车空空如也，赶快购物去吧！\033[0m")
    pass

def shopping_mall():
    """
    购物商城
    :return:
    """
    exit_flag = False
    global sum_price
    while not exit_flag:
        print("\033[31;1m购物商城\033[0m".center(60, "#"))
        #shopping_menu_key = list(shopping_menu.keys())
        #first_shopping_menu = sorted(shopping_menu.keys())
        #print(shopping_menu_key)
        #print("\n")
        #print(shopping_menu_key1)
        for num, menu in enumerate(entry_menu):
            print("\033[32;1m%s\033[0m %s" %(num,menu))
        menu_choose = int(input("请输入您选择的序号,[q键返回上一级]").strip())
        if menu_choose == 0:
            second_flag = False
            while not second_flag:
                for num, p_name in enumerate(first_shopping_menu):
                    print("\033[32;1m%s\033[0m %s" %(num,p_name))
                first_menu_choose = input("请输入您选择的序号，[q键返回上一级]：").strip()
                if first_menu_choose.isdigit():
                    buys_status = choose_goods(int(first_menu_choose))
                    second_flag = False
                elif first_menu_choose == "q":
                    second_flag = True
                else:
                    print("您的输入有误，请重新输入！")
        elif menu_choose == 1:
            show_shop_cart_status = show_shop_cart()
        elif menu_choose == 2:
            exit_flag = True
    pass
def check_balances():
    """
    查询账户信用卡余额
    :return:
    """
    print("\033[32;1m欢迎查询余额\033[0m".center(60))
    user_db_file = os.path.join(db_file_path, current_user["username"] + ".json")
    with open(user_db_file, 'r') as f1:
        user_info = json.load(f1)
        print("\033[31;1m您的信用卡最高额度为：%s,目前余额为：%s" %(user_info["credits"],user_info["balance"]))
    pass
def withdraw():
    """
    信用卡提现功能
    :return:
    """
    print("\033[32;1m欢迎提现,根据我行规定，信用卡提现需收取5%的手续费！\033[0m".center(60))
    withdraw_quota = int(input("\033[31;1m请输入您提现的额度（大于零的整数）：\033[0m").strip())
    withdraw_total = withdraw_quota  * (1+0.05)
    old_balance = current_user["balance"]
    new_balance = old_balance - withdraw_total
    user_db_file = os.path.join(db_file_path, current_user["username"] + ".json")
    with open(user_db_file,'r') as f1:
        user_info = json.load(f1)
        user_info["balance"] = new_balance
    with open(user_db_file,'w') as f1:
        json.dump(user_info,f1)
    if new_balance>0:
        print("\033[31;1m提现成功\033[0m")
        print("信用卡的现有额度：\033[32;1m %s RMB\033[0m" % new_balance)
        withdraw_status = atm_log("提现",withdraw_quota)
    else:
        print("您的提现额度超过了信用卡可使用的额度")
def transfer():
    """
    信用卡转账功能
    :return:
    """
    print("\033[31;1m欢迎转账\033[0m".center(60))
    username = input("\033[32;1m请输入收款人的账户名：\033[0m").strip()
    payee_db_file = os.path.join(db_file_path,username + ".json")
    user_db_file = os.path.join(db_file_path, current_user["username"] + ".json")
    if os.path.isfile(payee_db_file):
        money = int(input("\033[31;1m请输入金额：\033[0m").strip())
        with open(user_db_file, 'r') as f1:
            user_info = json.load(f1)
        if user_info["balance"] - money>0:
            user_info["balance"] -= money
            with open(user_db_file,'w') as f1:
                json.dump(user_info,f1)
            with open(payee_db_file,'r') as f1:
                payee_info = json.load(f1)
                payee_info["balance"] += money
            with open(payee_db_file,'w') as f1:
                json.dump(payee_info,f1)
            print("\033[31;1m转账成功，你的目前余额为：%s\033[0m" %user_info["balance"])
            transfer_status = atm_log("转账",money)
        else:
            print("\033[31;1m注意：\033[0m信用卡余额不足或者转账额度超出了信用卡的最高透支额，不能转账")
    pass
def repayment():
    """
    信用卡还款功能
    :return:
    """
    print("\033[31;1m欢迎还款\033[0m".center(60))
    repay_money = int(input("\033[31;1m请输入你的还款额(大于0的整数)：\033[0m"))
    user_db_file = os.path.join(db_file_path, current_user["username"] + ".json")
    if os.path.isfile(user_db_file):
        with open(user_db_file, 'r') as f1:
            user_info = json.load(f1)
            user_info["balance"] += repay_money
        with open(user_db_file, 'w') as f1:
            json.dump(user_info, f1)
        print("你的信用卡最高额度为：%s 现在余额为：%s 已透支额度为：%s" %(str(user_info["credits"]),str(user_info["balance"]),str(user_info["credits"]-user_info["balance"])))
        repay_status = atm_log("还款",repay_money)
    pass
def transaction_record():
    """
    ATM操作记录功能
    :return:
    """
    print("\033[31;1m欢迎查询ATM操作记录\033[0m".center(60))
    user_db_atm = os.path.join(db_file_path, current_user["username"] + "_atm.log")
    f = open(user_db_atm, 'r' ,encoding="utf-8")
    for line in f:
        print(line.strip())
    f.seek(0)
def atm_menu():
    """
    ATM功能函数
    :return:
    """
    user_msg = {"1":check_balances,"2":withdraw,"3":transfer,"4":repayment,"5":transaction_record}
    exit_flag = False
    while not exit_flag:
        print("\n\033[31;1mATM功能菜单\033[0m".center(60))
        print("""\033[31;1m
        1  查询余额
        2  提现
        3  转账
        4  还款
        5  ATM日志
        \033[0m""")
        choose_number = input("\033[31;1m请输入你的操作项[q键：返回上一级]：\033[0m").strip()
        if choose_number.isdigit():
            #print(user_msg.keys())
            if choose_number in user_msg.keys():
                deal_status = user_msg[choose_number]()
                #print("welcome atm world!")
        elif choose_number == "q":
            exit_flag = True
        else:
            print("\033[31;1m您的输入有误\033[0m")
def guest_entry():
    """
    普通用户接口
    :return:
    """
    exit_flag = False
    while not exit_flag:
        print("\033[31;1m消费者菜单\033[0m".center(60, "#"))
        print('''
        1 购物商城
        2 ATM
        3 退出
        ''')
        consumer_choose = input("请输入你选择的序号：").strip()
        if consumer_choose == "1":
            shopping_mall()
        elif consumer_choose == "2":
            atm_menu()
        elif consumer_choose == "3":
            exit_flag = True

# 认证账户是否存在
def verification(username, password):
    db_file = os.path.join(db_file_path, username + '.json')
    if os.path.isfile(db_file):
        #print("有此账号")
        with open(db_file, 'r') as f1:
            user_info = json.load(f1)
            return user_info
    else:
        # 不存在此账号
        return None

def auth():
    """
    用于认证的函数
    :return:
    """
    global current_user, logined
    user_input = input("输入账户名：").strip()
    passwd_input = input("输入账户密码：").strip()
    # 验证账户存在性
    current_user = verification(user_input,passwd_input)
    # print(current_user)
    if current_user:
        # print("登录成功")
        # 账户存在，进行是否锁定的验证
        if not current_user.get("locked", True):
            # 账号未被锁定，验证密码
            if passwd_input == current_user.get("password"):
                logined = True
                print("登录成功")
                return True
            else:
                print("密码不正确")
                return False
        else:
            print("\033[31;1m您好，该账号已被锁定了，请联系管理员！\033[0m")
    elif current_user is None:
        print("账号不存在")
        return False

def auth_deco(func):
    def deco(*args, **kwargs):
        if auth():
            # print("welcome")
            func(*args, **kwargs)
            # return ret
    return deco
@auth_deco
def run():
    """
    登录入口
    :return:
    """
    global current_user
    user_type = current_user.get("type")
    #print(user_type)
    if user_type == "admin":
        admin_entry()
    elif user_type == "guest":
        guest_entry()
    else:
        print("无类型")
if __name__ == "__main__":
    run()