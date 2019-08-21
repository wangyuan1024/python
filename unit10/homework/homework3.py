# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework3.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月21日 星期三 10时15分32秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

name = input("Please input your name:")
with open('guest_book.txt','w') as file:
    file.write(name)
