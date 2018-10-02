from discord.ext import commands

from modules.greeter import Greeter


class DNLabCommands(object):
    def __init__(self):
        self.greeter = Greeter()

    @commands.command(name='bot',
                 aliases=['인사'])
    async def hello(self, ctx, *args):
        """채널에 있는 사람에게 인사를 합니다."""
        await ctx.send(self.greeter.get_hello(ctx))
