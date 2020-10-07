from base.skill import Skill


class Skill0005(Skill):
    def __init__(self):
        super().__init__()
        self.name = '火焰冲击'
        self.mp_cost = 2
    def on_use(self):
        pass
