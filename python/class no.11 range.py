# range()生成不可变的等差整数列表，range(start, stop [,step]) 是一个左闭右开的区间，start 指的是计数起始值，默认是 0；stop 指的是计数结束值，但不包括 stop ，也可为0，step是步长，默认为1，不可为0，只能为整数,不可以是浮点数或者其他类型的数据

print(range(1, 3))  # 直接返回range对象，是不可变的等差列表

print(type(range(1, 3)))

print(len(range(1, 3)))

a = 2

for i in range(2, 10, a):  # step可以是变量，但是必须是整数类型的

    print(i, end=" ")

print()

# 递减等差的写法：步长为负，同样左闭右开，左边要大于右边,否则就反方向取值了

for i in range(3, 0, -1):  # 不含0哦
    print(i, end=" ")

print()

# range是不可变的序列类型，但是是一个可迭代的对象，可以进行判断元素、查找元素、切片等操作，但不能修改元素；
# 官方是这样明确划分的——有三种基本的序列类型：列表、元组和范围（range）对象。
print(range(0, 3)[0])  # 可以直接作为对象哦
print(2 in range(0, 3))
print(range(0, 3).index(1))
print(range(0, 3)[:-1])  # 返回的还是序列类型,切片同list

"""
在 for-循环 遍历时，可迭代对象与迭代器的性能是一样的，即它们都是惰性求值的，在空间复杂度与时间复杂度上并无差异。
过两者的差别是“一同两不同”：相同的是都可惰性迭代，不同的是可迭代对象不支持自遍历（即next()方法），而迭代器本身不支持切片（即__getitem__() 方法）。
"""
#range()序列可以转化为list

print(list(range(2)))
