"""创建一个字典，用户可以添加单词和定义"""

"""创建一个空字典"""

a = {}

"""目录：功能查询"""

function = input("Add or look a word?A or L")

if function == "A":

    word = input("What is your word?")

    definition = input("What is its definition?")

    """检查单词是否存在"""

    if word in a:

        print("Wrong input:This word already exists.")

    else:

        a[word] = definition
        print(a)

elif function == "L":

    function2 = input("Only Look or Look and Add?1 or 2")
    if function2 == "1":
        word = input("What is your word?")

        """检查单词是否存在"""

        if word in a:

            print(a[word])

        else:

            print("Wrong input:This word doesn't exist.")
        """检查单词是否存在，不存在则添加"""
    elif function2 == "2":
        word = input("What is your word?")
        newDefinition = input("What is its definition?")
        """If the word don't exist,add the newDefinition for it.Or print  its definition"""
        print(a.setdefault(word, newDefinition))
        print(a)
    else:
        print("Wrong input")

else:

    print("Wrong input")
