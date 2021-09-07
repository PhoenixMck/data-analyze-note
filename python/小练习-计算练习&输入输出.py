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
