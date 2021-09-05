# 程序的循环结构:遍历循环【for，循环次数硬编码】、无限循环【while】、break【跳出并结束当前整个循环，执行循环后的语句（一个break只能跳出一层循环，如果有嵌套就只是跳出一层）】和continue循环控制【结束当次循环，进行下一次循环，等于暂停跳过继续下一次】。

# while/for...else：while判断条件不成立时/for遍历完后，执行else语句；但是跳出循环时不能是因为break

"""

while 表达式/for 表达式:

    语句1

	if 表达式：

	break #使用break跳出循环，并没有操作，条件成立如果还是不会去执行else

else:

    语句2



逻辑：在条件语句(表达式)为False时执行else中的“语句2”

"""

# tip：获取输入的次数来作为循环次数，要记得不用加一

for i in range(eval(input("输入打印次数"))):
    print("*")

# while判断N+1次，执行N次

sum = 0  # 要先建立，不可以直接sum+=a，这是运算

a = 0  # 永远记得while的第一步是初始化变量【条件表达式需要时】

while a < 5:
    sum += a

    a += 1

print(sum, a)  # 不同于定义函数，while、if是可以用全局变量的

""" 求100内偶数的和：循环+if，也可以用for"""

a = 0

sum = 0

while a <= 100:

    if a % 2 == 0:
        sum += a

    a += 1

print(sum, a)

# 如果在循环中不需要使用到自定义变量，可以直接将它写成“_”

for _ in range(3):  # 不同于while，for可以在条件这里直接定义变量

    print("加油！")

sum = 0

"""

for i in range(5) if i%2==0:

	sum+=i   错误写法

print(sum)

"""

# IOError 输入输出流错误

# else练习
"""输入密码:3次机会"""

correctPassword = 769

for i in range(3):

    password = eval(input("请输入密码："))

    if password == correctPassword:

        print("密码正确")

        break  # if并不是嵌套循环，break影响的还是for这个循环

    else:

        print("密码不正确")

else:

    print("三次机会结束")
# 嵌套循环：while、for套来套去，套的越多越容易死机【代码越慢】
# pass语句：什么都不做，只是一个占位符，用于语法上需要语句的任何地方，可以在要搭结构但没想好怎么写的时候，写上pass
