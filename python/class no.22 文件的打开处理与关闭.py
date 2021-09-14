# 文件的打开
# open()主要参数有file（文件名，与程序文件夹不同时要加全部地址）, mode（打开方式，一个可能是出于安全考虑，另一个可能是为了提高读写速度，要写入磁盘的数据会先放进内存缓冲区，之后再回写，对内容先进行标识，方便识别）, encoding（编码格式，如UTF8），
f = open("sample.txt", "rb")  # 要创建文件对象,一旦打开文件并创建对象就不需要文件名了
# 文件关闭
f.close()  # 要记得关闭对象，关闭后，后续对文件的操作都会报错
# 路径：参数都是字符串啊，所以可以用字符串连接作为某一个参数
PATH = "D:/"
f = open(PATH + "sample.txt", "w")  # 一般"\"会作为格式化打印的标志，如\t，所以输入路径时最好输入/，或者输入\\【如果想要打印\，就必须在前面加入\\】，
f.close()
# 文件对象的属性
f = open("sample.txt", "rb")
print(f.closed)  # f既然是一个对象，就有自己的属性，closed就是其中之一，表示文件现在的状态，当closed的值为false时，对象是打开了文件，当closed为ture则文件关闭
print(f.mode)  # mode属性告诉我们文件以何种方式打开
print(f.name)  # 告诉我们文件对象所打开的文件的文件名

# 文件指针的位置：文件读取是通过指针移动进行的
print(f.tell())  # 告诉我们当前在打开文件中的哪个位置，当返回0说明未移动，文件指针处于起始处
print(f.seek(1, 2))  # 可以在文件中移动到某个位置，两个参数，位置【字节位置】，移动方式【0：从文件开始算起的绝对位置，1：从当前位置算起的相对位置，2：相对于文件末尾的绝对位置】
f.close()

# 文件的读取，在打开方式里要有“r”或者“+”相应声明，即以可读模式（包括 r、r+、rb、rb+）打开的文件
f = open("sample.txt", "r")
context = f.read(1)  # 可带参数，参数代表着读取指定个数的字节/字符串，指定一次最多可读取的字符（字节）个数，并返回含有读取数据的字节流/字符串，当没有传入具体参数时，默认全部读取
print(context)
# 对于文本文件，可以按行读取，从一个文件读取文本行，可以使用readlines()【size参数为读取该行前多少长度的字符串或字节；hint参数为行数，默认为全部读取，自动将文件内容分析成一个行的列表，并返回该列表【是列表就可以迭代了】，每个文本行都作为列表中的一项,空行则返回空字符串】、readline（）【只读一行，返回一个字符串】
# 每次读取后指针都会移动，下次操作都会从当前指针位置开始，所以重复读取的话要退回指针，用seek（0）移动直接到开头位置【seek（2）则直接移动到末尾】
context = f.readlines()
print(context)
f.seek(0)  # 不返回则全部读完,后续无法操作
context_1 = f.readlines(1)
print(context_1)

# 好像也可以直接用
for item in f:  # list（f）可以实现跟readlines一样的效果[每行一个list，每行是一个item]，记得指针要返回
    lst = item.strip("\n").split(",")
    print(lst)

# 写入文件
f = open("sample.txt", "w+")
lst = ["a", "b", "c"]
for item in lst:  # 可以用这种方式写入
    f.write(item + "\n")
f.seek(0)
print(f.read())
# 也可以
lst = ["a\n", "b\n", "c\n"]
f.write("".join(lst))
# writelines 输入后换行，下次写会在下一行写，可以直接把列表写入，
lst = ["e\n", "g\n", "f\n"]  # writelines直接写在同一行
f.writelines(lst)
f.close()
# 追加就是在"a"模式下写东东
f = open("sample.txt", "a")
f.write("\nThat is all!")
f.close()
# 追加写入的时候，要注意前面的写入有没有换行,没有就先补上

# 使用print的重定向写文件
f = open("sample.txt", "w")
print(12 * 12, file=f)  # >>告诉print要把输出发送到文件里而不是屏幕中，它会自动把数字转换成字符串的，如果要在文件中放入文本，print和write都可以
f.close()

# 创建文件，在open中使用”x“模式
f = open("new.txt", "x")
f.close()

# 在文件中保存内容 pickle库的dump函数,pickle模块可以保存序列甚至是模型。当保存模型时，常保存为pkl文件，（pkl文件是python里面保存文件的一种格式，打开后显示一堆序列化的东西），python用来保存固定变量的
import pickle

f = open("new.pkl", "wb")
dic = {"a": 1, "b": 3}
pickle.dump(dic, f)  # 参数要倒入的内容，文件
f.close()
# load函数，拿出被倒入的内容，即把倒入pickle文件的对象，放回到变量中
f = open("new.pkl", "rb")
dic = pickle.load(f)  # 参数要倒入的内容，文件
print(dic)
f.close()
