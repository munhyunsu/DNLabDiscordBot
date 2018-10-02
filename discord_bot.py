import discord
from discord.ext import commands

from modules.hello import Hello

from bot_description import BOT_DESC
from private_key import CLIENT_TOKEN


def main():
    bot = commands.Bot(command_prefix='!',
                       case_insensitive=True,
                       description=BOT_DESC)

    greeter = Hello()

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('----------')

    @bot.command(name='bot',
                 aliases=['인사'])
    async def hello(ctx, *args):
        """채널에 있는 사람에게 인사를 합니다."""
        await ctx.send(greeter.get_hello(ctx))
