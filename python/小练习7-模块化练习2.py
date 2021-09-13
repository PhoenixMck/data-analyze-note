import guess as g

"初始化字典"
print("请初始化你的字典（仅一个单词哦）")
w = input("你的单词是")
definition = input("你的定义")
dic = {w: definition}  # 这里写dict(w=definition)会报错，因为这是赋值语句，如果两端都是变量，a=b，则是把b的值传递给a
order = "Y"
while order == "Y":
    g.dictTool(dic)
    order = input("是否继续操作字典，Y or N").upper()
    if (order != "Y") and (order != "N"):
        order = input("输入错误，请重新输入，Y or N").upper()
else:
    print("关闭字典")
    if input("是否打印字典？Y or N").upper() == "Y":
        print(dic)
