# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework1.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月09日 星期五 20时41分51秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

friend = {'first_name' : 'wang','last_name' : 'yuan','age' : 24,'city' : 'beijing'}
print(friend['first_name'])
print(friend['last_name'])
print(friend['age'])
print(friend['city'])
human1 = {'first_name': 'xin','last_name': 'yincheng', 'age': 25,'city': 'xinjiang'}
human2 = {'first_name': 'su','last_name': 'zhuoran', 'age': 26,'city': 'jilin'}
peoples = [friend,human1,human2]
for people in peoples:
    print(people)
