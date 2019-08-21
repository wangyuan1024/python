# -*- coding: UTF-8 -*-
##########################################################################
# File Name: homework7.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年08月14日 星期三 19时07分09秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

def make_album(name,sang,num=''):
    if num:
        return {"name":name,"sang":sang,"num":num}
    else:
        return {"name":name,"sang":sang}


album = make_album("aaa","bbb")
print(album)
album = make_album("ccc","ddd",3)
print(album)
