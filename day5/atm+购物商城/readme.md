# 第五周作业  ATM + 购物商城

### 作者介绍:
* Author: cntsp
* My Blog:[https://cntsp.github.io.](https://cntsp.github.io."cntsp's blog")

### 功能实现
* 1 提供管理员和用户接口，管理员功能包括：添加账户、删除账户、修改用户信用卡额度、冻结/解冻用户等
* 2 用户认证用装饰器
* 3 额度15000或自定义
* 4 实现购物商城，买东西加入购物车，调用信用卡接口结账
* 5 用户可以提现，手续费5/%，转账、查询余额、还款、查询ATM操作日志
* 6 支持多账户登录

### 账户信息
* 管理员账号：admin 密码：admin
* 测试(1)用户账户：tangmengqi 密码：tangmengqi 测试(2)用户账户：tangshupei 密码：tangshupei

### 环境依赖
* Pycharm (python3.4.4)

### 目录结构
>*  /bin/main.py 主程序，实现了所有功能
>*  /db/admin.json 管理员的账号信息
>*  /db/tangmengqi.json 用户的账号信息
>*  /db/tangmengqi-shop-cart.json 用户的购物车信息
>*  /db/tangmengqi_atm.log 用户的ATM操作日志
>*  /db/tangshupei  用户的账号信息
