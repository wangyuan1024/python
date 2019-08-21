# -*- coding: UTF-8 -*-
##########################################################################
# File Name: test.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月21日 星期三 09时06分22秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

f_name = 'learning_python.txt'
with open(f_name) as f_name1:
    lines = f_name1.readlines()
for line in lines:
    c = line.replace('Python','C')
    print(c)
