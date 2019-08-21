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
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name + " " + self.last_name)

    def greet_user(self):
        print(self.first_name + " " + self.last_name + ",thanks for your coming!")

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def show_login_attempts(self):
        print(str(self.login_attempts) + " users have logined.")

user = User('wang','yuan')
user.describe_user()
user.greet_user()
user.show_login_attempts()
user.increment_login_attempts()
user.show_login_attempts()
user.increment_login_attempts()
user.show_login_attempts()
user.increment_login_attempts()
user.show_login_attempts()
user.reset_login_attempts()
user.show_login_attempts()
