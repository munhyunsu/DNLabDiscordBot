import os
import unittest
import unittest.mock

from luha.modules.deep_rock_paper_scissors import RockPaperScissors

FILEPATH = 'rps_history.csv'
USERPATH = 'rps_user.json'


class DeepRockPaperScissorsTestCase(unittest.TestCase):
    def setUp(self):
        self.rps_referee = RockPaperScissors(FILEPATH, USERPATH)

    def tearDown(self):
        del self.rps_referee
        if os.path.exists(FILEPATH):
            os.remove(FILEPATH)
        if os.path.exists(USERPATH):
            os.remove(USERPATH)

    # def test_do_battle(self):
    #     author_mock = unittest.mock.Mock(name='player', mention='@player')
    #     ctx_mock = unittest.mock.Mock(author=author_mock)
    #     args = ['가위']
    #     result = self.rps_referee.do_battle(ctx_mock, args)
    #     self.assertTrue(result.startswith('@player'))

