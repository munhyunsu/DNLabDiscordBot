import os
import random

import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
from discord import File

from private.private_key import GSPREAD_FILE, TAROT_GSPREAD_KEY


class TarotReader(object):
    def __init__(self, img_dir):
        self.img_dir = img_dir
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        credentials = SAC.from_json_keyfile_name(GSPREAD_FILE, scope)
        self.gc = gspread.authorize(credentials)
        self.decks, self.decks_mean = self._meditation()

    def _meditation(self):
        gc = self.gc

        # Deck options
        deck_names = ['RaiderWaiteTarot']

        # get decks
        decks = dict()
        decks_mean = dict()
        for deck_name in deck_names:
            deck = list()
            deck_record = dict()
            wks = gc.open_by_key(TAROT_GSPREAD_KEY).worksheet(deck_name)
            for row in wks.get_all_values()[1:]:
                name = row[2]
                deck.append(name)
                deck_record[name] = {'filename': row[3],
                                     'meaning': row[4],
                                     'meaning_r': row[5]}
            decks[deck_name] = deck
            decks_mean[deck_name] = deck_record

        return decks, decks_mean

    def _deck_shuffle(self, deck_name, seed=None):
        deck = list()
        for card in self.decks[deck_name]:
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

    def get_cards(self, deck_name, seed=None, num=1):
        deck = self._deck_shuffle(deck_name, seed=seed)
        deck_mean = self.decks_mean[deck_name]

        result = list()
        for index in range(0, num):
            card_name = deck[index]
            if card_name.endswith('(R)'):
                card_name_original = ' '.join(card_name.split(' ')[:-1])
                file_name = deck_mean[card_name_original]['filename']
                file_name = '-R.'.join(file_name.split('.'))
            else:
                file_name = deck_mean[card_name]['filename']
            file_path = os.path.expanduser(os.path.join(self.img_dir, deck_name))
            file_path = os.path.abspath(os.path.join(file_path, file_name))
            image_file = File(open(file_path, 'rb'))
            result.append((card_name, image_file))

        return result

    async def fortune(self, ctx, args=()):
        seed = ' '.join(args)
        card_name, image_file = self.get_cards('RaiderWaiteTarot', seed=seed)[0]
        await ctx.send('{0.author.mention} {1}'.format(ctx, card_name), file=image_file)


if __name__ == '__main__':
    tr = TarotReader('~/Github/DNLabDiscordBot/img')
    print(tr.get_cards('RaiderWaiteTarot'))
