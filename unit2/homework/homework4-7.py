# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework4-7.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月02日 星期五 16时59分27秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

inv_list = ['xiaohong','xiaoli','xiaoming']
for person in inv_list:
    print(person + ",please come to my dinner.")

print(inv_list[0] + " cannot come.")
inv_list.remove('xiaohong')
for person in inv_list:
    print(person + ",please come to my dinner.")

inv_list.insert(0,'xiaoqing')
inv_list.insert(2,'xiaobai')
inv_list.append('xiaogang')
for person in inv_list:
    print(person + ",please come to my dinner.")

print("Sorry, only two guests can be invited to dinner.")
n = len(inv_list)
while n>2:
    name = inv_list.pop()
    print(name + ",I am so sorry.")
    n = n - 1
print("----------------------")
for person in inv_list:
    print(person + ",please come to my dinner.")
while n>0:
    name = inv_list.pop()
    print(name + ",I am so sorry.")
    n = n - 1
for person in inv_list:
    print(person + ",please come to my dinner.")
