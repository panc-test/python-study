"""
迭代：访问集合元素的一种方式，可以遍历集合中的所有元素。
迭代的好处：节省内存空间，迭代是读取多少元素，就将多少元素装载到内存中，不读取就不装，。

原生的可迭代对象：list, tuple, dict, set, str  不是迭代器


"""
from collections.abc import Iterable,Iterator

list = [2,3,4]
tuple = (0,3,5)
str = "adafaf"

print(isinstance(list,Iterable))    #判断是否可迭代
print(isinstance(list,Iterator))    #判断是否是迭代器


#iter() 函数可以将可迭代对象转化成迭代器
print(type(iter(list)))
print(isinstance(iter(list),Iterator))