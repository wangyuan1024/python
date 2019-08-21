# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework4.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月21日 星期三 10时18分06秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

record = True
while(record):
    name = input("Please input your name:")
    if name == 'quit':
        record = False
    with open('guest_book.txt','a') as file:
        file.write(name)




