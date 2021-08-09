# 变量声明（变量首次赋值）变量有全局和局部之分，但不像其他语言有明显的变量声明，通过首次复制即可产生，超出使用范围自动消亡
# 一次赋多值，使用tuple即可
v = ("a", "b", "c")
(x, y, z) = v  # 实际上就是把一个tuple中的每一个值按顺序附给变量tuple中的每一个变量
print(x, y, z)
# 可以使用range()连续赋值
(x, y, z, p) = range(4)  # range()从0开始
print(z, p, x, y)
# 可以使用tuple一次性返回多个参数，只需返回含所有值的tuple、同时可以使用tuple赋值给其他变量，也可以使用range输入参数

# 格式化字符串：函数/把值插入到一个有字符串格式符%s（%s s会被后续的变量按顺序替代）的字符串中,代表强制类型转换
k = 1
v = 2
print("%s<%s" % (k, v))  # 有点类似tuple的连续赋值
# 字符串格式化可通过%d处理整数，字符串连接符不能连接非字符串的内容
print("my id is %d" % k)
# %f处理十进制浮点数，不指定精度是打印6位小数，指定精度的写法是%.nf,n为位数，%+.nf会加上一个正号
print("his id is %+.3f" % v)

# dictionary的items函数：把字典里的键值一一对应打印出来，返回一个类似(keys,value)的若干tuple组成的list
d = {"kate": 1, "Morphy": 2, "Catherine": "3"}
print(d.items())
# 方法联动："%s 's id is %s"%(k,v) for k,v in d.items()会生成了一个迭代器，把它变成list就可以正常输出了
print(["%s 's id is %s" % (k, v) for k, v in d.items()])

# 连接和分割字符串
# 任意字符串均可调用join函数可用于连接,结果每个元素用“；”隔开，join只能用于元素都是字符串的list
print(";".join(["%s 's id is %s" % (k, v) for k, v in d.items()]))
p = ["Morphy", "Kate", "Catherine"]
st = "-".join(p)
print(st)
# 任意字符串均可调用split函数对其自身分割，将生成一个list,第一个参数是分割符，第二个参数是分割次数。分割符会被完全去掉
print(st.split("-"))
# 如果想搜索一个字符串，然后分别处理前半部分和后半部分可以使用split
print(st.split("-", 1))
