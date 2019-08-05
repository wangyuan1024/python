# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework6.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月05日 星期一 16时51分00秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

age = input("Please input a age:")
if age < 2:
    print("He is a baby.")
elif age < 5:
    print("He is a toddler.")
elif age < 14:
    print("He is a kid.")
elif age < 21:
    print("He is a young boy.")
elif age < 66:
    print("He is a adults.")
else:
    print("He is an old man.")
