# PythonLearningEveryDay
Python3 Learning

# Python3 解释器

Linux/Unix的系统上，一般默认的 python 版本为 2.x，我们可以将 python3.x 安装在 /usr/local/python3 目录中。
安装完成后，我们可以将路径 /usr/local/python3/bin 添加到您的 Linux/Unix 操作系统的环境变量中，这样您就可以通过 shell 终端输入下面的命令来启动 Python3 。

```
$ PATH=$PATH:/usr/local/python3/bin/python3    # 设置环境变量
$ python3 --version
Python 3.6.0
```

在Window系统下你可以通过以下命令来设置Python的环境变量，假设你的Python安装在 C:\Python34 下:

```
set path=%path%;C:\python34
```

# 脚本式编程

在Linux/Unix系统中，你可以在脚本顶部添加以下命令让Python脚本可以像SHELL脚本一样可直接执行：

`#! /usr/bin/env python3`

然后修改脚本权限，使其有执行权限，命令如下：

`$ chmod +x hello.py`

执行以下命令：

`./hello.py`

# Python运算符优先级

运算符 | 描述
--------- | -------------
** | 指数 (最高优先级)
~ + - | 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % // | 乘，除，取模和取整除
+ - | 加法减法
>> << | 右移，左移运算符
& | 位 'AND'
^ | | 位运算符
<= < > >= | 比较运算符
<> == != | 等于运算符
= %= /= //= -= += *= **= | 赋值运算符
is is not | 身份运算符
in not in | 成员运算符
not or and | 逻辑运算符