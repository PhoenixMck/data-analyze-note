# random库【生成随机数，使用的是伪随机数算法】 random.random是最核心的函数,生成一个0到1之间的随机小数，其他随机数都是在这个函数的基础上衍生的
import random as r#【常命名为r】
print(r.random())
#随机数的生成依赖于种子，种子相同随机数相同。种子默认值为当前系统时间，用seed()设定
r.seed(10)
print(r.random())
print(r.random())
a=r.randint(2,10)#生成【a，b】之间【含a，b】的随机整数
print(a)
a=r.getrandbits(2)#生成k比特长度的随机整数
print(a)
a=r.randrange(1,18,3)#【start，stop，[step]】生成一个在范围内的步长为step内的随机整数
print(a)
b=r.uniform(2,8)#生成【a，b】之间的随机小数
print(b)
b=r.choice([1,9,2,34,4])#在序列类型中随机返回一个元素
print(b)
c=r.shuffle([1,9,2,34,3,4])#把序列类型随机排列，返回排序后的序列
print(c)
c=r.sample([1,9,2,34,3,4],4)#从pop类型中随机选取k个元素并返回一个新的列表【有点像随机取样】
print(c)
r.seed(10)
print(r.random())
print(r.random())
a=r.randint(2,10)#生成【a，b】之间【含a，b】的随机整数
print(a)#果然只要种子一样，r所有函数出来的都一样--伪随机数的不安全性