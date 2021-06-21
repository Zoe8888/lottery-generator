import rsaidnumber

import unittest
import random
from main import LogIn
from window_2 import UserID
from window_2 import Lotto
from claim_prize import Prize


class TestLogIn(unittest.TestCase):
    def test_id(self):
        id_number = rsaidnumber.parse('9903200072086')
        self.assertTrue(len(id_number) == 13, 'If ID length equals 13, it should return true')


class TestLotto(unittest.TestCase):
    def test_generate_lott(self):
        lotto_number = random.randint(1, 49)
        self.assertFalse(50 > lotto_number > 1, 'Lotto number within range 1 to 49')

    def test_count(self):
        self.count = 0
        lotto_number = random.randint(1, 49)
        user_number = self.number_entry.get()
        if lotto_number == user_number:
            self.count += 1
        self.assertTrue(lotto_number == user_number, 'If lotto number equals the users number a count of 1 should'
                                                     ' return true')


if __name__ == '__main__':
    unittest.main()
