## 第6周作业 
### 题目：开发一个支持多用户在线的FTP程序
#### 作者介绍：
*   Author: cntsp
*   My Blog: https://cntsp.github.io

#### 功能实现：
*   用户加密认证
*   允许同时多用户登录
*   每个用户有自己的家目录，且只能访问自己的家目录
*   对用户进行磁盘配额，每个用户的可用空间不同
*   允许用户在ftp server 上随意切换目录
*   允许用户查看当前目录下的文件
*   允许上传和下载文件，保证文件的一致性
*   文件传输过程中，显示进度条
*   附加功能：支持文件的断点续传

#### 环境依赖
> python3.6.8 linux系统(centos7)
#### 目录结构
```text
.
|-- cntsp       # ftp服务端 cntsp用户的家目录
|   |-- 222.txt
|   |-- clientftp.py
|   `-- henan
|       `-- ftp-c-s.zip
|-- ftpclient           # ftp客户端项目目录
|   |-- bin
|   |   |-- __init__.py
|   |   `-- start.py        # ftp客户端启动脚本
|   |-- core
|   |   |-- authentication.py       # 用户登录验证接口
|   |   |-- authentication.pyc
|   |   |-- commands.py             # ftp 服务各个命令实现
|   |   |-- __init__.py
|   |   |-- main.py             # 客户端主程序
|   |   `-- __pycache__
|   |       |-- authentication.cpython-36.pyc
|   |       |-- authentication.cpython-37.pyc
|   |       |-- commands.cpython-36.pyc
|   |       |-- __init__.cpython-36.pyc
|   |       `-- main.cpython-36.pyc
|   |-- home            # ftp用户上传下载的客户端文件保存目录
|   |   |-- 111.txt
|   |   |-- 222.txt
|   |   |-- 444.txt
|   |   `-- ftp-c-s.zip
|   `-- __init__.py
|-- ftpserver
|   |-- bin
|   |   |-- __init__.py
|   |   `-- start.py        # ftp服务端启动脚本
|   |-- core
|   |   |-- __init__.py
|   |   |-- main.py         # ftp服务端主程序
|   |   |-- __pycache__
|   |   |   |-- __init__.cpython-36.pyc
|   |   |   |-- main.cpython-36.pyc
|   |   |   `-- user.cpython-36.pyc
|   |   `-- user.py     # 初始化ftp用户实例
|   |-- data            # ftp用户信息文件
|   |   `-- user.json
|   `-- __init__.py
`-- xiaojie             # ftp服务端 xiaojie 用户的家目录
    |-- anhui
    |   `-- ftp-c-s.zip
    |-- biejing
    |   `-- ftp-c-s.zip
    |-- ftp-c-s.zip
    |-- guangdong
    |   `-- ftp-c-s.zip
    |-- henan
    |   `-- ftp-c-s.zip
    |-- hubei
    |   `-- ftp-c-s.zip
    |-- hunan
    |   `-- ftp-c-s.zip
    |-- shanghai
    |   `-- ftp-c-s.zip
    |-- shanxi
    |   `-- ftp-c-s.zip
    `-- tianjing

```
#### 初始化用户信息
> 用户1：username: cntsp password: nihaoma 磁盘配额：100M
> 
> 用户2：username: xiaojie password: nihaoma 磁盘配额：50M
