from base.skill import Skill


class Skill0003(Skill):
    def __init__(self):
        super().__init__()
        self.name = '援军'
        self.description = '召唤一个1/1的白银之手新兵'
        self.mp_cost = 2
    def on_use(self):
        pass
