# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework6.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月14日 星期三 17时12分07秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

def city_country(city,country):
    message = city + ", " + country
    return message.title()

mes = city_country("beijing","china")
print(mes)
mes = city_country("london","the united kindom")
print(mes)
