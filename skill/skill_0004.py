from base.skill import Skill


class Skill0004(Skill):
    def __init__(self):
        super().__init__()
        self.name = '稳固射击'
        self.description = '对敌方英雄造成2点伤害'
        self.mp_cost = 2
    def on_use(self):
        pass
