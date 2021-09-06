# 计算练习
print("每人要付出", int(35.27 * 1.15 / 3) + 1, "元")  # 分饭费问题，向上取整
print("每人要付出", round(35.27 * 1.15 / 3, 2), "元")  # 分饭费问题，自动取两位小数
print("每人要付出{:.2f}元".format(35.27 * 1.15 / 3))
a = 35.27 * 1.15 / 3
print(a)
print("每人要付出 %.2f 元" % a)

# 输入输出练习
"""姓名输入并打印"""
firstName = input("输入你的名")
lastName = input("输入你的姓")
print(firstName, " ", lastName)
print("你的姓是%s，你的名是%s" % (lastName, firstName), "你的名字是", lastName, firstName)
"""计算地毯"""
length = float(input("输入房间的长（单位：米）"))
width = float(input("输入房间的宽（单位：米）"))
square = length * width
print("房间的面积是", square, "平方米")
price = float(input("输入每平方米地毯的价格（单位：元）"))
print("房间的地毯价格是", square * price, "元")

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
"""倒计时工具，同时嵌套对应的星号打印，不嵌套时间计数更精准"""
import time

sleepTime = eval(input("输入倒数时间"))
for i in range(sleepTime, 0, -1):
    print("%2d" % i, end="")  # 格式化输入，保证每一个数字都是两个位
    # print("Start : %s" % time.ctime())
    for v in range(i):
        print("*", end="")  # 嵌套打印星号
    else:
        print()
        time.sleep(1)
        # print("End : %s" % time.ctime())
print("time's up")
