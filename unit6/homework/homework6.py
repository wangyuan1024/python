# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework6.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月10日 星期六 09时55分12秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

human = ['phil','sarah']
for key in favorite_language.keys():
    if key in human:
        print(key.title() + ",thanks for your survey.")
    else:
        print(key.title() + ",hope you come on.")
