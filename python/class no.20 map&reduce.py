# map()函数会根据提供的函数对指定序列做映射，两个参数，第一个是指定的函数，用于对后续可迭代对象的内容进行映射，第二个是可迭代对象，可以是一个或多个，按顺序传入作为前面函数的参数

b = list(map(float, [1, 2, 3, 4]))  # 可以用内置函数或导入模块的函数

print(b)

[x, y, z] = list(map(float, [1, 2, 3]))

print(x, y, z)  # 可以与快速赋值一起使用


def sumab(x, y):
    return x + y


print(map(sumab, [1, 2, 3], [2, 34, 1]))  # map()返回的是一个迭代器，要通过list等函数转换成具体的可迭代对象

print(list(map(sumab, [1, 2, 3], [2, 34, 1])))  # 多个可迭代对象按顺序传入

# map可以直接与匿名函数一起用

print(list(map(lambda x, y: x + y, [1, 2, 3], [2, 33, 1])))

# reduce()使用二元函数、一个可迭代对象作为参数，会对可迭代对象里的元素按顺序输入二元函数，并把输出作为新的参数传入二元函数，直到所有函数计算完毕得到唯一的值

# reduce需要import库functools

from functools import reduce

print(reduce(lambda x, y: x + 2 * y, [1, 2, 3]))  # 2y是错的，要2*y
