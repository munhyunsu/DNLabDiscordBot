import os
import random
import csv
import time
import json
import statistics

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
MAX_LEN = 10


class RockPaperScissors(object):
    def __init__(self, log_path, user_path):
        self.log_path = log_path
        if not os.path.exists(self.log_path):
            with open(self.log_path, 'w') as f:
                writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
                writer.writeheader()
        self.stats = dict()
        self.histories = dict()
        self._get_stats()
        self.user_path = user_path
        self.user_db = dict()
        if os.path.exists(self.user_path):
            with open(self.user_path, 'r') as f:
                self.user_db = json.load(f)

    def do_battle(self, ctx, args=()):
        if len(args) > 0:
            if args[0] is '랭크':
                return self._print_rank(ctx, args)
        p1_hand = self._rparse_hand(ctx.message.content)
        p2_hand = self._get_com_hand(ctx)
        score = self._get_score(p1_hand, p2_hand)
        win_rate, rounds = self._update_rounds(ctx, score)
        self._write_log(ctx, p1_hand, score)
        self._update_user_db(ctx)
        text = '{0.author.mention} {1} vs {2} {3}!! 총 {4}판 승률: {5:.2%}'.format(ctx,
                                                                               HAND_MAP[p1_hand],
                                                                               HAND_MAP[p2_hand],
                                                                               SCORE_MAP[score],
                                                                               rounds,
                                                                               win_rate)
        user_id = str(ctx.author.id)
        history = self.histories.get(user_id, deque(maxlen=MAX_LEN))
        if len(history) < MAX_LEN:
            text = ('{0}\n'
                    '아직 배치 중입니다.').format(text)
        else:
            text = ('{0}\n'
                    '{1}명중 {2}등 입니다.').format(text,
                                              len(self.histories.keys()), self._get_rank(ctx))
        return text

    def _get_rank(self, ctx):
        userid = str(ctx.author.id)
        stat = self.stats.get(userid, [0, 0, 0])
        rounds = sum(stat)
        win_rate = stat[0] / rounds
        rank = 1
        for stat in self.stats.values():
            if sum(stat) < 10:
                continue
            other_win_rate = stat[0] / sum(stat)
            if win_rate < other_win_rate:
                rank = rank + 1
        return rank

    def _get_stats(self):
        with open(self.log_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                userid = str(row['userid'])
                score = int(row['score'])
                stat = self.stats.get(userid, [0, 0, 0])
                stat[score - 1] = stat[score - 1] + 1
                self.stats[userid] = stat
                history = self.histories.get(userid, deque(maxlen=MAX_LEN))
                history.appendleft(int(row['hand']))
                self.histories[userid] = history

    def _update_rounds(self, ctx, score):
        userid = str(ctx.author.id)
        stat = self.stats.get(userid, [0, 0, 0])
        stat[score - 1] = stat[score - 1] + 1
        rounds = sum(stat)
        win_rate = stat[0] / rounds
        self.stats[userid] = stat
        return win_rate, rounds

    def _update_user_db(self, ctx):
        user_name = '#'.join(str(ctx.author).split('#')[:-1])
        user_id = str(ctx.author.id)
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
        user_id = str(ctx.author.id)
        history = self.histories.get(user_id, deque(maxlen=MAX_LEN))
        history.appendleft(hand)
        self.histories[user_id] = history

    def _get_com_hand(self, ctx):
        user_id = str(ctx.author.id)
        history = self.histories.get(user_id, deque(maxlen=MAX_LEN))
        if len(history) != MAX_LEN:
            return random.choice([1, 2, 3])
        return random.choices([2, 3, 1],
                              weights=[history.count(1), history.count(2), history.count(3)],
                              k=1)[0]

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
