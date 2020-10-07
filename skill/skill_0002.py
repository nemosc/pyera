from base.skill import Skill


class Skill0002(Skill):
    def __init__(self):
        super().__init__()
        self.name = '稳固射击'
        self.description = '装备一把1/2的匕首'
        self.mp_cost = 2
    def on_use(self):
        pass
