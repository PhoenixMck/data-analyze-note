import random as rd


# 块的导入

# 函数声明 def+函数名+参数【多个参数用逗号隔开，参数也不需要指定数据类型，会自己识别】+":",没有定义返回值的数据类型，甚至不需要定义是否有返回值，若无return则默认返回None
# 文档化函数：让阅读函数的工程师，能够方便的理解函数的作用，函数文档化的位置（在函数名称之后，函数代码块的第一行之间写上代表函数的作用的一句话）
def stringprint(p):
    """自动把字符串列表生成一句话"""  # 三引号最好看
    print(stringprint.__doc__)  # 打印文档注释
    print(";".join(p))


a = ["Kate", "Catherine", "Morphy"]
stringprint(a)


# python中万物皆对象
# 代码缩进，函数唯一的分隔符是”：“，接着的代码本身就是缩进的，python函数没有明显的开始和结束的花括号，也没有begin和end，只是通过缩进来定义，取消缩进代表代码块的结束
# 缩进不一定为4格但必须保持一致
def judgeNum(n):
    """判断n能不能被3整除，不能的话大于它的能被3整除的最小数是多少"""
    # print(judgenum.__doc__)
    if n % 3 == 0:
        print("%d 可以整除3" % n)
    else:
        for i in range(n + 1, n + 3):
            if i % 3 == 0:
                print("%d 可以整除3" % i)
            else:
                i += 1


for k in range(1, 101):
    """测试100次"""
    a = int(rd.random() * 100)
    judgeNum(a)
    k += 1
