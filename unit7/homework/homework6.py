# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework5.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月14日 星期三 15时22分28秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

active = input("Please input your active: ")
while active!='quit':
    active = int(active)
    if active<3:
        print("It is free.")
    elif active <=12:
        print("Please hand in 10 dollars.")
    else:
        print("Please hand in 15 dollars.")
    active = input("Please input your active: ")

