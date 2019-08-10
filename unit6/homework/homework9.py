# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework9.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月10日 星期六 22时49分06秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

favorite_places = {
    'wangyuan':['qingdao','shenzhen'],
    'xinyincheng': ['chengdu'],
    'suzhuoran': ['hangzhou','chengdu']
}
for person,place in favorite_places.items():
    print(person.title() + "'s favorite place:")
    print(place)
