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
# 简单的逻辑判断
print("Morphy" in a)
if "Nate" in a:
    print(a)
else:
    print("'nate' isn't in a,add it now")
    a["nate"] = 1
    print(a)
# 字典删除 del允许通过键删除一个独立元素，方法clear可以直接所有
del a["Morphy"]
print(a)
a.pop("Kate")  # 效果同del
a.clear()
print(a)
