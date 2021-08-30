# input函数 用于获取用户的输入并返回，可以直接赋给变量为值，其接收任意输入。将所有输入默认为字符串处理，并返回字符串类型。
str_a = input()
# input与print连用
print("你的字符串是", input())  # 先输入再print
# input可以带字符串参数，字符串会被print，终端会获取字符串打印后的输入,并作为字符串返回，可以强制转化
str_b = int(input("输入任意整数"))
print(str_b)

# 可以用eval对input的结果进行转化
# eval()函数用来执行一个字符串表达式【表达式一定要是可以被解析和计算的，或有意义的【即eval是起到去掉引号的作用，去掉引号后读表达式找变量，如果变量可以计算的话就会对他进行计算了，如果不可以计算就会判断式子是否有意义】】，并返回表达式的值。还可以直接把字符串转换成列表、字典、元组
print(eval("[1,2,3]"))
# print(eval("abk"))报错
x = 7
print(eval("x*7"))
# eval(expression[, globals[, locals]]),expression ： 表达式。
# globals ： 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。locals ： 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
# 当后两个参数都为空时，很好理解，就是一个string类型的算术表达式，计算出结果即可。等价于eval(expression)。
print(eval("x*7", {"x": 8}))  # 当locals参数为空，globals参数不为空时，先查找globals参数中是否存在变量，并计算，有则计算。
print(eval("x*7", {"x": 8}, {"x": 6}))  # 当两个参数都不为空时，先查找locals参数，再查找globals参数。

# eval与input的使用
a = eval(input("输入一个列表"))  # 利用input获取用户输入的字符串【input会把用户输入的内容，包括数字都默认为字符串】和eval直接把字符串转换成列表的功能
print(a)
x = 5
b = eval(input("输入你的公式"))  # 支持input多种内容，如x*7，float(x)都可以处理
print(b)


# 把函数赋值给变量，两种形式，变量=函数名【不带括号】，变量=函数名()
# 第一种
def suma(x, y):
    return x + y


a = suma  # a直接与suma等价，调用a等于调用suma，直接运行一遍suma
print(a(1, 2))  # print不能print print函数只能print函数返回值


def sumb(x, y):
    print(x + y)


b = sumb
b(1, 3)  # 调用b等于调用sumb，直接运行一遍sumb
