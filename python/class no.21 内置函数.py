# bin(x)把整数x转换成二进制字符串形式
print(bin(12))
# oct(x)把整数x转换成八进制字符串形式
print(oct(18))
# bool(x)把x转换成布尔变量
print(bool("o"))
# chr(x)把x转换成unicode中对应的字符
print(chr(100))
# divmod(x,y)返回x和y的商和余数
print(divmod(4, 3))

# pow(x,y)计算x的y次幂
print(pow(3, 4))
# reversed(r)返回一个组合类型r对应的逆序迭代序列
print(list(reversed(range(2, 12, 2))))
# round(n)四舍五入n，在python3中是四舍六入五成双【五成双的意思是，高位为单数则进1凑成双数，高位为双数则不进位。它的作用是让统计数据更公平，降低舍入的误差。】
print(round(3.5))
print(round(2.5))
# abs()取绝对值
print(abs(-98))
# all(x)x为组合类型变量，只有x中所有数据均为真时，all才返回真
print(all([1,2,3,""]))
# any(x)x为组合类型变量，只有x中所有数据有一个为真时，any马上返回真
print(any([1,2,3,""]))

print(exec("a=1+100"), a)  # exec 返回值永远为 None，但是会执行语句
print(exec("1+19"))  # exec也可以执行表达式，但他的返回值永远为none
