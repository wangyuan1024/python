# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework4.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月10日 星期六 09时48分39秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

river = {
    'changjiang' : 'china',
    'nile' : 'egypt',
    'mengjialahe' : 'indian'
}

for key,value in river.items():
    print("The " + key.title() + " runs through " + value.title())
print("river:")
for key in river.keys():
    print(key)

print("country:")
for value in river.values():
    print(value)
