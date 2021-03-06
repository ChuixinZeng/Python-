# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
# 第一段代码，无法运行，没有定义bar
# 相当于bar没有对应的房间，只有门牌号
# def foo():
#     print("in the foo")
#     bar()
# foo()

# 第二段示例代码，可以运行
# bar有房间了，也有门牌号
# def bar():
#     print("in the bar")

# def foo():
#     print("in the foo")
#     bar()
# foo()

# 第三段示例代码，可以运行
# Python是解释运行的语言，所以定义x=1,y=2，或者先定义y=2,x=1，没什么区别
# 所以这一段代码和上一段没什么区别，foo和bar相当于两个“变量”，先定义谁都一样，都解释在内存里了
# def foo():
#     print("in the foo")
#     bar()

# def bar():
#     print("in the bar")
# foo()

# 第四段示例代码，不能运行，报错：没有定义bar
# 应该先声明再调用，只要在调用之前存在了，就可以，下面的在调用之前不存在

# def foo():
#     print("in the foo")
#     bar()
# foo()
# def bar():
#     print("in the bar")

# 函数即“变量”
#    1、变量的值相当于内存这个大房间中的一个小房间，而变量名相当于这个小房间的门牌号，门牌号被清理掉了，房间就没有了
#       1.1 只要变量名没有被del删掉，那会一直驻留在内存里面，直到程序运行结束
#    2、函数也是类似，函数体相当于大房间中的小房间，而函数名相当于这个房间的门牌号
#    3、匿名函数没有函数名称，但也是一样找个房间存放函数体，匿名函数没有门牌号，把匿名函数赋给变量，相当于就有了门牌号