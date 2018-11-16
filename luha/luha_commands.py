from discord.ext import commands

from .modules.greeter import Greeter
from .modules.item_selector import ItemSelector
from .modules.kawibawibo import KawiBawiBo
from .modules.dice import DiceRoll


class LuHaCommands(object):
    def __init__(self):
        self.greeter = Greeter()
        self.selector = ItemSelector()
        self.kbb_referee = KawiBawiBo()
        self.dice = DiceRoll()

    @commands.command(name='hello',
                      aliases=['인사'])
    async def hello(self, ctx, *args):
        """채널에 있는 사람에게 인사를 합니다."""
        await ctx.send(self.greeter.get_hello(ctx, args))

    @commands.command(name='select',
                      aliases=['선택', '랜덤'])
    async def select(self, ctx, *args):
        """주어진 항목 중에서 무작위로 1개 선택합니다."""
        await ctx.send(self.selector.get_random(ctx, args))

    @commands.command(name='kbb',
                      aliases=['가위바위보'])
    async def kbb(self, ctx, *args):
        """가위 바위 보를 합니다."""
        await ctx.send(self.kbb_referee.kbb_game(ctx, args))

    @commands.command(name='dice',
                      aliases=['주사위'])
    async def roll_dice(self, ctx, *args):
        """주사위를 굴립니다. 사용법: 횟수D면체"""
        await ctx.send(self.dice.roll_dice(ctx, args))


def setup(bot):
    bot.add_cog(LuHaCommands())