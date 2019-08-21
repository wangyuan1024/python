# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework6.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月21日 星期三 14时19分27秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

number1 = input("Please input a number:")
number2 = input("Please input another number:")
try:
    num1 = int(number1)
    num2 = int(number2)
except ValueError:
    print("This is not a number.")
else:
    print(str(num1 + num2))
