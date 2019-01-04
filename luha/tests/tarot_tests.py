import unittest
import unittest.mock

from modules.tarot import TarotReader


class TarotTestCase(unittest.TestCase):
    def setUp(self):
        self.tarot_reader = TarotReader

    def tearDown(self):
        del self.tarot_reader

