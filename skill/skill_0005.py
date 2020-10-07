from base.skill import Skill


class Skill0005(Skill):
    def __init__(self):
        super().__init__()
        self.name = '变形'
        self.description = '本回合+1攻击力。+1护甲值。'
        self.mp_cost = 2
    def on_use(self):
        pass
