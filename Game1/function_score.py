"""判断玩家得分，需要玩家的牌的列表"""


def extract(list):
    c_lst = []
    n_lst = []
    """还是把牌搞成列表方便"""
    for i in range(len(list)):
        c_lst.append(list[i][0])
        n_lst.append(list[i][1])
    """处理JQK"""
    while "J" in n_lst:
        n_lst[n_lst.index("J")] = 11
    else:
        while "Q" in n_lst:
            n_lst[n_lst.index("Q")] = 12
        else:
            while "K" in n_lst:
                n_lst[n_lst.index("K")] = 13
    return c_lst, n_lst


def score_count(list, command):
    """
    event1. 三鬼：三张牌且都是大小王(无癞子就没有三鬼)20倍
    event2. 双鬼：两张牌且都是大小王(首轮牌)10倍
    event3. 天空九：两张牌且9点(首轮牌)
    event4. 天空八：两张牌且8点(首轮牌)
    event5. 同花顺：三张牌组成顺子且同花 8倍
    event6. 三条：三张牌点数相同 5倍
    event7. 顺子：三张牌组成顺子234~QKA 4倍
    event8. 木虱：点数个位数为0，只能吃双鬼
    event9. 三张同花 3倍
    event10.两张同花2倍
    event11.对子 2倍
    event12. 9点~1点 1倍
    """
    points = 0
    multiple = 1
    event = 0
    (c_lst, n_lst) = extract(list)

    """获胜判断"""
    if c_lst.count("Joker") == 3:
        multiple = 30
        event = 1
    elif command == "N":
        if c_lst.count("Joker") == 2:
            multiple = 20
            event = 2
        elif sum(n_lst) % 10 == 9:
            multiple = 9
            event = 3
        elif sum(n_lst) % 10 == 8:
            multiple = 8
            event = 4
        elif len(set(c_lst)) == 1:
            multiple = 2
            event = 10
        elif len(set(n_lst)) == 1:
            multiple = 2
            event = 11
    elif len(set(c_lst)) == 1 and command == "Y":
        multiple = 5
        event = 6

    return multiple, event
