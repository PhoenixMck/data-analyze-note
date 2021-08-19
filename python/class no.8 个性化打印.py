# end参数：在python3里，没有 end =‘ ’，每次 print 语句都会自动换行【因为end默认值为\n】，有了值末尾会用上end的值，且不换行
print("kate is no,1", end=";")
print("morphy is no.2", end=";")
print("Catherine")

# sep参数：分割值与值，即在多个值之间插入默认的值，默认是一个空格
print("a", "b", "c", sep="#")

# file与flush：将内容输入到file里，可以是数据流，也可以是文本等
f = open("sample.txt", 'w')
# flush值为True或者False,表示是否立刻将输出语句输入到参数file指向的对象中,默认False【只有执行f.close()之后才将内容写进文件。】，Ture就马上输入
print("print函数学习", file=f, flush=True)
f.close()

##格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
"""
1.
不需要理会数据类型的问题，在 % 方法中 % s只能替代字符串类型
2.
单个参数可以多次输出，参数顺序可以不相同
3.
填充方式十分灵活，对齐方式十分强大
4.
官方推荐用的方式， % 方式将会在后面的版本被淘汰
"""

# str.format()作为字符串可以调用的一种函数，用 {} 和 : 【:用于在{}中引入格式符的】来代替以前的 %

# 以前是“%s”%变量：基本用法是将值插入到%s占位符的字符串中

# format是把对应的参数放进{}中,参数不限

print("{}{}{}".format("This ", "is ", "Phoenix"))  # {}内为空，后面按顺序输入

# 参数可以不用或用多次，但是前面的{}要保证有值跟它们都对应上

# {}可以指定关键字参数【字典，字典要作为关键字参数调用噢，或赋值】，或者位置参数【对应参数顺序，从0开始】

dic = {"Morphy": "no.1", "Catherine": "no.2", "Kate": "no.3"}

print("{Morphy},{Catherine},{Kate}".format(**dic))

print("{Morphy},{Catherine},{Kate}".format(Morphy="no.1", Catherine="no.2", Kate="no.3"))

print("{1},{0}".format(19, 20))  # {}内的数字锁定参数位置

print('{1}{1}{0}'.format(19, 20))  # 参数一次可多用

# 还可以使用对象属性【超纲以后再说】

# 可以通过索引

a = [17, 18]

b = [6, 7]

print('{0[1]},{1[1]}'.format(a, b))

# list和tuple可以通过“打散”成普通参数给函数，而dict可以打散成关键字参数给函数（通过和**）。所以可以轻松的传个list/tuple/dict给format函数。非常灵活。


# 格式限定符，^、<、>分别是居中、左对齐、右对齐，后面带宽度，:号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充

print("{:a^8}".format(a[0]))  # 把a[0]输出，一共8位，a[0]居中，剩余位数用字符a填充

print("{:a<8}".format(1))

print("{:a>8}".format(2))

# 精度打印

print("{:.2f}".format(1.278))  # 保留两位

# 进制打印

print("{:b}".format(10))  # b、d、o、x分别是二进制、十进制、八进制、十六进制
