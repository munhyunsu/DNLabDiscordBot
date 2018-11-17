class KawiBawiBo(object):
    def __init__(self):
        self.entry = dict()

    def kbb_game(self, ctx, args=()):
        if len(args) <= 0:
            return '{0.author.mention} 가위/바위/보 또는 결과를 선택해야합니다.'.format(ctx)
        if args[0] == '결과':
            result_str = '[총 {0:d}명의 선수]\n'.format(len(self.entry))
            for key in self.entry.keys():
                result_str = result_str + '{0}: {1}\n'.format(key, self.entry[key])
            return result_str
        elif args[0] in ['가위', '바위', '보']:
            self.entry[ctx.author.name] = args[0]
            return '{0.author.mention} {1} 엔트리!'.format(ctx, args[0])
        else:
            return '{0.author.mention} 가위/바위/보 또는 결과를 선택해야합니다.'.format(ctx)
