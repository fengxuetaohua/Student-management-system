# !/usr/bin/python
# -*- coding: utf8 -*-


# 首页面
def main_function():
    print("****************************************")
    print("欢迎使用【学生管理系统】v1.0")
    print("1.添加学生")
    print("2.显示全部")
    print("3.查找一个学生")
    print("4.修改一个学生")
    print("5.删除一个学生")
    print("0.退出系统")
    print("****************************************")


# 定义读取文件的函数
def read_file():
    student_database = []
    # 以r形式读文件,如果没有这个文件不会创建新文件.
    f = open('student_database.txt', 'r')
    for line in f:
        my_dict = eval(line)
        student_database.append(my_dict)
    return student_database


# 获取将学生数据库全部内容读取到student_database这个列表中,全局变量
class public_fuction():
    # 录入学生信息,组成字典
    def Create_dict(self):
        name = input("请录入姓名")
        tel = input("请录入电话号码")
        weixin = input("请录入微信")
        adress = input("请录入住址")
        dict1 = {'姓名': name, '电话': tel, '微信': weixin, '地址': adress}
        return dict1

    # 查询是否重复
    def Duplicates(self,dict2):
        student_database=read_file()
        for i in student_database:
            if (dict2) == i:
                return '重复'

    def isdigit(self,str1):
        if str1.isdigit():
            return int(str1)
        else:
            return 0


# 定义添加学生模块
def student_add():
    while True:
        add = public_fuction()
        # 添加字典
        dict1 = add.Create_dict()
        # 判断字典信息是否与数据库信息重复
        result = add.Duplicates(dict1)
        # 判断为空时
        if dict1.get('姓名') == "":
            answer = input('对不起，姓名不能为空，请重新输入姓名，退出请输入1')#提示为空,是否退出
            answer = add.isdigit(answer)
            # 回答不退出
            if answer != 1:
                # 不再执行下面的语句,返回循环继续添加
                continue
            else:
                # 跳出循环,停止添加功能
                break
            # 判断重复时
        elif result == '重复':
            answer = input('对不起，您输入的学生信息已存在，请重新输入，退出请输入1') # 提示信息重复,是否退出
            answer = add.isdigit(answer)
            # 回答不退出
            if answer != 1:
                # 不再执行下面的语句,返回循环继续添加
                continue
            else:
                # 提示退出
                print("即将退出!!!")
                # 跳出循环,停止添加功能
                break
        else:
            # 以追加的形式打开文件
            f = open('student_database.txt', 'a')
            # 写入并换行
            f.write(str(dict1)+'\n')
            f.close()
            print("添加信息成功,即将退出!")
            break


# 展示全部学生信息模块
def student_show_all():
    student_database = read_file()
    print(f'当前录入学生个数为{len(student_database)},显示如下:')
    print("姓名".ljust(15)+"电话".ljust(13)+"微信".ljust(15)+"地址".ljust(15))
    print("-----------------------------------")
    for dict in student_database:
        for value in dict.values():
            print(value.ljust(15), end="")
        print()
    print("-----------------------------------")


# 查询学生信息模块
def student_find():
    student_database = read_file()
    name = input("请输入您要查找的学生姓名:")
    for dict in student_database:
        if name == dict.get("姓名"):
            print("您要查找的学生信息如下:")
            print("姓名".ljust(15) + "电话".ljust(13) + "微信".ljust(15) + "地址".ljust(15))
            print("-----------------------------------")
            for value in dict.values():
                    print(value.ljust(15), end="")
            print()
            print("-----------------------------------")
            break
    else:
        # 当且仅当不执行break的时候才打印
        print("对不起没有你要查询的学生信息!")


# 修改学生信息模块
def student_amend():
    student_database = read_file()
    name = input("请输入您要修改的学生姓名:")
    for dict in student_database:
        # 如果数据库里有要修改的学生姓名,则执行下面操作
        if name == dict.get("姓名"):
            while True:
                add = public_fuction()
                # 添加字典
                dict1 = add.Create_dict()
                # 判断字典信息是否与数据库信息重复
                result = add.Duplicates(dict1)
                # 判断为空时
                if dict1.get('姓名') == "":
                    answer = input('对不起，姓名不能为空，请重新输入姓名，退出请输入1')  # 提示为空,是否退出
                    answer = add.isdigit(answer)
                    # 回答不退出
                    if answer != 1:
                        # 不再执行下面的语句,返回循环继续添加
                        continue
                    else:
                        # 跳出循环,停止添加功能
                        break
                        # 判断重复时
                elif result == '重复':
                    answer = input('对不起，您修改的学生信息与已存在的学生信息重复，请重新输入，退出请输入1') # 提示信息重复,是否退出
                    answer = add.isdigit(answer)
                    # 回答不退出
                    if answer != 1:
                        # 不再执行下面的语句,返回循环继续添加
                        continue
                    else:
                        # 提示退出
                        print("即将退出!!!")
                        # 跳出循环,停止添加功能
                        break
                else:
                    # 删除原来的信息
                    student_database.remove(dict)
                    # 添加现在的信息
                    student_database.append(dict1)
                    # 以重新写入的形式打开文件
                    f = open('student_database.txt', 'w')
                    for i in student_database:
                        # 写入并换行
                        f.write(str(i) + '\n')
                    f.close()
                    print("添加信息成功,即将退出!")
                    # while内的break跳出的是while循环
                    break
            # 与while齐平,跳出的是外面的for循环
            break
    else:
        # 当且仅当不执行break的时候才打印
        print("对不起没有你要修改的学生信息!")


# 删除学生信息模块
def student_delete():
    student_database = read_file()
    name = input("请输入您要修改的学生姓名:")
    for dict in student_database:
        # 如果数据库里有要修改的学生姓名,则执行下面操作
        if name == dict.get("姓名"):
            # 删除原来的信息
            student_database.remove(dict)
            # 以重新写入的形式打开文件
            f = open('student_database.txt', 'w')
            for i in student_database:
                # 写入并换行
                f.write(str(i) + '\n')
            f.close()
            print("删除信息成功,即将退出!")
            break
    else:
        print("对不起没有你要修改的学生信息!")