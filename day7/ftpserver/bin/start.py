#!/usr/bin/python
#_*_coding:utf8_*_


import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
# print("line :", sys.path)
from core import main

if __name__ == "__main__":
    main.start()
