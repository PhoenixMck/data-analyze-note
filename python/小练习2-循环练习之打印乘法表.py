
# 循环练习
""" 乘法表打印"""
num = eval(input("你要打印谁的乘法口诀，范围1~9"))
for i in range(1, 10):  # for里的i会自己变的噢
    print("%d * %d=" % (i, num), i * num)  # 多变量与%连用要用元组框起来噢
"""用while的写法"""
i = 1
while i < 10:
    print("%d * %d=" % (i, num), i * num)  # 多变量与%连用要用元组框起来噢
    i += 1
"""任意相乘打印"""
num = eval(input("你要打印谁的乘法口诀，范围1~9"))
rangeNum = eval(input("你要打印到的最大范围是，范围1~100"))
for i in range(1, rangeNum + 1):  # rangenum只是用来确定次数时，就可以从0开始，不用加1，但是如果用来算，那就记得加1
    print("%d * %d=" % (i, num), i * num)  # 多变量与%连用要用元组框起来噢
"""用while的写法"""
i = 1
while i <= rangeNum:
    print("%d * %d=" % (i, num), i * num)  # 多变量与%连用要用元组框起来噢
    i += 1