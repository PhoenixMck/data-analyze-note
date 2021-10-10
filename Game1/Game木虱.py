import sys
import easygui as e
from class_pleayer import player
import function_Licensing as f
import class_score as sc

"""Game_body:木虱游戏"""

"""进入游戏"""
e.msgbox("欢迎进入木虱")
order = e.buttonbox("准备好开始了吗", choices=["开始", "不想玩啦"])
if order != "不想玩啦":
    """创建玩家对象player1，同时允许玩家给自己命名"""
    player1 = player("P", "")
    player1.get_name()
else:
    order = e.buttonbox("你将离开游戏", choices=["不不，我要留下", "不想玩啦"])
    if order == "不想玩啦":
        e.msgbox("跑喽跑喽下班喽ヾ（≧?≦）〃")
        sys.exit()
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
    player2.get_name()

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
for i in [player1, player2]:
    """i为轮数，每轮发两人"""
    playerlist = []
    for k in [1, 2]:
        (c, p) = f.dealCard(cardLst, playerlist, lst_color, lst_num)
    i.card = p
    print(i.card)

if player2.type == "P":
    """两个人类玩家判断是否继续发牌，command_1"""
    for i in [player1, player2]:
        command_1 = e.buttonbox("来吧人类玩家%s，要不要继续发牌" % i.name, choices=["要", "不要"])
        if command_1 == "要":
            i.command = "Y"
            playerlist = i.card
            (c, p) = f.dealCard(cardLst, playerlist, lst_color, lst_num)
            i.card = p
            print(i.card)
else:
    """如果有电脑玩家，电脑判断是否继续要牌"""
    print("还没开发完呢,去跟人类玩吧")
    sys.exit()

"""获胜判断:计算双方得分
print(sc.score_count(player1.card,player1.command))
print(sc.score_count(player2.card,player2.command))
"""