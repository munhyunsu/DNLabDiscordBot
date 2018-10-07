from discord.ext import commands

from luha_commands import LuHaCommands

from bot_description import BOT_DESC
from private_key import CLIENT_TOKEN


def main():
    bot = commands.Bot(command_prefix='!',
                       case_insensitive=True,
                       description=BOT_DESC)

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('----------')

    bot.add_cog(LuHaCommands())

    bot.run(CLIENT_TOKEN)


if __name__ == '__main__':
    main()