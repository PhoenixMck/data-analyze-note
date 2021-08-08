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
a.clear()
print(a)

# 元组 tuple 两边用圆括号，不可修改的，其索引依旧为方括号
# 元组相当于一个不可修改的list，一样是用数字索引，可负数可切片(切片同list切片一样，实际是返回一个新元组)
t = (1, 2, 3)
print(t, t[0:2])
print(t.index(2))
# tuple没有方法，无法修改。有index和count，可以用in判断是否在元组内，tuple比list更快，所以不需要查看修改，只需要遍历的，用list比用tuple快
# tuple、list转换
l = list(t)
print(type(l), l)
# tuple可以作为字典的一个键，但是list不行，因为字典的键一旦确定无法更改
dic = {t: 1}
print(dic)
