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

get_input_name = ""
get_input_sang = ""
get_input_num = ""
while True:
    get_input_name = input("Please input name: ")
    if get_input_name == 'q':
        break;
    get_input_sang = input("Please input sang: ")
    if get_input_sang == 'q':
        break;
    get_input_num = input("Please input num: ")
    if get_input_num == 'q':
        break;
    get_end = make_album(get_input_name,get_input_sang,get_input_num)
    print(get_end)
