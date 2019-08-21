# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework3.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月19日 星期一 20时04分03秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name + " " + self.last_name)

    def greet_user(self):
        print(self.first_name + " " + self.last_name + ",thanks for your coming!")

user = User('wang','yuan')
user.describe_user()
user.greet_user()
