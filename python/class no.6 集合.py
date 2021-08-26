# 集合的声明：大括号，不同于字典没有键值的概念，同时没有索引,无序的，可迭代；可以放数字、字符串,甚至变量
# 集合不同于列表和元组，其中的元素是不可重复的，所以集合在很大程度上能够高效地从列表或元组中删除重复值，并执行取并集、交集等常见的的数学操作
# 初始化空集
# a={}是初始化空字典
a = set([])
print(type(a))
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
e = set([])
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
print(set(d) ^ set(c))  # 交叉补集
# 此处运算符 实际上是位运算符，按位运算符是把数字【注意：布尔变量是可以作为数字参与运算的，所以写条件并列也可以用位运算符】看作二进制来进行计算的

# 不同于列表的直接连接，并集可以去掉重复项，set也可以直接去掉一个列表里的重复项
c = [1, 2, 3, 4, 4, 5, 5, "a", "a"]
print(set(c))
# 子集判断 ture则为子集
p = [1, 2]
print(set(p) < set(c))

b = set([1, 2, 3])
c = set([2, 4, 5])

# 集合的迭代
# 使用减法处理差集
"""
for x in b:
 if x in c:
  b.discard(x)
  这样会报错，因为在这个迭代器中b.discard()对b进行了修改，会影响迭代读取元素，
  所以应该对b进行复制，也就是说被迭代的对象，在迭代过程中要保持不变的
"""
for x in b.copy():  # b.copy()返回一个集合
    if x in c:
        b.discard(x)
print(b)

# 集合计数
print(len(c))

# 集合的值变有序，sorted() 函数对所有可迭代的对象进行排序操作。sort只能应用于列表上，sorted保留原来的对象不变，返回一个新的;reverse参数ture 降序，false升序
a = {1, 8, 7}
print(sorted(a, reverse=True))
"""sorted(iterable, cmp=None, key=None, reverse=False)，
cmp比较的函数，一般写作cmp(x, y)，cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序【字典使用】。
"""

# 推导式, comprehensions（又称解析式），python独有，用于遍历数据序列的。
# 推导式是可以从一个数据序列构建另一个新的数据序列,写作”变量名 = [表达式 for 变量 in 列表 for 变量 in  xxx]”，带条件生成款：变量名 = [表达式 for 变量 in 列表 if 条件]。
# 列表、字典、集合、生成器都可以有推导式
print({k for k in a if k % 2 != 0})  # ==等于 ！=不等于

# 集合中通常不能包含集合等可变的值。即不同于字典、元组、列表可以相互嵌套，集合不可嵌套；
# 只能转换成不可变集合才可以嵌套进可变集合，frozenset()，而不可变集合本身无法修改
# p=frozenset([b,c])会报错,只能有一个吧
p = frozenset()  # 创不可变空集
b = frozenset(b)
c = frozenset(c)
print(set([p, b, c]))

# 可变集合和不可变集合的运算：看谁在前面
p = frozenset([1, 2])
b = set([2, 3, 5])
print(b.intersection(p))
print(p.intersection(b))
