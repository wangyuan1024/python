# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework14.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月20日 星期二 20时36分55秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

from random import randint

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        self.sides = randint(1,6)
        print(self.sides)

    def roll_die10(self):
        self.sides = randint(1,10)
        print(self.sides)

    def roll_die20(self):
        self.sides = randint(1,20)
        print(self.sides)

die = Die()
for i in range(10):
    die.roll_die()
for i in range(10):
    die.roll_die10()
for i in range(10):
    die.roll_die20()
