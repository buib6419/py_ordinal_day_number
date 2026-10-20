import unittest
from datetime import date
from py_ordinal_day_number import date_to_ordinal, ordinal_to_date, EPOCH


class TestOrdinalDayNumber(unittest.TestCase):
    def test_epoch_maps_to_one(self):
        self.assertEqual(date_to_ordinal(date(1970, 1, 1)), 1)

    def test_round_trip(self):
        d = date(2024, 3, 15)
        self.assertEqual(ordinal_to_date(date_to_ordinal(d)), d)

    def test_known_value(self):
        # 1970-01-01 is day 1, so 1970-01-02 is day 2
        self.assertEqual(date_to_ordinal(date(1970, 1, 2)), 2)
        self.assertEqual(ordinal_to_date(2), date(1970, 1, 2))

    def test_leap_day(self):
        d = date(2000, 2, 29)
        n = date_to_ordinal(d)
        self.assertEqual(ordinal_to_date(n), d)

    def test_pre_epoch_raises(self):
        with self.assertRaises(ValueError):
            date_to_ordinal(date(1969, 12, 31))

    def test_zero_ordinal_raises(self):
        with self.assertRaises(ValueError):
            ordinal_to_date(0)

    def test_negative_ordinal_raises(self):
        with self.assertRaises(ValueError):
            ordinal_to_date(-1)

    def test_non_date_raises(self):
        with self.assertRaises(TypeError):
            date_to_ordinal("2024-01-01")

    def test_non_int_raises(self):
        with self.assertRaises(TypeError):
            ordinal_to_date("1")

    def test_bool_rejected(self):
        with self.assertRaises(TypeError):
            ordinal_to_date(True)

    def test_subclass_of_date_works(self):
        class MyDate(date):
            pass
        md = MyDate(2020, 6, 1)
        self.assertEqual(ordinal_to_date(date_to_ordinal(md)), date(2020, 6, 1))

    def test_epoch_constant(self):
        self.assertEqual(EPOCH, date(1970, 1, 1))


if __name__ == "__main__":
    unittest.main()
