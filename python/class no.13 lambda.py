# lambda 函数的语法只包含一个语句，表现形式如下：
# lambda [arg1 [,arg2,.....argn]]:expression,即lambda 参数：函数【函数需要的参数要在前面定义】，即输入函数的参数：函数
"""
可用的参数：
a,b
a=1,b=2
*args
**kwargs
a,b=1.*args,**kwargs
空
"""
# lambda是匿名的，即无名的
# lambda输出的是表达式的返回值
# lambda实际也是一个函数，有自己的命名空间，不能访问其他函数的参数和全局变量
a = lambda x, y: x + y  # x+y本身没有返回值,将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数。
print(a(1, 2))
