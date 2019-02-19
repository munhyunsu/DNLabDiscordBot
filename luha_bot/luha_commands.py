from discord.ext import commands

from luha_bot.greeter import Greeter
from luha_bot.item_selector import ItemSelector
from luha_bot.kawibawibo import KawiBawiBo
from luha_bot.dice import DiceRoll
from luha_bot.search_engine import SearchEngine
from luha_bot.deep_rock_paper_scissors import RockPaperScissors
from luha_bot.tarot import TarotReader

class LuHaCommands(object):
    def __init__(self):
        self.greeter = Greeter()
        self.selector = ItemSelector()
        self.kbb_referee = KawiBawiBo()
        self.dice = DiceRoll()
        self.search_engine = SearchEngine()
        self.dl_rps = RockPaperScissors('dl_rps_log.csv', 'users.json')
        self.tarot_reader = TarotReader('img')

    @commands.command(name='hello',
                      aliases=['인사'])
    async def hello(self, ctx, *args):
        """사용법: 인사"""
        await ctx.send(self.greeter.get_hello(ctx, args))

    @commands.command(name='select',
                      aliases=['선택', '랜덤'])
    async def select(self, ctx, *args):
        """사용법: 선택 하나 둘 셋"""
        await ctx.send(self.selector.get_random(ctx, args))

    @commands.command(name='kbb',
                      aliases=['가위바위보'])
    async def kbb(self, ctx, *args):
        """사용법: 가위바위보 가위 -> 가위바위보 결과"""
        await ctx.send(self.kbb_referee.kbb_game(ctx, args))

    @commands.command(name='dice',
                      aliases=['주사위'])
    async def roll_dice(self, ctx, *args):
        """사용법: 주사위 횟수D면체"""
        await ctx.send(self.dice.roll_dice(ctx, args))

    @commands.command(name='search',
                      aliases=['검색'])
    async def search(self, ctx, *args):
        """사용법: 검색 [구글|네이버|다음] [검색어]"""
        await ctx.send(self.search_engine.search(ctx, args))

    @commands.command(name='rps',
                      aliases=['가위', '바위', '보'])
    async def rps(self, ctx, *args):
        """사용법: [가위|바위|보]"""
        await ctx.send(self.dl_rps.do_battle(ctx, args))

    @commands.command(name='fortune',
                      aliases=['타로'])
    async def fortune_tarot(self, ctx, *args):
        """사용법: 타로"""
        await self.tarot_reader.fortune(ctx, args)


def setup(bot):
    bot.add_cog(LuHaCommands())
