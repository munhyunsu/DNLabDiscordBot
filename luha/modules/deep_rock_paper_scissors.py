import os
import random
import csv
import time
import json

from collections import deque

HAND_MAP = {0: 'Error',
            1: '바위',
            2: '보',
            3: '가위'}
RHAND_MAP = {'바위': 1,
             '보': 2,
             '가위': 3}
SCORE_MAP = {0: 'Error',
             1: '승리',
             2: '무승부',
             3: '패배'}
FIELDNAMES = ['unixtime', 'userid', 'hand', 'score']


class RockPaperScissors(object):
    def __init__(self, log_path, user_path):
        self.log_path = log_path
        if not os.path.exists(self.log_path):
            with open(self.log_path, 'w') as f:
                writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
                writer.writeheader()
        self.user_path = user_path
        self.user_db = dict()
        if os.path.exists(self.user_path):
            with open(self.user_path, 'r') as f:
                self.user_db = json.load(f)

    def do_battle(self, ctx, args=()):
        p1_hand = self._rparse_hand(ctx.message.content)
        p2_hand = self._get_com_hand()
        score = self._get_score(p1_hand, p2_hand)
        self._write_log(ctx, p1_hand, score)
        self._update_user_db(ctx)
        return '{0.author.mention} {1:2s}(H) vs {2:2s}(C) {3}!!'.format(ctx,
                                                                        HAND_MAP[p1_hand],
                                                                        HAND_MAP[p2_hand],
                                                                        SCORE_MAP[score])

    def _update_user_db(self, ctx):
        user_name = '#'.join(str(ctx.author).split('#')[:-1])
        user_id = ctx.author.id
        print(user_id, user_name)
        if user_id in self.user_db:
            if self.user_db[user_id] is user_name:
                return None
        self.user_db[user_id] = user_name
        with open(self.user_path, 'w') as f:
            json.dump(self.user_db, f, ensure_ascii=False, sort_keys=True, indent=4)

    @staticmethod
    def _rparse_hand(message):
        return RHAND_MAP[message[1:]]

    def _write_log(self, ctx, hand, score):
        data = {'unixtime': time.time(),
                'userid': ctx.author.id,
                'hand': hand,
                'score': score}
        with open(self.log_path, 'a') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writerow(data)

    @staticmethod
    def _get_com_hand():
        return random.choice([1, 2, 3])

    @staticmethod
    def _get_score(p1, p2):
        if p1 == p2:  # R-R, P-P, S-S
            return 2
        elif p1 == 1:
            if p2 == 2:  # R-P
                return 3
            elif p2 == 3:  # R-S
                return 1
        elif p1 == 2:
            if p2 == 1:  # P-R
                return 1
            elif p2 == 3:  # P-S
                return 3
        elif p1 == 3:
            if p2 == 1:  # S-R
                return 3
            elif p2 == 2:  # S-P
                return 1
