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

strTest = 'Huntergai'

print(strTest)
print(strTest[0:-1])  # 从左到右0开始，从右到左-1开始
print(strTest[0])
print(strTest[2:5])
print(strTest[2:])
print(strTest * 2)
print(strTest + "你好")

# 等待用户输入
input("\n\n按下Enter键后退出")


