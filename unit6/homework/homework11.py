# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework2.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月09日 星期五 20时45分14秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

cities = {
    'beijing':{
        'country': 'china',
        'population': 16,
        'fact': 'prosperous'
    },
    'Los Angeles':{
        'countor': 'USA',
        'population': 2,
        'fact': 'beautiful'
    }
}

for city,truth in cities.items():
    print(city.title() + "'s specialty is:")
    print(truth)
