from base.card import Card
class CardPriest0015(Card):
    def __init__(self):
        self.hp_total = 0
        self.hp_current = 0
        self.atk_total = 0
        self.atk_current = 0
        self.is_selectable = True
        self.type = '法术'
        self.tags = []

    def on_start_phase(self):
        pass

    def on_draw_phase(self):
        pass

    def on_main_phase(self):
        pass

    def on_end_phase(self):
        pass

    def on_summon(self):
        pass

    def on_die(self):
        pass

    def on_draw(self):
        pass

    def on_discard(self):
        pass

    def on_attack(self):
        pass

    def on_injured(self):
        pass