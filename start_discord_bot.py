from discord.ext import commands

from private.private_key import CLIENT_TOKEN

BOT_DESC = '''충남대학교 데이터네트워크연구실 디스코드 봇
무슨 일을 하려고 만드는지는 아직 모른다.
하지만 재미있는 응용이므로 일단 만들어 둔다.'''


def main():
    bot = commands.Bot(command_prefix='!',
                       case_insensitive=True,
                       description=BOT_DESC)

    extensions = ['luha_bot.luha_commands']

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('----------')

    for extension in extensions:
        print('Load extension {0}'.format(extension))
        bot.load_extension(extension)
        print('Complete {0} loading'.format(extension))

    bot.run(CLIENT_TOKEN)


if __name__ == '__main__':
    main()
