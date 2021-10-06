import random as r
import sys
import easygui as e

"""木虱游戏--双人局"""

"""创建一个纸牌类，纸牌有两个属性：花色【含大小王和功能牌】和大小"""


class card:
    """传递纸牌参数"""

    def __init__(self, color, num):
        self.color = color
        self.num = num


"""创建玩家类，玩家有两种属性：性质【电脑或人类】和姓名"""


class player:

    def __init__(self, type, name):
        self.type = type
        self.name = name

    """方法：获取人类玩家名称"""

    def get_name(self):
        if self.type == "P":
            self.name = input("输入你的名字")
        else:
            self.name = "Eve"


"""方法：不重复发牌"""

global cardLst


def dealCard(cardLst, lst_color, lst_num):
    """发牌"""

    def dealCard2():
        color = r.choice(lst_color)
        num = r.choice(lst_num)
        return color, num

    """大小王检验"""
    (color, num) = dealCard2()
    if (color == "Joker") and (num != 1) and (num != 2) and (num != 3):
        (color, num) = dealCard2()
    """查重"""
    if (color, num) in cardLst:
        (color, num) = dealCard2()
    else:
        cardLst.append((color, num))
    return color, num, cardLst


"""进入游戏"""
e.msgbox("欢迎进入21点")
order = e.buttonbox("准备好开始了吗", choices=["开始", "不想玩啦"])
while order == "不想玩啦":
    order = e.buttonbox("你将离开游戏", choices=["不不，我要留下", "不想玩啦"])
    if order == "不想玩啦":
        e.msgbox("跑喽跑喽下班喽ヾ（≧?≦）〃")
        sys.exit()
    else:
        """创建玩家对象player1，同时允许玩家给自己命名"""
        player1 = player("P", "")
        player1.get_name()
else:
    """创建玩家对象player1，同时允许玩家给自己命名"""
    player1 = player("P", "")
    player1.get_name()

"""对手选择：电脑，P2"""
"""获取选择：弹出选择窗口"""
order_2 = e.buttonbox("欢迎你,%s,你想和谁作战" % player1.name, choices=["电脑就好啦", "当然要邀请P2"])
if order_2 == "电脑就好啦":
    """创建电脑玩家player2，性质为默认"""
    player2 = player("C", "Eve")
"""可以设置游戏难度"""
if order_2 == "当然要邀请P2":
    """再创建一个人类玩家对象play2，性质修改为人类"""
    player2 = player("P", "")
    player1.get_name()

"""可以选择多轮游戏：积分制"""

"""游戏本体"""

"""初始化纸牌"""
"""花色列表"""
lst_color = ["Joker", "黑桃", "红心", "黑梅", "方块"]
"""大小列表"""
lst_num = list(range(1, 11))
lst_num.extend(["J", "Q", "K"])
"""创建本局的纸牌list"""
cardLst = []

"""
第一轮发牌：每人一手两张
创建4个纸牌对象
"""
for i in [1, 2]:
    """i为轮数，每轮发两人"""
    player1_card = []
    for k in [1, 2]:
        (c, n, l) = dealCard(cardLst, lst_color, lst_num)
        thiscard = card(c, n)
        player1_card.append((thiscard.color, thiscard.num))
    print(player1_card)

"""人类判断是否继续发牌，command_1"""
command_1 = e.buttonbox("来吧人类玩家d号，要不要继续发票" , choices=["要", "不要"])
if command_1=="要":
    (c, n, l) = dealCard(cardLst, lst_color, lst_num)
    thiscard = card(c, n)
    player1_card.append((thiscard.color, thiscard.num))
    print(player1_card)
"""再发一张"""
"""如果有电脑玩家，电脑判断是否继续要牌，command_2"""
"""再发一张"""

"""获胜判断"""
