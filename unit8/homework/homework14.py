# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework14.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月17日 星期六 22时28分04秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

def make_car(manufacturers,model,**trait):
    car = {}
    car['manufacturers'] = manufacturers
    car['model'] = model
    for key,value in trait.items():
        car[key] = value
    return car

car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)
