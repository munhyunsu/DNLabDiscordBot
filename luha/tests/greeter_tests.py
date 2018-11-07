import unittest
import unittest.mock

from luha.modules.greeter import Greeter


class GreeterTestCase(unittest.TestCase):
    def setUp(self):
        self.greeter = Greeter()

    def tearDown(self):
        del self.greeter

    def test_hello(self):
        author_mock = unittest.mock.Mock(mention='@everyone')
        ctx_mock = unittest.mock.Mock(author=author_mock)
        self.assertEqual('@everyone Hello, World!',
                         self.greeter.get_hello(ctx_mock))
