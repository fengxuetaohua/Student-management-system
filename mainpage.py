#!/usr/bin/python
# -*- coding: utf8 -*-
import function
while True:
    function.main_function()
    str1 = input("请录入菜单编号:")
    if str1.isdigit():
        main_nuber = int(str1)
        if main_nuber == 1:
            function.student_add()
        elif main_nuber == 2:
            function.student_show_all()
        elif main_nuber == 3:
            function.student_find()
        elif main_nuber == 4:
            function.student_amend()
        elif main_nuber == 5:
            function.student_delete()
        elif main_nuber == 0:
            print("您即将退出管理系统!")
            break
        else:
            print("您输入有误,请重新输入!")
    else:
        print("请重新输入纯数字!")