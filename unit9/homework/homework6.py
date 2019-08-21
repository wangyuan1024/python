# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework6.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月20日 星期二 19时07分02秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8
from homework1 import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['apple','banana']

    def printFlavors(self):
        print(self.flavors)

ice = IceCreamStand('name','type')
ice.describe_restaurant()
ice.printFlavors()

