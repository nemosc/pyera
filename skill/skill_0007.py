from base.skill import Skill


class Skill0007(Skill):
    def __init__(self):
        super().__init__()
        self.name = '火焰冲击'
        self.description = '造成1点伤害'
        self.mp_cost = 2
    def on_use(self):
        pass
