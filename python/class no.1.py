# Learning annotation
# 单行注释
"""
第一行注释
第二行注释
"""
# 注释快捷键 ctrl+/

# Learning data type
# python 弱类型语言
print("1.", 1 + 1)

# 两大数字类型：整数、浮点数
# int 整数
print("2.", type(1))
# 整数加整数
print("3.", type(1 + 1))
# float 浮点数
print("4.", type(1.2))
# 整数加浮点数 浮点数
print("5.", type(1 + 1.2))

# 快速计算：取余求整除
# 正常除
print("6.", 3 / 2)
# 整除
print("7.", 7 // 4)
# 求余数
print("8.", 7 % 4)

# 快速取整(向下取整)
print("9.", int(1.2))
print("10.", int(3 / 2 + 0.1))
# int还可以用于格式转换
print("11.", int("1"))
print("12.", float("1"))

# 数据类型：字符串
# 单双引号一样的
print(type('a'))
print(type("a"))
print('hello')
print("hello")
# 引号做标识符
print("he says 'hello'")
# 三引号
print('''the book says "he says 'hello'"''')
# \的使用:\'用于强调’是‘不是标识符
print('\'\'')
# str用于格式转换
print("13.", str(1))

# 布尔变量
print("14.", type(True))
print("15.", type(False))
# 布尔函数可以直接计算，记得大写
print(True + 1)
print(False + 1)
# 逻辑式也可以直接进行运算
print("16.", 1 < 2)
# 逻辑运算优先于数字运算
print("17.", 1 + 1 < 2)
# 括号优先于逻辑运算
print("18.", (1 + 1) < 2)

# 空值，不可计算
print(None)

# 变量【实际就存在内存里】，一般用英文，python中没有常量，python中定义常量本质上就是变量
a = 1
print(a)
# 快速计算 a+=1 == a=a+1
a += 1
print(a)
a += 2
print(a)
# 变量 随时可以更新值
a = 'string'
print(a)

# python的三大数据结构：列表，数组，字典
