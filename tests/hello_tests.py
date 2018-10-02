import unittest
import unittest.mock

from modules.hello import Hello


class HelloTestCase(unittest.TestCase):
    def setUp(self):
        self.greeter = Hello()

    def tearDown(self):
        del self.greeter

    def test_hello(self):
        author_mock = unittest.mock.Mock(mention='@everyone')
        ctx_mock = unittest.mock.Mock(author=author_mock)
        self.assertEqual('@everyone Hello, World!',
                         self.greeter.get_hello(ctx_mock))
