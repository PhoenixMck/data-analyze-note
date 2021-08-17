# __name__测试模块

# 一个python文件通常有两种使用方法，第一是作为脚本直接执行，第二是 import 到其他的 python 脚本中被调用（模块重用）执行。

# if __name__ == '__main__'：【要带引号，name和main前后都是两个下划线】的用法：用于测试程序是否作为脚本被直接执行，调用上文的模块

# __name__是模块的内置属性，如果是import了模块，那么此时__name__通常是模块的文件名，不带路径和扩展名，如果是作为脚本被直接执行，则__name__是一个特殊的缺省值"__main__"

def printing(x, y):
    print(x + y)


if __name__ == '__main__':
    # if 表示逻辑判断，并不影响上文的执行，所以如果后文有调用，上面的代码也会执行，只是会先执行if

    # 因为Python虽然是顺序执行的，但首先执行依旧是最先出现的非函数定义和非类定义的没有缩进的代码，在这里为if，一般类中的代码和函数中的代码不会执行 (除非后文有被调用)

    print("直接调用")

printing(2, 3)


# 如何让定义的函数自己无调用也运行，使用__name__ == '__main__':
def main():
    print("we are in %s" % __name__)


if __name__ == '__main__':
    main()  # 实际跟前面的main函数是两个代码块的了
