#!/usr/bin/env python
# coding=utf-8
"""
  Create at 21:12 on 2020/3/7
"""

"""
数字类型的值和字符串类型的值，即使长得一摸一样，也是不相等的，比如 123 和 "123"
这一点在理解上不难理解，但是用起来的时候就会发现困难重重
假设有这么一个场景，我从一个文件里面读出来一个数字 123456
但是因为文件的读取的结果类型都是字符串，这个时候如果我想把它当作数字来用就很麻烦了
还好 python 支持类型转换，也就是，如果字符串里面都是纯数字的，就可以转化成数字，具体用法如下
"""
a = "1234"
b = int(a)  # 这里的 int 就是整数的类型，直接将其作为一个运算符（还记得什么是运算符吗？），就可以将字符串转成整数
print(b)  # 试着打印出来，结果就是 1234
a = "12.3"
try:
    b = int(a)  # 注意，这里这样使用是错误的，因为字符串看起来是个 float 类型，下面才是正确的使用方法
except:
    print("不能使用 int 操作符对明显是 float 类型的数字做类型转化，因为 float 类型的复杂度比 int 复杂")
c = float(a)
print(c)
print(float("123"))  # 但是却可以使用 float 对明显是 int 类型的数字做类型转化

"""
那如果要把数字的运算结果保存到文件里面去呢？数字保存进文件之前得先转换成 string 类型才行，做法如下
"""
a = 1234
b = str(a)  # 没错 str 其实是字符串类型的表示符号，和 int 和 float 一样，也可以做运算符用
print(b)
a = 123.4
b = str(a)  # 也可以对 float 做转化
print(b)

"""
习题：将下面对值从数字转成字符串，或者从字符串转成数字
"""
a = "3.1415"
b = "365"
c = 12
d = 167.5
e = 36.5
