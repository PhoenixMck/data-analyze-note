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
# lambda为什么print是返回地址：因为lambda只是在定义函数，即使参数赋了值，也没用调用函数的功能，没有调用就没有返回值，可以在定义后赋值给变量后调用，就可以打印了
# lambda的布尔值总是为真，所以他可以用在and-or里作为a不用担心a为假的问题

print(type(1))

x = 4

target = (x % 2 == 0) and (lambda b: b * 2) or 2  # 变成函数，第一个x永远为4，第二个x是定义的局部变量

print(target(9))

x = 3  # target执行时，已经对x%2进行了判断，结果是lambda b；b*2，即target等于lambda不变的了
print(target(9))

