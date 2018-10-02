class Greeter(object):
    @staticmethod
    def get_hello(ctx):
        return '{0.author.mention} Hello, World!'.format(ctx)

