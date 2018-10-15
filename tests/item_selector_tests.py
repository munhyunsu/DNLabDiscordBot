import unittest
import unittest.mock

from modules.item_selector import ItemSelector


class ItemSelectorTestCase(unittest.TestCase):
    def setUp(self):
        self.selector = ItemSelector()

    def tearDown(self):
        del self.selector

    def test___init__(self):
        self.assertEqual(dict(), self.selector.contents)

    def test_get_random_of_0_and_1(self):
        author_mock = unittest.mock.Mock(mention='@everyone')
        ctx_mock = unittest.mock.Mock(author=author_mock)
        vote_list = []
        result = self.selector.get_random(ctx_mock, vote_list)
        self.assertEqual('@everyone 선택지가 2개 이상이여야 합니다.', result)
        vote_list = ['One']
        result = self.selector.get_random(ctx_mock, vote_list)
        self.assertEqual('@everyone 선택지가 2개 이상이여야 합니다.', result)

    def test_get_random_of_3(self):
        ctx_mock = unittest.mock.MagicMock()
        vote_list = ['하나', '둘', '셋']
        result = self.selector.get_random(ctx_mock, vote_list)
        self.assertIn(result.split(' ')[-1], vote_list)
