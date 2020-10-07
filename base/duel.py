from base import player
from util import util
import random


class Duel:
    def __init__(self, decks):
        self.players = [player.Player(deck) for deck in decks]
        self.turn = 1
        self.current = 0

    def start(self):
        """
        before started,
        we need to decide which player will play first,
        and switch hand cards.
        """
        self.current = self.toss()
        for i in range(len(self.players)):
            if i == self.current:
                self.players[i].draw(3)
                self.switch(self.players[i])
            else:
                self.players[i].draw(4)
                self.switch(self.players[i])
                self.players[i].create('硬币') # add a coin
        while True:
            self.turn()
            self.current = (self.current+1) % len(self.players)
            self.turn += 1

    def switch(self, p):
        choices = util.get_list()
        samples = random.sample(range(len(p.deck)), len(choices))
        for i in range(len(choices)):
            p.hand[choices[i]], p.deck[samples[i]] = p.deck[samples[i]], p.hand[choices[i]]

    def turn(self):
        """
        four phases in total:
        start phase
        draw phase
        main phase
        end phase
        """
        p = self.players[self.current]
        for i in range(len(self.players)):
            for j in range(len(self.players[i].field)):
                self.players[i].field[j].on_start_phase()
        for i in range(len(self.players)):
            for j in range(len(self.players[i].field)):
                self.players[i].field[j].on_draw_phase()
        for i in range(len(self.players)):
            for j in range(len(self.players[i].field)):
                self.players[i].field[j].on_main_phase()
        user_input = util.get_string()
        while user_input!='回合结束':
            # do something
            user_input = util.get_string()
        for i in range(len(self.players)):
            for j in range(len(self.players[i].field)):
                self.players[i].field[j].on_end_phase()





    def toss(self):
        return random.randint(0, len(self.players)-1)
