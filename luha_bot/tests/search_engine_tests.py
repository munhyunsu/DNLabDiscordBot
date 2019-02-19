import unittest
import unittest.mock

from luha_bot.search_engine import SearchEngine


class SearchEngineTestCase(unittest.TestCase):
    def setUp(self):
        self.search = SearchEngine()

    def tearDown(self):
        del self.search

    def test_no_args(self):
        author_mock = unittest.mock.Mock(mention='@everyone')
        ctx_mock = unittest.mock.Mock(author=author_mock)
        args = ()
        self.assertEqual('@everyone 검색엔진 검색어 형태로 입력해주세요.',
                         self.search.search(ctx_mock, args))

    def test_one_args(self):
        author_mock = unittest.mock.Mock(mention='@everyone')
        ctx_mock = unittest.mock.Mock(author=author_mock)
        args = ('구글', '스플래툰2')
        self.assertEqual('@everyone https://www.google.co.kr/search?q=스플래툰2',
                         self.search.search(ctx_mock, args))

    def test_two_args(self):
        author_mock = unittest.mock.Mock(mention='@everyone')
        ctx_mock = unittest.mock.Mock(author=author_mock)
        args = ('구글', '스플래툰2', '아미보')
        self.assertEqual('@everyone https://www.google.co.kr/search?q=스플래툰2+아미보',
                         self.search.search(ctx_mock, args))
