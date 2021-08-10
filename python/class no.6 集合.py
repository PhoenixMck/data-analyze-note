# 集合的声明：大括号，不同于字典没有键值的概念，同时没有索引,无序的，可迭代；可以放数字、字符串,甚至变量
s = {1, 2}
print(type(s))
# list不可以作为集合的一个元素，和字典一样只能用set转换成集合,字典是键变成集合的元素
# 集合的元素可以是变量，变量存的值不可以是list
a = 1
p = set([a, a])  # set()类似强制类型转换，类似于变量声明
print(p)

# 集合元素的添加和删除
s.add(3)  # 一次只能加一个
print(s)
v = s.pop()
print(s, v)  # 随机删除,会返回被删除的值
"""
s.pop()
print(s,s.pop())
s会被删除两次
"""
# remove 删除指定的值（参数为元素值），但是要注意，如果参数不存在会报错;remove没有返回值
s.remove(2)
print(s)
# set.discard()与remove（）用法相同，但是如果元素不存在，不会报错。也没有返回值
s.discard(1)
print(s)
# clear全部清空
s.clear()
print(s)

# 集合运算——函数
a = set([5, 6, 7])
b = {4, 5, 6}
# set.intersection() 求交集,不改变a
i = a.intersection(b)
print(i)
# set.union(）求并集，去重，不改变a
i = a.union(b)
print(i)
# set.difference()求差集,且是a-b
i = a.difference(b)
print(i)
# set.symmetric_difference()求交叉补集，即a独有的和b独有的的合集
i = a.symmetric_difference(b)
print(i)

# 集合的运算——代码块
c = set([])
for x in a:
    """并集"""
    if x in b:
        c.add(x)
print(c)
d = set([])
for x in a:
    """差集"""
    if x not in b:
        d.add(x)
print(d)
e=set([])
"""交叉补集"""
for x in a:
    if x not in b:
        e.add(x)
for x in b:
    if x not in a:
        e.add(x)
print(e)

# 集合的运算——运算符
c = [1, 2, 3]
d = [3, 4, 5]
print(set(c) & set(d))  # 交集
print(set(c) | set(d))  # 并集且去重
print(set(c) - set(d))  # 差集

# 不同于列表的直接连接，并集可以去掉重复项，set也可以直接去掉一个列表里的重复项
c = [1, 2, 3, 4, 4, 5, 5, "a", "a"]
print(set(c))

# 集合的迭代
