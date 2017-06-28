#测试一个用户信息库中没有的用户
please enter your username:cntsp
用户名输入错误
选择[0=重新输入][1=注册新用户]1

请输入新的用户名和密码:
username:cntsp
password:629
registration success!
please enter your username:cntsp
please enter your password:629
欢迎第一次来到欢乐购,请输入你的工资:50000
可购买的商品如下： 单价(元)
0 . SONY CAMERA 4000
1 . Bicycle 1000
2 . IPhone 5888
3 . Mac Pro 12000

Enter your choose product number:0
SONY CAMERA
4000
 you buy goods has been added shop_cart successfully!
user buy log has write!
[q=quit][g=go on buy][c=check]g
可购买的商品如下： 单价(元)
0 . SONY CAMERA 4000
1 . Bicycle 1000
2 . IPhone 5888
3 . Mac Pro 12000

Enter your choose product number:2
IPhone
5888
 you buy goods has been added shop_cart successfully!
user buy log has write!
[q=quit][g=go on buy][c=check]c
第 0 条, ['SONY CAMERA', 4000, '2017-06-27 12:47:47']
第 1 条, ['IPhone', 5888, '2017-06-27 12:47:57']
[g=go on][q=quit]q

Process finished with exit code 0

# 再次以cntsp的身份进入
please enter your username:cntsp
please enter your password:123
password is false,please try again!
please enter your username:cntsp
please enter your password:629
欢迎再次来到欢乐购,下面是你上次离开后的消费情况！
white your balance: 40112 RMB.
your shop_cart has:
SONY CAMERA 
IPhone 
再次登录可继续购买！
username:cntsp
password:629
可购买的商品如下： 单价(元)
0 . Bicycle 1000
1 . IPhone 5888
2 . Mac Pro 12000
3 . SONY CAMERA 4000

Enter your choose product number:2
Mac Pro
12000
 you buy goods has been added shop_cart successfully!
user buy log has write!
[q=quit][g=go on buy][c=check]g
可购买的商品如下： 单价(元)
0 . Bicycle 1000
1 . IPhone 5888
2 . Mac Pro 12000
3 . SONY CAMERA 4000

Enter your choose product number:0
Bicycle
1000
 you buy goods has been added shop_cart successfully!
user buy log has write!
[q=quit][g=go on buy][c=check]c
第 0 条, ['SONY CAMERA', 4000, '2017-06-27 12:47:47']
第 1 条, ['IPhone', 5888, '2017-06-27 12:47:57']
第 2 条, ['Mac Pro', 12000, '2017-06-27 13:01:48']
第 3 条, ['Bicycle', 1000, '2017-06-27 13:02:06']
[g=go on][q=quit]q

Process finished with exit code 0