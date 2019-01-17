from discord.ext import commands

from .modules.greeter import Greeter
from .modules.item_selector import ItemSelector
from .modules.kawibawibo import KawiBawiBo
from .modules.dice import DiceRoll
from .modules.search_engine import SearchEngine
from .modules.deep_rock_paper_scissors import RockPaperScissors


class LuHaCommands(object):
    def __init__(self):
        self.greeter = Greeter()
        self.selector = ItemSelector()
        self.kbb_referee = KawiBawiBo()
        self.dice = DiceRoll()
        self.search_engine = SearchEngine()
        self.dl_rps = RockPaperScissors('dl_rps_log.csv', 'users.json')

    @commands.command(name='hello',
                      aliases=['인사'])
    async def hello(self, ctx, *args):
        """채널에 있는 사람에게 인사를 합니다.
        사용법: 인사"""
        await ctx.send(self.greeter.get_hello(ctx, args))

    @commands.command(name='select',
                      aliases=['선택', '랜덤'])
    async def select(self, ctx, *args):
        """주어진 항목 중에서 무작위로 1개 선택합니다.
        사용법: 선택 하나 둘 셋"""
        await ctx.send(self.selector.get_random(ctx, args))

    @commands.command(name='kbb',
                      aliases=['가위바위보'])
    async def kbb(self, ctx, *args):
        """가위 바위 보를 합니다.
        사용법: 가위바위보 가위 -> 가위바위보 결과"""
        await ctx.send(self.kbb_referee.kbb_game(ctx, args))

    @commands.command(name='dice',
                      aliases=['주사위'])
    async def roll_dice(self, ctx, *args):
        """주사위를 굴립니다.
        사용법: 주사위 횟수D면체"""
        await ctx.send(self.dice.roll_dice(ctx, args))

    @commands.command(name='search',
                      aliases=['검색'])
    async def search(self, ctx, *args):
        """검색어가 포함된 URL을 표시합니다.
        사용법: 검색 [구글|네이버|다음] [검색어]"""
        await ctx.send(self.search_engine.search(ctx, args))

    @commands.command(name='rps',
                      aliases=['가위', '바위', '보'])
    async def rps(self, ctx, *args):
        """딥러닝 가위바위보 봇과 대결합니다.
        사용법: [가위|바위|보]"""
        await ctx.send(self.dl_rps.do_battle(ctx, args))


def setup(bot):
    bot.add_cog(LuHaCommands())
