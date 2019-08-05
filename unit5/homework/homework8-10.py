# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework8.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月05日 星期一 17时00分59秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

users = ['admin','zhao','qian','sun','li']
for user in users:
    if user == 'admin':
        print("Hello " + user + ",would you like to see a status report?")
    else:
        print("Hello " + user + ",thank you for logging in again")

if users:
    print("It is not empty.")
else:
    print("It is empty.")
users = []
if users:
    print("It is not empty.")
else:
    print("It is empty.")

current_users = ['admin','zhao','qian','sun','li']
new_users = ['admin','zhou','Li','zheng','sun']
for user in new_users:
    if user.lower() in current_users:
        print(user + " has been used.")
    else:
        print(user + " is not used.")
