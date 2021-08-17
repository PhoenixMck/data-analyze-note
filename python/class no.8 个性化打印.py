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

#fomat()