import random as r

global cardLst
global playerlist


def dealCard(cardLst, playerlist, lst_color, lst_num):
    """发牌"""
    """创建一个纸牌类，纸牌有两个属性：花色【含大小王和功能牌】和大小"""
    def dealCard2():
        color = r.choice(lst_color)
        """大小王检验"""
        if color=="Joker":
            num=r.choice([1,2,3])
        else:
            num = r.choice(lst_num)
        return color, num
    (color, num) = dealCard2()
    """查重"""
    while (color, num) in cardLst:
        (color, num) = dealCard2()
    else:
        playerlist.append((color, num))
        cardLst.append((color, num))
    return cardLst, playerlist

