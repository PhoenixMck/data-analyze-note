import function_deal_card as dc
import abc

"""
event1. 三鬼：三张牌且都是大小王(无癞子就没有三鬼)40倍
event2. 双鬼：两张牌且都是大小王(首轮牌)20倍
event3. 天公九：两张牌且9点(首轮牌)
event4. 天公八：两张牌且8点(首轮牌)
event5. 同花顺：三张牌组成顺子且同花 8倍
event6. 三条：三张牌点数相同 5倍
event7. 顺子：三张牌组成顺子234~QKA 4倍
event8. 木虱：点数个位数为0，只能吃双鬼
event9. 三张同花 3倍
event10.两张同花2倍
event11.对子 2倍
event12. 9点~1点 1倍
"""


class Score(metaclass=abc.ABCMeta):  # 定义抽象类
    @abc.abstractmethod  # 定义抽象方法
    def score(self, c_lst, n_lst):
        pass


class CountScore(Score):  # 定义子类：用于计算非顺子非五雷的结果，普通计算，天公,木虱
    def score(self, c_lst, n_lst):  # 必须创建同样的方法覆盖父类的方法
        event = 12
        level = 3
        p = dc.takeZero(n_lst)
        multiple = 1
        points = sum(p) % 10
        if "Joker" not in c_lst:
            if len(c_lst) == 2:
                """两只牌是否有天公9、天公8"""
                if sum(p) % 10 == 9:
                    event = 3
                    level = 1
                elif sum(p) % 10 == 8:
                    event = 4
                    level = 1
                elif sum(p) % 10 == 0:
                    event = 8
                    level = 4
                else:
                    pass
            else:
                pass
        else:
            pass
        print("按普通计算的结果，当前属于事件%d，倍数为%d，点数为%d" % (event, multiple, points))
        return level, event, multiple, points


class FlushScore(Score):  # 定义子类，用于计算同花
    def score(self, c_lst, n_lst):
        event = 12
        level = 3
        multiple = 1
        points = None
        if (len(n_lst) == 2) and (len(set(c_lst)) == 1):
            """两只牌是否同花"""
            event = 10
            multiple = 2
            level = 2
        else:
            pass
        if (len(n_lst) == 2) and (set(c_lst) == {"Joker"}):
            event = 2
            level = 1
            multiple = 20
        else:
            pass

        if (len(n_lst) == 3) and (len(set(c_lst)) == 1):
            """三只牌是否同花"""
            event = 9
            level = 2
            multiple = 3
        else:
            pass

        if (len(n_lst) == 3) and (set(c_lst) == {"Joker"}):
            """三只同花牌是否双鬼"""
            event = 1
            level = 1
            multiple = 40
        else:
            pass
        print("按同花计算的结果，当前属于事件%d，倍数为%d，点数为%s" % (event, multiple, points))
        return level, event, multiple, points


class FlowScore(Score):  # 定义子类，用于计算顺子
    def score(self, c_lst, n_lst):
        event = 12
        level = 3
        points = None
        multiple = 1
        p = dc.takeNum(n_lst)
        p.sort()
        if "Joker" not in c_lst:
            if ((p[1] - p[0]) == 1 and (p[2] - p[1]) == 1) or p in ([1, 12, 13], [1, 2, 13]):
                event = 7
                multiple = 4
                if len(set(c_lst)) == 1:
                    event = 5
                    multiple = 8
                else:
                    pass
            else:
                pass
        else:
            pass
        print("按顺子计算的结果，当前属于事件%d，倍数为%d，点数为%s" % (event, multiple, points))
        return level, event, multiple, points


class PlusScore(Score):  # 定义子类，用于计算同点【含木虱】
    def score(self, c_lst, n_lst):
        event = 12
        level = 3
        points = None
        p = dc.takeNum(n_lst)
        multiple = 1
        if len(set(p)) == 1:
            if set(p) in [{10}, {11}, {12}, {13}]:
                event = 8
            else:
                points = sum(p) % 10
                if len(n_lst) == 2:
                    event = 11
                    multiple = 2
                else:
                    event = 6
                    multiple = 5
        else:
            pass

        print("按五雷计算的结果，当前属于事件%d，倍数为%d，点数为%s" % (event, multiple, points))
        return level, event, multiple, points


"""建立方法收集子类"""


def collect():
    strategy = []
    strategy.append(CountScore())
    strategy.append(FlushScore())
    strategy.append(FlowScore())
    strategy.append(PlusScore())
    return strategy


def PlayScore(lst):
    print("你的牌是", lst)
    (c_lst, n_lst) = dc.extract(lst)
    funlst = collect()
    end = []
    for i in funlst:
        (a, b, c, d) = i.score(c_lst, n_lst)
        end.append((a, b, c, d))
    return end


if __name__ == '__main__':
    n = [('红心', 1), ('红心', 3), ('红心', 2)]
    print(PlayScore(n))
