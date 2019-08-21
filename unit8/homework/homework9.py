# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework9.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月17日 星期六 20时49分10秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

magician = ['liuqian','dawei']
name_change = []
name_change2 = []

def show_magicians(list):
    for name in list:
        print(name)

show_magicians(magician)

def make_great(names,changes):
    while names:
        name = names.pop()
        name = "the Great "+name
        changes.append(name)

make_great(magician,name_change)
show_magicians(name_change)

def make_great2(names,changes):
    while names:
        name = names.pop()
        name = "the Great "+name
        changes.append(name)

make_great2(magician,name_change2[:])
show_magicians(name_change2)
