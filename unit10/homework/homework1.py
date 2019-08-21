# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework1.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月21日 星期三 08时34分30秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

with open('learning_python.txt') as file:
    contents = file.read()
    print(contents)

print("------lines------------")

with open('learning_python.txt') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
