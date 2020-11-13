#!/usr/bin/python
#_*_coding:utf8_*_


import os
import sys

# 文件所在绝对路径的上上级目录
file_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(file_directory, 'core')
sys.path.insert(0,path)
# 定义客户端文件的上传下载的目录
up_down_file_path = os.path.join(file_directory, "home")

import main


if __name__ == "__main__":
    f1 = main.FtpClient()
