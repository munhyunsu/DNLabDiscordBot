import random


class ItemSelector(object):
    def __init__(self):
        self.contents = dict()

    @staticmethod
    def get_random(ctx, args=()):
        if len(args) <= 1:
            return '선택지가 2개 이상이여야 합니다.'
        elif len(args) >= 2:
            return '총 {0:2d}개 중에서 선택: {1}'.format(len(args), random.choice(args))
