from datetime import date, timedelta
import unittest


def add_days(start_date, num_days):
    return start_date + timedelta(days=num_days)


def subtract_days(start_date, num_days):
    return start_date - timedelta(days=num_days)


class TestModule(unittest.TestCase):

    def test_addition(self):
        d1 = date(2000, 1, 1)
        td = timedelta(weeks=2)
        result = add_days(d1, td.days)
        self.assertEqual(result, date(2000, 1, 15))
        print("test_addition test module is passed.")

    def test_subtraction(self):
        d1 = date(2000, 1, 1)
        td = timedelta(days=10)
        result = subtract_days(d1, td.days)
        self.assertEqual(result, date(1999, 12, 22))
        print("test_subtraction test module is passed.")


if __name__ == '__main__':
    unittest.main()
