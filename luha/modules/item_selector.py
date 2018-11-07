import random


class ItemSelector(object):
    def __init__(self):
        self.contents = dict()

    @staticmethod
    def get_random(ctx, args=()):
        if len(args) <= 1:
            return '{0.author.mention} 선택지가 2개 이상이여야 합니다.'.format(ctx)
        elif len(args) >= 2:
            return '{0.author.mention} 총 {1:2d}개 중에서 선택: {2}'.format(ctx,
                                                                     len(args),
                                                                     random.choice(args))
