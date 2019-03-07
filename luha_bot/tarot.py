import os
import random

import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
from discord import File

from private.private_key import GSPREAD_FILE, TAROT_GSPREAD_KEY


class TarotReader(object):
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        credentials = SAC.from_json_keyfile_name(GSPREAD_FILE, scope)
        self.gc = gspread.authorize(credentials)
        self.decks = self._meditation()

    def _meditation(self):
        gc = self.gc

        # Deck options
        deck_names = ['RaiderWaiteTarot']

        # get decks
        decks = dict()
        for deck_name in deck_names:
            deck = dict()
            wks = gc.open_by_key(TAROT_GSPREAD_KEY).worksheet(deck_name)
            for row in wks.get_all_values()[1:]:
                name = row[2]
                deck[name] = {'url': row[4],
                              'urlr': row[5],
                              'meaning': row[6],
                              'meaningr': row[7]}
            decks[deck_name] = deck

        return decks

    def _deck_shuffle(self, deck_name, seed=None):
        deck = list()
        for card in self.decks[deck_name].keys():
            if random.randint(0, 1) == 1:
                card_name = '{0} (R)'.format(card)
            else:
                card_name = card
            deck.append(card_name)
        random.shuffle(deck)
        if seed is not None:
            random.seed(seed)
        random.shuffle(deck)
        random.seed(None)
        return deck

    def one_card(self, deck_name, seed=None):
        talk = '{0}\n{1}: {2}'
        deck = self.decks[deck_name]
        hands = self._deck_shuffle(deck_name, seed=seed)

        card_name = hands[0]
        if card_name.endswith('(R)'):
            meaning = deck[card_name[:-4]]
            talk = talk.format(meaning['urlr'], card_name, meaning['meaningr'])
        else:
            meaning = deck[card_name]
            talk = talk.format(meaning['url'], card_name, meaning['meaning'])

        return talk

    def get_cards(self, deck_name, num, seed=None):
        deck = self.decks[deck_name]
        hands = self._deck_shuffle(deck_name, seed=seed)
        talk = ''
        for index in range(0, num):
            card_name = hands[index]
            if card_name.endswith('(R)'):
                meaning = deck[card_name[:-4]]
                append_talk = '[{0}] {1}: {2}'.format(index+1, card_name, meaning['meaningr'])
                talk = '{0}\n{1}'.format(talk, append_talk)
            else:
                meaning = deck[card_name]
                append_talk = '[{0}] {1}: {2}'.format(index+1, card_name, meaning['meaning'])
                talk = '{0}\n{1}'.format(talk, append_talk)
        return talk

    def fortune(self, ctx, args=()):
        if len(args) > 0 and args[0] == '켈틱크로스':
            seed = ' '.join(args[1:])
            if seed == '':
                seed = None
            talk = self.get_cards('RaiderWaiteTarot', num=10, seed=seed)
        elif len(args) > 0 and args[0] == '쓰리카드':
            seed = ' '.join(args[1:])
            if seed == '':
                seed = None
            talk = self.get_cards('RaiderWaiteTarot', num=3, seed=seed)
        else:
            seed = ' '.join(args)
            if seed == '':
                seed = None
            talk = self.one_card('RaiderWaiteTarot', seed=seed)
        return '{0.author.mention} {1}'.format(ctx, talk)


if __name__ == '__main__':
    tr = TarotReader()
    print(tr.get_cards('RaiderWaiteTarot'))
