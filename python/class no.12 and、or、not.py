# if扩展

a = 18

if 12 <= a <= 16:

    print("%d在12和16之间" % a)

elif a > 16:  # elif表示继续判断，if后可以接多个elif

    print("{}比16大".format(a))

else:

    print("%d比12小" % a)

# 逻辑表达式 and or not 用于多条件的测试

# and表示两个条件都需要为真时才能执行下面的模块

a = 78

if a % 2 == 0 and a % 3 == 0:

    print("%s为2和3的倍数" % a)

else:

    print("%s不为2和3的倍数" % a)

# or表示两个条件有一个为真时即可执行下面的模块

a = "o4#so"

if "#" in a or "&" in a:

    print("你的密码符合条件")

else:

    print("你的密码不符合条件")

# not表示相反的逻辑

if "*" not in a:
    print("你的密码缺少'*'")

if not ("*" in a):  # 两个写法一样
    print("你的密码缺少'*'")

# “不等于”的逻辑符:<>不可用

a = 9

if (a % 2) != 0:
    print("a为奇数")

# and 或or 进行逻辑判断时都会返回布尔值，但作为三元表达式用于赋值时会返回他们实际比较的值之一，可以视为条件判断的简化

a = 69

b = ""  # 0、“”、[]、{}、None在布尔环境中均为假，其他值为真

print(a % 2 == 0 or a % 3 == 0)  # 输出True

print(a or b)  # 输出69

b = 7

print(a and b)  # 如果所有值均为真则返回最后一个真值
b = ""
print(a and b)  # 如果有值为假，则返回假值

print(a or b)  # or只要遇到真值马上就返回该值，后续不会进行判断；

c = None

print(b or c)  # 如果所有值均为假，则返回最后一个假值

# 三元表达式
# and-or表达式 是一种三元表达式，模拟其他语言的三目计算式，实际上等于if else
# 如 “表达式” and a or b； 从左到右演算，and-or主要是用来模仿 三目运算符 bool?a:b的，即当表达式bool为真，则取a否则取b。则a若为假时就实现不了这一点，可以使用[a]把a放进列表里，因为[""]为真
# 当a为真，先进行and的计算，若“表达式 and a”，若表达式为真则返回a，再进行or的计算，返回a；
# 否则，and计算返回假，or计算返回b【b为真】；
# 当a为假时，1 and a 的结果为假，无论b是否为空，计算完都得到b
d = 90
print(d % 2 == 0 and a or b) #还可以直接用于赋值
print(b if d % 2 == 0 else a) # 变量1 if 表达式 else 变量2 如果表达式为真则返回变量1，否则返回变量2
