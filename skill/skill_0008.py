from base.skill import Skill


class Skill0008(Skill):
    def __init__(self):
        super().__init__()
        self.name = '次级治疗术'
        self.description = '恢复2点生命值'
        self.mp_cost = 2
    def on_use(self):
        pass
