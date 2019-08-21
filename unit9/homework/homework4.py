# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework1.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月19日 星期一 19时50分53秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is opening")

    def show_number_served(self):
        print(str(self.number_served) + " people have eaten.")

    def set_number_served(self,number):
        self.number_served = number

    def increment_number_served(self):
        self.number_served+=1

restaurant = Restaurant('回信餐厅','茶餐厅')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.show_number_served()
restaurant.number_served = 3
restaurant.show_number_served()
restaurant.set_number_served(4)
restaurant.show_number_served()
restaurant.increment_number_served()
restaurant.show_number_served()

