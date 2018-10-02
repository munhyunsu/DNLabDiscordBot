import unittest

from modules.item_selector import ItemSelector


class ItemSelectorTestCase(unittest.TestCase):
    def test___init__(self):
        item_selector = ItemSelector()
        self.assertEqual(dict(), item_selector.contents)

    def test_add_new_list(self):
        pass
