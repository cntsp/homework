#!/usr/bin/python
#-*-coding:utf8-*-

import os
import sys

config_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(config_path)

from core import main

hm1 = main.HostManager()
main.HostManager.read_config()

