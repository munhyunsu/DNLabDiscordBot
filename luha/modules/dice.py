import re
import random


class DiceRoll(object):
    @staticmethod
    def roll_dice(ctx, args=()):
        if len(args) <= 0:
            return '{0.author.mention} 숫자D숫자 형태의 입력이 필요합니다.'.format(ctx)
        elif len(args) >= 1:
            try:
                if '번' in args[0]:
                    roll, dice = map(int, re.findall(r'(\d+)(?:번)(\d+)', args[0])[0])
                else:
                    roll, dice = map(int, re.findall(r'(\d+)(?:d|D)(\d+)', args[0])[0])
            except IndexError:
                roll, dice = (None, None)

            if roll is None or dice is None:
                return '{0.author.mention} 숫자D숫자 형태의 입력이 필요합니다.'.format(ctx)

            re_str = '{0.author.mention} {1:d}면체 주사위 {2:d}번 굴린 결과:'.format(ctx,
                                                                           dice,
                                                                           roll)
            for rand_int in random.choices(range(1, dice + 1), k=roll):
                re_str = '{0} {1}'.format(re_str,
                                          rand_int)

            return re_str
