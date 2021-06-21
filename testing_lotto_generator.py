import random
import unittest
from main import LogIn
from window_2 import UserID
from window_2 import Lotto
from claim_prize import Prize


class TestLogIn(unittest.TestCase):
    def test_verify(self):
        self.assertEqual(True, False)


class TestUserID(unittest.TestCase):
    def test_generate_lott(self):
        x = random.randint(range(1, 49), 6)
        print(x)
        return x




if __name__ == '__main__':
    unittest.main()
