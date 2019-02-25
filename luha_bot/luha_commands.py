from discord.ext import commands

from luha_bot.greeter import Greeter
from luha_bot.item_selector import ItemSelector
# from luha_bot.kawibawibo import KawiBawiBo
from luha_bot.dice import DiceRoll
from luha_bot.search_engine import SearchEngine
from luha_bot.deep_rock_paper_scissors import RockPaperScissors
from luha_bot.tarot import TarotReader


class LuHaCommands(object):
    def __init__(self):
        self.greeter = Greeter()
        self.selector = ItemSelector()
        # self.kbb_referee = KawiBawiBo()
        self.dice = DiceRoll()
        self.search_engine = SearchEngine()
        self.dl_rps = RockPaperScissors('dl_rps_log.csv', 'users.json')
        self.tarot_reader = TarotReader('img')

    @commands.command(name='hello',
                      aliases=['인사'])
    async def hello(self, ctx, *args):
        """인사를 합니다. '!hello'"""
        await ctx.send(self.greeter.get_hello(ctx, args))

    @commands.command(name='select',
                      aliases=['선택', '랜덤'])
    async def select(self, ctx, *args):
        """띄어쓰기로 구분된 단어들 중에서 하나를 선택합니다. 단어는 2개 이상이어야 합니다. '!선택 [선택지1] [선택지2] [선택지3]'"""
        await ctx.send(self.selector.get_random(ctx, args))

    # Delete it: it's difficult to both use and explain
    # @commands.command(name='kbb',
    #                   aliases=['가위바위보'])
    # async def kbb(self, ctx, *args):
    #     """사용법: 가위바위보 가위 -> 가위바위보 결과"""
    #     await ctx.send(self.kbb_referee.kbb_game(ctx, args))

    @commands.command(name='dice',
                      aliases=['주사위'])
    async def roll_dice(self, ctx, *args):
        """주사위를 굴립니다. '!주사위 [횟수(숫자)]D[면체(숫자)]'"""
        await ctx.send(self.dice.roll_dice(ctx, args))

    @commands.command(name='search',
                      aliases=['검색'])
    async def search(self, ctx, *args):
        """해당 검색엔진에서 검색어로 검색한 링크를 줍니다. '!검색 [구글or네이버or다음] [검색어]'"""
        await ctx.send(self.search_engine.search(ctx, args))

    @commands.command(name='rps',
                      aliases=['가위', '바위', '보'])
    async def rps(self, ctx, *args):
        """봇과 가위바위보를 합니다. '![가위or바위or보]'"""
        await ctx.send(self.dl_rps.do_battle(ctx, args))

    @commands.command(name='fortune',
                      aliases=['타로'])
    async def fortune_tarot(self, ctx, *args):
        """타로카드를 하나 뽑습니다. 타로 뒤에 문자열을 적을 수 있습니다. '!타로 (문자열)'"""
        await self.tarot_reader.fortune(ctx, args)


def setup(bot):
    bot.add_cog(LuHaCommands())
