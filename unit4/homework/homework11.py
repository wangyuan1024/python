# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework1.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月04日 星期日 10时05分47秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

pizzas = ['pepperoni','potato','tomato']
for pizza in pizzas:
    print("I like " + pizza + " pizza")

print("I really love pizza.")
print("----------------------")
friend_pizzas = pizzas[:]
pizzas.append('meat')
friend_pizzas.append('fruit')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
