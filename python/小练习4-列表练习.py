# 列表练习
"""用list保存用户提供的五个名字并打印"""

a = []

"""一次性获取"""

for i in range(1, 6):
    a.append(input("输入第%d个名字" % i))

"""一次性打印"""

print(",".join(a))  # list可以直接作为join的参数

"""对列表排序并打印，默认升序"""

a.sort()

print(",".join(a))

"""对列表排序并打印，降序"""

a.sort(reverse=True)

print(",".join(a))

"""设计打印只某一个名字"""

num = eval(input("你要打印哪个名字"))

print("第%d个名字是" % num, a[num - 1])

"""设计修改某一个名字并打印"""

num2 = eval(input("你要修改第几个名字")) - 1

print("你要修改的是", a[num2])

newName = input("你要把它修改成")

a[num2] = newName

print("新的列表是", ",".join(a))
