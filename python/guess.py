"""创建添加功能"""


def addFunction(dict, word, definition):
    """检查单词是否存在"""

    if word in dict:

        print("Wrong input:This word already exists.")

    else:

        dict[word] = definition
        print(dict)


"""创建查询功能"""


def lookFunction(dict, word):
    """检查单词是否存在"""

    if word in dict:

        print(dict[word])

    else:

        print("Wrong input:This word doesn't exist.")


"""创建查询且添加功能"""


def lookAdd(dict, word, definition):
    print(dict.setdefault(word, definition))
    print(dict)


"""获取要使用那种功能"""


def dictTool(dict):
    functiona = input("要使用哪种功能？添加（1）or 查询（2）or 查询并添加（3）")
    inputWord = input("你要添加/查询的词？")
    if functiona == "1":
        inputDefinition = input("为这个词你下的定义是？")
        addFunction(dict, inputWord, inputDefinition)
    elif functiona == "2":
        lookFunction(dict, inputWord)
    elif functiona == "3":
        inputDefinition = input("你在查询单词，当它不存在，你想把它写入字典，你为它下的定义是？")
        lookAdd(dict, inputWord, inputDefinition)
    else:
        print("Wrong input")

