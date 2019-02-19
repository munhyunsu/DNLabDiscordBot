import re
import random


class TarotReader(object):
    def __init__(self):
        self.deck = dict()

    def get_cards(self):
        pass

    def _shuffle(self):
        for key in self.deck.keys():
            random.shuffle(self.deck[key])

