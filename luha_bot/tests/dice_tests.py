import unittest
import unittest.mock

from luha_bot.dice import DiceRoll


class GreeterTestCase(unittest.TestCase):
    def setUp(self):
        self.dice = DiceRoll()

    def tearDown(self):
        del self.dice

    def test_no_args(self):
        author_mock = unittest.mock.Mock(mention='@everyone')
        ctx_mock = unittest.mock.Mock(author=author_mock)
        args = ()
        self.assertEqual('@everyone 숫자D숫자 형태의 입력이 필요합니다.',
                         self.dice.roll_dice(ctx_mock, args))

    def test_invalid_args(self):
        author_mock = unittest.mock.Mock(mention='@everyone')
        ctx_mock = unittest.mock.Mock(author=author_mock)
        args = ('4 d 99', 'aa bb c')
        self.assertEqual('@everyone 숫자D숫자 형태의 입력이 필요합니다.',
                         self.dice.roll_dice(ctx_mock, args))
        args = ('이것은 틀림', )
        self.assertEqual('@everyone 숫자D숫자 형태의 입력이 필요합니다.',
                         self.dice.roll_dice(ctx_mock, args))

    def test_roll_dice(self):
        author_mock = unittest.mock.Mock(mention='@everyone')
        ctx_mock = unittest.mock.Mock(author=author_mock)
        args = ('4d6', )
        self.assertIn('@everyone 6면체 주사위 4번 굴린 결과',
                      self.dice.roll_dice(ctx_mock, args))
        args = ('4번6', )
        self.assertIn('@everyone 6면체 주사위 4번 굴린 결과',
                      self.dice.roll_dice(ctx_mock, args))
