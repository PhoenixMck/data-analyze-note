"""判断玩家得分，需要处理玩家的牌的列表"""

def extract(list):
    """把牌属性的元组提取成花色列表和大小列表"""
    c_lst = []
    n_lst = []
    """还是把牌搞成列表方便"""
    for i in range(len(list)):
        c_lst.append(list[i][0])
        n_lst.append(list[i][1])
    return c_lst, n_lst


def takeNum(n_lst):
    """处理JQK，处理成11、12、13，可用于判断顺子"""
    while "J" in n_lst:
        n_lst[n_lst.index("J")] = 11
    else:
        while "Q" in n_lst:
            n_lst[n_lst.index("Q")] = 12
        else:
            while "K" in n_lst:
                n_lst[n_lst.index("K")] = 13
    return n_lst


def takeZero(list):
    """被JQK处理成10，用于计算点数"""
    n_lst1 = list.copy()
    for i in n_lst1:
        if i in ["J", "Q", "K"]:
            i = 10
    return n_lst1
