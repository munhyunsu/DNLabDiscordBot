import datetime


class Toys(object):
    def __init__(self):
        self.attendance = set()
        self.latest = datetime.datetime.now()

    def three_out(self, ctx, args=()):
        current = datetime.datetime.now()
        if (current - self.latest).total_seconds() > 60:
            self.attendance.clear()
        self.attendance.add(ctx.author.id)
        if len(self.attendance) > 2:
            self.attendance.clear()
            return 'https://imgur.com/a/22Sk1HS'
