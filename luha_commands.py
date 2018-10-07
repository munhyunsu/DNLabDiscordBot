from discord.ext import commands

from modules.greeter import Greeter
from modules.item_selector import ItemSelector


class LuHaCommands(object):
    def __init__(self):
        self.greeter = Greeter()
        self.selector = ItemSelector()

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
