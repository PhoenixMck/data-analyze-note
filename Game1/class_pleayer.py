"""创建玩家类，玩家有两种属性：性质【电脑或人类】和姓名"""


class player:

    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.card = []
        self.command = "N"  # 发牌命令

    """方法：获取人类玩家名称"""

    def get_name(self):
        if self.type == "P":
            self.name = input("输入你的名字")
        else:
            self.name = "Eve"
