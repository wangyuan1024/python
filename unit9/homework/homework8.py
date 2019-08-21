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

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privilege = Privileges(['can add post','can delete post','can ban user'])

class Privileges():
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

admin = Admin('wang','yuan')
admin.privilege.show_privileges()

