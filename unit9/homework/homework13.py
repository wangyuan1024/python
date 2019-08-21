# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework13.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月20日 星期二 20时32分49秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language['mike'] = 'python'
favorite_language['sarah'] = 'c'

for key,value in favorite_language.items():
    print(key + ' ' + value)
