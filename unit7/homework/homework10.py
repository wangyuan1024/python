# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework10.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月14日 星期三 16时38分46秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

places = []
place = ''
while place != 'quit':
    place = input("If you could visit one place in the world,where would you go?")
    if place!='quit':
        places.append(place)
print(places)
