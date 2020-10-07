from base.skill import Skill


class Skill0006(Skill):
    def __init__(self):
        super().__init__()
        self.name = '生命分流'
        self.description = '抽一张牌并受到2点伤害'
        self.mp_cost = 2
    def on_use(self):
        pass
