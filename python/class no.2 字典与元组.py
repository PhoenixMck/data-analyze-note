# python三大数据结构：列表，字典，元组
# 字典，有两部分，值【value】和键【key】，一一对应，用大括号表示，先键后值
a = {"Catherine": "no.1", "Morphy": "no.2", "Kate": "no.3"}
print(a)
# 可以用键直接索引值,区分大小写
print(a['Catherine'])  # 键是字符串，就要写引号,单双引号一样
# 但是不可以用值直接索引键
# 不可以有重复的键【key】，给原先的键赋值会覆盖,但是值可以重复
a["Kate"] = "no.1"
print(a)
# 可以直接打印字典的键
print(a.keys())
#  get () 函数返回指定键的值，如果值不在字典中返回默认值[none]
print(a.get("Kate"))
# 可以通过赋值直接插入,但列表不可以这样写会报错
a["phoenix"] = "no.4"
print(a)
"""
b = [1, 2]
b[2] = 1 会报错的
print(b)
"""
# 字典是无序的，只有序偶的简单排列，会用类似字母表的方式存储
# 字典的值可以存储任何数据类型的数据，字符串、整数、对象都可以，甚至可以是字典，而且可以混用
# 但字典的键只能说字符串、整数
# 简单的逻辑判断，字典和列表都可以这样写
print("Morphy" in a)
if "Nate" in a:
    print(a)
else:
    print("'nate' isn't in a,add it now")
    a["nate"] = 1
    print(a)
b = [1, 2]
c = 1
if c in b:
    print(c in b)
else:
    print("c isn't in b")
# 字典删除 del允许通过键删除一个独立元素，方法clear可以直接所有
del a["Morphy"]
print(a)
d = a.pop("Kate")  # 效果同del，必须带参数--键,字典使用pop用法同list
print(d)
print(a)
# dict.popitem() 方法随机返回并删除字典中的一对键和值(一般删除末尾对)
a.clear()
print(a)
# 提取字典的键和值并转换成列表
d = {"amy": 1, "john": 2, "nancy": 3}
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))
# 容错提取
print(d.get("name", 1))  # 若无键为name的值，则返回1
# 容错提取并赋值
d.setdefault("name", 0)  # 若无键为name的值，则创建一个键为name，值为0的键值对
print(d)
print(set(d))  # 字典转化为集合
# dict() 函数用于创建一个新的字典，用法与 Pyhon 字典 update() 方法相似。语法：dict(key/value)，参数可为：**kwargs -- 关键字；mapping -- 元素的容器，如zip函数；iterable -- 可迭代对象。
d = dict([(0, 1), (2, 3)])

print(d)

# dict(key/value)，参数可为：**kwargs -- 关键字；mapping -- 元素的容器；iterable -- 可迭代对象。

d1 = dict(name=1, age=19)  # 直接传参，等号前不用打引号

print(d1)

# 对比

d2 = {"name": 2, "age": 18}

print(d2)

d3 = dict(zip(["name", "age"], [1, 2,
                                3]))  # zip（)把多个可迭代对象同一个位置的元素提取出来放在同一个元组内，得到若干元组组成的可迭代对象，单个则直接拆分。如果各个可迭代对象的元素个数不一致，则返回的对象长度与最短的可迭代对象相同。

print(d3)
print(list(zip([1, 2, 3], [2, 4, 5])))

# 在Python3中zip返回的只是一个对象，如果想要得到列表，可以用 list() 函数进行转换。

print(zip(["name", "age"], [1, 2, 3]))

print(list(zip(["name", "age"], [1, 2, 3])))
# 在zip中可以使用 * 号操作符，可以将元组解压为列表

z = list(zip([1, 2, 3], [2, 4, 5]))
print(z)

print(list(zip(*z)))
# dict会直接把可迭代对象里的每个元素（常每个元素是一个含两个值的对象）处理为键值对，因为这里会默认把键值对用元组或列表输入。

d4 = dict(([0, 1], [2, 3]))

print(d4)
# self.fromkeys() 函数用于创建一个新字典，以原字典中元素做字典的键，以输入的参数value为字典所有键对应的初始值。
d = d.fromkeys(d4, 12)
print(d)
# self.update（）把输入的字典参数 的 key/value(键/值) 对补充到字典 self 里【键相同就覆盖】。
d.update(d3)
print(d)

# 元组 tuple 两边用圆括号，不可修改的，其索引依旧为方括号
# 元组相当于一个不可修改的list，一样是用数字索引，可负数可切片(切片同list切片一样，实际是返回一个新元组)
t = (1, 2, 3)
print(t, t[0:2])
print(t.index(2))
# 一个元素的元组,定义一个list、dictionary、tuple的时候都可以在最后的元素上跟上一个逗号，当定义一个只包含一个元素的tuple时逗号是必须的
v = (1,)
print(v)
# tuple没有方法，无法修改。有index和count，可以用in判断是否在元组内，tuple比list更快，所以不需要查看修改，只需要遍历的，用list比用tuple快
# tuple、list转换
l = list(t)
print(type(l), l)
# tuple可以作为字典的一个键，但是list不行，因为字典的键一旦确定无法更改
dic = {t: 1}
print(dic)
