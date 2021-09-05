# 就是把异常放进分支结构里，当出现异常时进行处理，而不是直接暂停程序
# 异常处理是通过try…expect[…else[…finally]]来处理的
# try的工作原理是:
"""
当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生什么依赖于执行时是否出现异常。
如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印默认的出错信息）。
如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。
"""
# try…expect… 最简单的异常处理【expect后不带异常类型】，只要一出现异常就执行expect的内容
a = [1, 2, 3, 7]
try:  # 要加冒号
    a.index(4)
except:
    print("列表中不含4")
    a.append(4)
    print("已添加4", a)
# try…expect[异常内容]… 带异常类型的异常处理，只要一出现规定类型的异常就执行expect的内容，但出现其他类型的异常不在考虑范围内，依旧报错暂停程序
try:
    a.index(5)
except ValueError as o:  # 异常类型相当于变量，值是ValueError后正常报错的内容，可以用as起别名
    print("出错了", o)
    a.append(5)
    print("已添加5", a)
# try…expect…else… 当不带异常时，除了执行try还会奖励执行else的内容
except IndexError as p:  # 还支持多个except
    print("出错了", p)

try:
    a.index(5)
except ValueError:
    print("列表中不含5")
    a.append(5)
    print("已添加5", a)
else:
    print("没错，列表中含有5")


# try…expect…else…finally 无论有无异常，都会执行finally的内容，其他内容正常执行
def trytoadd():
    try:
        a.index(6)
    except ValueError:
        print("列表中不含6")
        a.append(6)
        print("已添加6", a)
    else:
        print("没错，列表中含有6")
    finally:
        print("恭喜你，完成了训练")


trytoadd()
trytoadd()
# 常见异常类型
"""
ZeroDivisionError 除于0
IndexError 序列中没有该索引
NameError 未声明或初始化对象（没有属性）
KeyError 映射中没有该键
SyntaxError 语法错误
ValueError 传入无效参数
TypeError 对类型的无效操作
IOError 输入输出流错误
"""
