#!/usr/bin/python3

# Start
print("Hello, World")

# 多行
# 注释

'''
多行注释
多行注释

'''
# 缩进表示代码块
if True:
    print("True")
else:
    print("False")

print("END")

# 多行语句
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three

totalStr = ['item_one', 'item_two',
            'item_three']
# 字符串

'''
python中单引号和双引号使用完全相同。
使用三引号(\'\'\'或 \"\"\")可以指定一个多行字符串。
转义符 '\'
反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串的截取的语法格式如下：变量[头下标:尾下标]

'''

strTest = 'Huntergai'

print(strTest)
print(strTest[0:-1])  # 从左到右0开始，从右到左-1开始
print(strTest[0])
print(strTest[2:5])
print(strTest[2:])
print(strTest * 2)
print(strTest + "你好")

# 等待用户输入
# input("\n\n按下Enter键后退出")


# import 与 from...import

'''
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *

'''

import sys

print("================Python import mode==========================")
print("命令行参数为：")
for i in sys.argv:
    print(i)
print('\n python路径为', sys.path)

