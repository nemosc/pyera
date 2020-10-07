from base.skill import Skill


class Skill0006(Skill):
    def __init__(self):
        super().__init__()
        self.name = '致命射击'
        self.mp_cost = 2
    def on_use(self):
        pass
