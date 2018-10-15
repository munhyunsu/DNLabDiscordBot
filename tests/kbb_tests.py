import unittest
import unittest.mock

from modules.kawibawibo import KawiBawiBo


class ItemSelectorTestCase(unittest.TestCase):
    def setUp(self):
        self.kbb_referee = KawiBawiBo()

    def tearDown(self):
        del self.kbb_referee

    def test___init__(self):
        self.assertEqual(dict(), self.kbb_referee.entry)

    def test_get_random_of_0_and_1(self):
        ctx_mock = unittest.mock.MagicMock()
        args = []
        result = self.kbb_referee.kbb_game(ctx_mock, args)
        self.assertEqual('가위/바위/보 또는 결과를 선택해야합니다.', result)

    def test_get_game_result(self):
        author_mock = unittest.mock.Mock(name='player', mention='@player')
        ctx_mock = unittest.mock.Mock(author=author_mock)
        args = ['가위']
        result = self.kbb_referee.kbb_game(ctx_mock, args)
        self.assertEqual('@player 가위 엔트리!', result)
        author_mock = unittest.mock.Mock(name='player2', mention='@player2')
        ctx_mock = unittest.mock.Mock(author=author_mock)
        args = ['바위']
        result = self.kbb_referee.kbb_game(ctx_mock, args)
        self.assertEqual('@player2 바위 엔트리!', result)
        ctx_mock = unittest.mock.MagicMock()
        args = ['결과']
        result = self.kbb_referee.kbb_game(ctx_mock, args)
        self.assertIn('[총 2명의 선수]\n', result)
