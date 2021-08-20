# Learning annotation
# 单行注释
"""
第一行注释
第二行注释
"""
# 注释快捷键 ctrl+/

# Learning data type
# python 动态识别+强类型语言
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
# 指数的两种写法
print(3 * 3 * 3)  # 3的三次幂
print(3 ** 3)  # 3的三次幂,这种写法可以计算非整数次幂
print(3 ** 2.5)

# 快速取整(向下取整)
print("9.", int(1.2))
print("10.", int(3 / 2 + 0.1))
# int还可以用于格式转换
print("11.", int("1"))
print("12.", float("1"))

# E记法 处理非常大或非常小的数
print(1.9e11)  # 同1.9E11，即1.9乘以10的11次方
print(1.9e-11)  # 同1.9E-11，即1.9乘以10的负11次方,一般就直接显示e记法

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

# python的三大数据结构：列表，元组，字典
# 列表是[]，列表内的数据就是列表的元素
b = [1, 2, 3]
# 列表求和，可以直接用sum
print(sum(b))
# 列表长度
print(len(b))
# 计数 count
print(22, b.count(1))
# 列表索引,从0开始，任何一个非空列表的第一个元素总是list[0]
print(b[0])
# 输出第n至最后一个
print(b[1:])
# list[m:n]输出第m+1[从0开始，0代表第一个]至n-1个,可以理解为m+1是要的第一个元素,n是第一个不要的元素，返回在之间的所有元素
print(b[:1])
# 输出倒数第n个，即从list尾部开始向前计数来提取元素，任何一个非空列表的最后一个元素总是list[-1]
print(b[-1])
# 另一种理解：b[-1]=b[len(b)-1]
print(b[len(b) - 1])
# 输出第1至倒数n-1个
print(b[:-1])
# 切片返回的是一个新的列表，他是原列表的子集,如果两个索引为空，则表示返回list的所有函数，但此时也是一个全新的list
print(type(b[0:1]))
print(type(b[:]))
# 带步长的切片，list[star:stop:step]这种格式呢，但s表示步进，缺省为1，star开始位置，stop在其前一位停止
print(b[:2:1])
# 如果步长为负数[默认为-1]，且star为缺省时，则star默认为-1，则会从最后一位开始数起；若stop为缺省，则stop默认为-len(list)-1,则会在-len(a)停止；两者均缺省时等于把list从后往前读了
print(b[::-1])


