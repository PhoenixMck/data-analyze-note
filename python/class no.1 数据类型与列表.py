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
# index函数,返回值匹配的第一个匹配项的索引，匹配项可能的区间开始位置和结束位置是可选项
print(23, b.index(1))
# 增加列表 列表名.insert(插入点的索引位置（同样0表示第一个），值)
b.insert(3, 4)  # 把4插入到list的第“3”个位置[实际上第4位]
print(b)
# 倒数第n个同样ok，此时会输出[1,2,3,5,4]
b.insert(-1, 5)
print(b)
# 用append可以表示直接插入到最后，但只能插入一个
b.append(6)
print(b)
# 最后插入多个，可以直接使用集合的计算,但b+[7,8,9]并没有改变b的值,同样的可以使用b+=[7,8,9]
print(b + [7, 8, 9])
b = b + [7, 8, 9]
# 用extend可以连接列表，不同于使用“+”，它会直接修改当前列表,extend的参数是列表，它会把列表中各个元素都补充到原列表中
b.extend([10, 11, 12])
# print(b)
# extend与append的区别，append直接把参数作为一个元素插入列表，参数可以是任何类型，包括列表（因为列表的元素可以是列表）但是直接追加，不会像extend一样处理
b.append([13, 14])
print(b)
# print(b - [8, 9])会报错
# 列表复制 list*n等于list+list+list+……
c = [1, 2] * 3
print(c)
# 移除要用pop,参数为索引,为空则默认删除最后一个，pop方法会返回值，返回的值是被删除的元素——可以使用pop实现删除同时把删除的值存储起来。避免误删同时方便回溯
delete_num = b.pop()
print(b)
print(19, delete_num)
print(b)
b.pop(1)
print(b)
b.pop()
print(b)
# del(基于索引)、remove（可基于值）也可以用于删除
del b[2]
print(b)
del b[:2]
print(b)
# remove() 方法只会删除第一个和指定值相同的元素，而且必须保证该元素是存在的，否则会引发 ValueError 错误。
b.remove(8)
print(b)
# 修改直接用索引切片
b[2] = 3
b[1] = 2
print(b)
# clear清空列表
b.clear()
print(b)
# 二维列表
c = [[1, 2], [3, 4]]
print(c)
b = [3, 4]
d = [1, 2]
c = [b, d]
print(c)
# 第一个元素是[3,4],第二个元素是[1,2]
# 二维列表索引
print(c[0])
print(c[0][1])
# 多维列表的快速生成，numpy更直观
e = [b] * 3  # [b]就是一个以列表b为元素的列表
print(e)

# list可以包含任何类型的数据，甚至变量【直接引用值，但值不会跟着变，因为python是给值附上变量的名，变值==给新值附上旧名】
a = 1
b = 2
c = [a, b]
print(c)
a += 1
print(c, a)
# 对比
d = ["a", "b"]  # 有括号是字符串不是变量
print(d)

# list的映射：对list中的每一个元素都应用同一个函数，在映射为另一个list，原list不变
l = [1, 2, 3]
print([elem - 1 for elem in l], l)  # 把list中每一个元素都暂时赋给变量elem（可起任意名，就是中转站），对elem应用函数计算再返回到list中

# 列表的判断
a = [1, 2, 3]
print([1, 2] < a)
