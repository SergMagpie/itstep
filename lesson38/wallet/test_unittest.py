import unittest
from main import ConsoleInterface
from wallet import Wallet
from datetime import date


class TestConsoleInterface(unittest.TestCase):
    def setUp(self):
        self.to_test = ConsoleInterface(Wallet)

    def test_money_validator(self):
        self.assertEqual(self.to_test.money_validator('20.5'), 20.5)
        self.assertEqual(self.to_test.money_validator('-20.5'), -20.5)
        self.assertEqual(self.to_test.money_validator('0'), 0.0)
        self.assertEqual(self.to_test.money_validator('d'), None)
        self.assertEqual(self.to_test.money_validator('3,3'), None)

    def test_int_validator(self):
        self.assertEqual(self.to_test.int_validator('0'), 0)
        self.assertEqual(self.to_test.int_validator('1'), 1)
        self.assertEqual(self.to_test.int_validator('-1'), -1)
        self.assertEqual(self.to_test.int_validator('999'), 999)
        self.assertEqual(self.to_test.int_validator('lk'), None)

    def test_date_validator(self):
        self.assertEqual(self.to_test.date_validator(
            '2021/09/15'), date(2021, 9, 15))
        self.assertEqual(self.to_test.date_validator(
            '2021-09-15'), None)
        self.assertEqual(self.to_test.date_validator(
            '2021/09/31'), None)
        self.assertEqual(self.to_test.date_validator(
            '2025/09/15'), date(2025, 9, 15))
        self.assertEqual(self.to_test.date_validator(
            '2025.09.15'), None)
        self.assertEqual(self.to_test.date_validator(
            '2025/13/15'), None)
        self.assertEqual(self.to_test.date_validator(
            '1988,09,15'), None)


if __name__ == "__main__":
    unittest.main()
