## 第7周作业 
### 题目：简单主机批量管理工具
#### 作者介绍：
*   Author: cntsp
*   My Blog: https://cntsp.github.io

#### 功能实现：
*   主机分组
*   主机信息配置文件用configparser解析
*   可批量执行命令、发送文件，结果实时返回，执行格式如下
    *   batch_run -h h1,h2,h3 -g web_clusters,db_servers -cmd "df -h"
    *   batch_scp -h h1,h2,h3 -g web_clusters,db_servers -action put -local test.py
*   主机用户名密码、端口可以不同
*   执行远程命令使用 paramiko 模块
*   批量命令需使用 multiprocessing 并发

补充说明：
1. 执行scp命令，需要主控机和各个节点做免密登录
2. 批量执行命令和批量上传文件命令参考如下：
```shell
    批量执行shell 命令时，举例如下：
    batch_run -h web1 -cmd "df -h"
    上面命令将在 web1 主机上执行 df -h
    batch_run -h web1,web2 -cmd "df -h"
    上面命令将在 web1, web2 上执行 df -h 命令
    batch_run -h web1,web2, mysql1 -cmd "df -h"
    上面命令将在 web1,web2,mysql1 上执行 df -h 命令
    batch_run -g web_clusters -cmd "df -h"
    上面命令将在 web_clusters 下的所有web{web1, web2} 上执行 df -h 命令
    batch_run -g db_servers -cmd "df -h"
    上面命令将在 db_servers 下的所有db{mysql1, mysql2} 上执行 df -h 命令
    batch_run -g web_clusters,db_servers -cmd "df -h"

    批量执行put上传 命令时，举例如下：
    batch_scp -h web1 -action put -local test.py -remote /tmp
    上面命令将把本地目录(/core目录)下的test.py 上传到远程主机 web 的 /tmp 目录下
    batch_scp -h we1,web2 -action put -local test.py -remote /tmp/
    上面命令将把本地目录(/core目录)下的test.py 上传到远程主机 web1,web2 的 /tmp 目录下
    batch_scp -h web1,web2,mysql1 -action put -local test.py -remote /tmp
    上面命令将把本地目录(/core目录)下的test.py 上传到远程主机 web1,web2,mysql1 的 /tmp 目录下
    batch_scp -h web1,web2,mysql1,mysql2 -action put -local test.py -remote /tmp
    上面命令将把本地目录(/core目录)下的test.py 上传到远程主机 web1,web2,mysql1,mysql2 的 /tmp目录下
    batch_scp -g web_clusters -action put -local test.py -remote /tmp/
    上面命令将把本地目录(/core目录)下的test.py 上传到所有的web{web1,web2,....} 远程主机的 /tmp 目录下
    batch_scp -g web_clusters,db_servers -action put -local test.py -remote /tmp
    上面命令将把本地目录(/core目录)下的test.py 上传到所有的web{web1,web2,...}db{mysql1,mysql2,...} 远程主机的 /tmp 目录下
```

#### 环境依赖
> python3.6.8 linux系统(centos7)
#### 目录结构