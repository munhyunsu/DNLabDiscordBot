import sys

QUERY_GOOGLE = '{0.author.mention} https://www.google.co.kr/search?q={1}'
QUERY_NAVER = '{0.author.mention} https://search.naver.com/search.naver?query={1}'
QUERY_DAUM = '{0.author.mention} https://search.daum.net/search?q={1}'


class SearchEngine(object):
    def __init__(self):
        self.queries = {'구글': QUERY_GOOGLE,
                        '네이버': QUERY_NAVER,
                        '다음': QUERY_DAUM}

    def search(self, ctx, args=()):
        if len(args) <= 1:
            return '{0.author.mention} 검색엔진 검색어 형태로 입력해주세요.'.format(ctx)
        if args[0] not in self.queries.keys():
            return '{0.author.mention} 지원하지 않는 검색엔진입니다.'.format(ctx)
        query_form = self.queries[args[0]]
        query = '+'.join(args[1:])
        return query_form.format(ctx, query)
