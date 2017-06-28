#第二周作业：购物车程序

### 作者介绍:
* Author: cntsp
* My Blog:[https://cntsp.github.io.](https://cntsp.github.io."cntsp's blog")

### 功能实现
* 1 商品信息-- 单价、名称
* 2 用户信息-- 用户名、密码、余额
* 3 余额不足时，提醒，可充值
* 4 购买过程中，高亮显示商品加入购物车，可以查看历史信息
* 5 用户可多次购买
* 6 用户退出时，打印账户余额和购买过的商品
* 7 用户下次登陆时，回到上次的退出状态，可查看消费信息、余额

### 环境依赖
* Pycharm (python3.4)

### 目录结构
> * database.json用来存放字典类型用户相关信息:用户名、密码、登陆标志位、余额、所买物品
> * shop.json用来存放字典类型商品信息，以字典的格式存放商品名和单价
> * user_log.json用来以字典的形式记录用户的购买历史
> * shop_cart.py购物车程序
> * shop_cart.png流程图
