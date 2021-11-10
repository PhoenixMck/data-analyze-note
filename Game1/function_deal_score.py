
def singlescore(end):
    """
    event1. 三鬼：三张牌且都是大小王(无癞子就没有三鬼)40倍 level:1
    event2. 双鬼：两张牌且都是大小王(首轮牌)20倍 level:1
    event3. 天公九：两张牌且9点(首轮牌) level:2
    event4. 天公八：两张牌且8点(首轮牌) level:2
    event5. 同花顺：三张牌组成顺子且同花 8倍 level:3
    event6. 三条：三张牌点数相同 5倍 level:3
    event7. 顺子：三张牌组成顺子234~QKA 4倍level:3
    event8. 木虱：点数个位数为0，只能吃双鬼level:0
    event9. 三张同花 3倍 level:3
    event10.两张同花2倍 level:3
    event11.对子 2倍 level:3
    event12. 9点~1点 1倍 level:4
    """

    """
    end是五种计算方式下得到的(level, event, multiple, points)的列表
    """
    level = min(end, key=lambda x: x[0])[0]
    multiple = max([k for k in end if k[0] == level], key=lambda x: x[2])[2]
    event=list(set([k[1] for k in end if k[0]==level and  k[2]==multiple]))[0]
    if level == 4:
        points = end[0][3]
    else:
        points = None
    """判断是不是木虱"""
    if 0 in [k[0] for k in end]:
        s = 1
    else:
        s = 0
    print("你的结果是，当前属于事件%d，倍数为%d，点数为%s,等级为%s" % (event, multiple, points, level))
    return level, event, multiple, points, s


if __name__ == '__main__':
    n = [(4, 12, 1, 3), (4, 12, 1, None), (4, 12, 1, None), (3, 6, 5, 3), (4, 12, 1, None)]
    print(singlescore(n))
