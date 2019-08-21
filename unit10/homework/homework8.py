# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework8.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月21日 星期三 14时33分23秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8
try:
    with open('cat.txt') as file:
        lines = file.readlines()
except FileNotFoundError:
    pass
else:
    for line in lines:
        print(line)

