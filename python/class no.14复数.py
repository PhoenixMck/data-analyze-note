# 复数：complex类型，由一个实数和一个虚数组合构成，表示为：x+yj，即一对有序浮点数【实虚都是浮点数】 (x,y)，其中 x 是实数部分,即real部分，y 是虚数部分，即image部分

# 虚数部分必须有后缀j或J，同整数和浮点数一样可以直接创建

a = 12 + 12j

print(a)

print(a.real)

print(a.imag)  # 可以直接打印实部和虚部的数字部分

# conjugate()返回共轭复数【实相同，虚互为相反数】

print(a.conjugate())

# 复数的乘法

"""

复数的乘法法则：把两个复数相乘，类似两个多项式相乘，结果中i2 = -1，把实部与虚部分别合并。两个复数的积仍然是一个复数。

即：z1z2=（a+bi)(c+di)=ac+adi+bci+bdi2=(ac－bd)+(bc+ad)i.

"""

print(a * a.conjugate())

# 复数的除法

"""

复数除法定义：满足（c+di)(x+yi)=(a+bi）的复数x+yi(x,y∈R）叫复数a+bi除以复数c+di的商运算方法：

将分子和分母同时乘以分母的共轭复数，再用乘法法则运算。

"""

b = 11 - 9j

print(a / b)  # 真的可以算哎牛逼了

# print((a.real*b.real+a.imag*b.imag)/(b.real**2+b.imag**2)+((b.real*a.imag-a.real*b.imag)/(b.real**2+b.imag**2))j)

# 内置函数 complex()直接用于复数创建
c=complex(3,4)
print(c)
