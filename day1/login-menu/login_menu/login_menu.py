# -*- coding:utf-8 -*-
# Author: CNTSP
####################################################
# ѧԱ��Ϣ��8��-������
# ��ʦ��Ϣ��sublimePython
# QQ:1909873483
# blog:https://cntsp.github.io./
###################################################
import getpass       # ����getpassģ�飬ʹ�û���������벻�ɼ�
username = input("username: ")
list1 = []
list2 = []    # �����������б��ֱ����ڴ�Ŵ��ļ������������û��Լ��û�������
with open("lock_name","r",encoding="utf-8") as f1: # with as�﷨�����ļ����û�����list1�б���
    for line in f1:
        list1.append(line.strip("\n"))              # for��������list1 = ['tangshupei','hushaohua']
if username in list1:                               # ���username����Ϊtangshupei��hushaohuaʱ�����������û�,ͬʱ�˳�����
    print("your username has been locked!")
    exit()
with open("name","r",encoding="utf-8") as f2:    # ��name�ļ��е��û���������ת�����б�list2
    for line in f2:
        list2.append(line.strip("\n")) # forѭ��������list2 = ['tangshupei 111', 'hushaohua  222', 'wangning   333', 'lushujie   444']
    n = len(list2)                    # n = 4
    count = 0                   # count������¼�������Ĵ���
while True:
    for line in range(n):     # ��ʼ�û������Ե�forѭ����ֱ��������ȷ���û���
            m = list2[line]
            s = m.split()
            user = s[0]
            passwd = s[1]
            if username == user:             # ������ȷ���û���
                while True:                    # ��ʼ���������ѭ��
                    password = input("password:")    # Pycharm ��password = getpass.getpass(pwd="password:")�����������
                    if password == passwd:  #
                        print("%s,welcome coming the python world" % username.capitalize())
                        exit()
                    else:                            # ��������ٴγ���
                         print("password is error,please try again!")
                         count += 1            # ��¼�������
                         if count >2:                # ����������3�δ���󣬰Ѹ��û�����ӵ������ļ���ͬʱ�˳�����
                             print("password has more than three times,and your username has locked!")
                             with open("lock_name", "a", encoding="utf-8") as f2:
                                 f2.write(username + "\n")
                             exit()
    if not count:     # �жϸ��û��Ƿ���ڣ�countΪ0ʱ�����û�������,��������
        print("Sorry,%s not exist!" % username)
        break