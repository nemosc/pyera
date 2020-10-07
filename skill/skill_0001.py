from base.skill import Skill


class Skill0001(Skill):
    def __init__(self):
        super().__init__()
        self.name = '图腾召唤'
        self.mp_cost = 2
    def on_use(self):
        pass
