from discord.ext import commands

from dnlab_commands import DNLabCommands

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

    bot.add_cog(DNLabCommands())

    bot.run(CLIENT_TOKEN)


if __name__ == '__main__':
    main()