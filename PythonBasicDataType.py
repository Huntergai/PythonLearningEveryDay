#!/usr/bin/python3

# 多变量赋值

a = b = c = 1

x, y, z = 1, 2, 'huntergai'

# Number
#  int、float、bool、complex（复数）

o, p, q, r = 20, 5.5, True, 4+3j
print(type(o), type(p), type(q), type(r))

# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。

# del 删除对象引用
var1 = 1
print(var1)
del var1

# 数值运算

print(5 + 4)
print(4.3 - 2)
print(3 * 7)
print(2 / 4)
print(2 // 4)
print(17 % 3)
print(2 ** 5)

# 字符串

# 列表 List

# 和字符串类似，只不过字符串不可以元素，列表中可以修改元素

# 元组 Tuple
# 与列表类似，不能修改元素
tuple = ('abc', 786, 2.23, 'huntergai', 70.2)
tinytuple = (123, 'huntergai')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组




