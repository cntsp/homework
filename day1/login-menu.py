# -*- coding:utf-8 -*-
# Author: CNTSP
####################################################
#学员信息：8组-唐书培
#导师信息：sublimePython
#QQ:1909873483
#blog:https://cntsp.github.io./
###################################################

f1 = open("name",'r',encoding="utf-8")     #以只读模式打开存放登录名和密码的文件名为name的文件
f2 = open("lock_name",encoding="utf-8")   #在调用open时可以省略模式说明，因为'r'是默认的，读默认打开锁定用户名的文件lock_name
count = 0              #计数器是用来记录用户名错误的输入次数
flag = 0               #标志位初始化为零，是用来和计数器共同来判断是否跳出最外层while 循环，结束程序的
while True:        #开始用户的输入循环
    if count <3 and flag==0:               #判断用户名是否输入3次错误，输入错误3次结束程序，或者flag被置为1，也跳出程序，flag被置为1的可能是该用户是个被锁定的用户，或者该用户在3次内成功登陆了
        username = input("username:")     #input提示输入用户名
        password = input("password:")    #input提示输入密码
        while True: #进入内层while循环
            line1 = f2.readline()      #循环读取锁定文件的每一行
            if username in line1:     #判定输入的用户名是否在锁定文件中，如果是则打印已锁定信息，同时flag标志置1，跳出内层while循环
                print("your useranme has been locked!")
                flag = 1
                break
            if len(line1)==0:       #检测锁定文件是否读完，读完用户名没有锁定，进入if
                line2 = f1.readline()  #循环读取存放用户名和密码的f1文件的每行
                if username in line2 and password in line2: #判断输入的用户名和密码是否存在，存在，打印欢迎信息，同时flag置为1，跳出内层while循环
                    print("%s,welcome coming the python world!" % username.capitalize())
                    flag=1
                    break
                if len(line2)==0: #判断f1文件是否读完，读完说明f1未有该用户
                    if count == 2:#判读该用户是否输入错误达到3次，如果达到3次，打印锁定信息，同时把该用户名锁定到lock_name文件中
                        print("you have entered 3 times false, you are out!")
                        f2=open("lock_name",'a',encoding="utf-8")
                        lock_name=username
                        try: #使用try/finally语句，确保写入的文件及时关闭，防止程序因为某些原因崩溃，造成数据未写入文件
                            f2.write(lock_name+"\n")
                        finally:
                            f2.close()
                    else:   #else子句，若用户输入错误不到3次，打印请用户再次输入信息
                        print("your username or password is false,please try again")
                        #count +=1
                    f1.seek(0)#存放用户名和密码的文件回到文件起始位置，开始下一次重新输入的检测
                    count +=1#记录输入错误的次数
                    #print(count)
                    break#跳到外层的while循环中
    else:#当count=3或者flag=1时跳出最外层while，程序结束
        break


