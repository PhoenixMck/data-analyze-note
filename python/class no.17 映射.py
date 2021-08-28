from collections.abc import Iterator, Iterable  # 从collections中导入ABCs已被弃用，并在python3.8中将停止工作，可使用collections.abc代替它进行使用

# collections.abc（没错，是collections的一个子模块）模块是在py3中被新引进的（我们将在本文最后对其做简单介绍）
# 过滤、映射的简洁表示
x = 4

target = (x % 2 == 0) and (lambda b: b * 2) or 2
print([target(i) for i in range(3)])
print([i ** 3 for i in range(3)])
print(["str" + str(i) for i in range(3)])

print([i ** 2 for i in range(6) if i % 2 == 0])
print([i ** 2 for i in range(6) if (i % 2 == 0) & (i % 3 == 0)])  # 要加括号啊
print([i ** 4 for i in range(7) if (i % 2 == 0) | (i % 3 == 0)])  # 位运算符的优先级比a逻辑运算符高，所以要打括号啊
# 只要是可迭代对象(iterable)都可以用映射：可迭代对象包括range（）、各种list、提取出来的dict的值、键值对、str【字符串可以看做字符的列表】、tuple、dict【默认情况下，dict迭代的是key】、set
# 可迭代对象性质：可以通过for...in...这类语句迭代读取一条数据供我们使用的对象
# 迭代是访问集合元素的一种方式，迭代器是一个可以记住遍历位置的对象(可迭代对象如list、dic等不是迭代器，列表生成式也是迭代器)

# 可以使用 isinstance() 判断一个对象是否是 Iterable、Iterator 对象
print(isinstance([], Iterator))  # isinstance是一个用来判断对象类型的函数，功能类似与type，参数（对象，可以是直接或间接类名、基本类型或者由它们组成的元组。）
# 如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False。
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系
print(isinstance([], Iterable))
print(isinstance((i ** 2 for i in range(3)), Iterator))
# 可以通过iter()函数获得一个Iterator对象。
# 凡是可作用于for循环的对象都是Iterable类型；凡是可作用于next()函数的对象都是Iterator类型；
# for item in Iterable 循环的本质就是先通过iter()函数获取可迭代对象Iterable的迭代器，然后对获取到的迭代器不断调用next()方法来获取下一个值并将其赋值给item，当遇到StopIteration的异常后循环结束。
# 迭代器是用来帮助我们记录每次迭代访问到的位置，当我们对迭代器使用next()函数的时候，迭代器会向我们返回它所记录位置的下一个位置的数据。实际上，在使用next()函数的时候，调用的就是迭代器对象的__next__方法（Python3中是对象的__next__方法，Python2中是对象的next()方法）。所以，我们要想构造一个迭代器，就要实现它的__next__方法。但这还不够，python要求迭代器本身也是可迭代的，所以我们还要为迭代器实现__iter__方法，而__iter__方法要返回一个迭代器，迭代器自身正是一个迭代器，所以迭代器的__iter__方法返回自身即可。
# 我们分析对可迭代对象进行迭代使用的过程，发现每迭代一次（即在for...in...中每循环一次）都会返回对象中的下一条数据，一直向后读取数据直到迭代了所有数据后结束。那么，在这个迭代过程中就应该有一个“记录员”去记录每次访问到了第几条数据，以便每次迭代都可以返回下一条数据。我们把这个能帮助我们进行数据迭代的“记录员”称为迭代器(Iterator)。可迭代对象的本质就是可以向我们提供一个这样的“记录员”即迭代器帮助我们对其进行迭代遍历使用。
# 可迭代对象通过__iter__方法向我们提供一个迭代器，我们在迭代一个可迭代对象的时候，实际上就是先获取该对象提供的一个迭代器，然后通过这个迭代器来依次获取对象中的每一个数据。那么也就是说，一个具备了__iter__方法的对象，就是一个可迭代对象。
# list、tuple等都是可迭代对象，我们可以通过iter()函数获取这些可迭代对象的迭代器。然后我们可以对获取到的迭代器不断使用next()函数来获取下一条数据。iter()函数实际上就是调用了可迭代对象的__iter__方法。
# 当我们已经迭代完最后一个数据之后，再次调用next()函数会抛出StopIteration的异常，来告诉我们所有数据都已迭代完成，不用再执行next()函数了。
# 迭代器只能往前不会后退，迭代到最后继续访问会从头再开始
# 列表元素可以按照某种算法推算出来，使用时只需要循环该推算出下一个元素，类似于这样的机制被称为生成器（生成器就是一个迭代器）
