import unittest

from src.exceptions.data_exceptions import InvalidHourRangeException, InvalidHourValueException
from src.model.payment import Payment


class TestPayment(unittest.TestCase):

    def test_should_raise_invalid_hour_range_exception_when_start_hour_is_larger_than_end_hour(self):
        range_hours = "12:00-10:00"
        payment = Payment("MO", range_hours)
        with self.assertRaises(InvalidHourRangeException):
            payment.validate_range()

    def test_should_raise_invalid_hour_value_exception_when_start_hour_is_larger_than_end_hour(self):
        range_hours = "09:99-10:00"
        payment = Payment("MO", range_hours)
        with self.assertRaises(InvalidHourValueException):
            payment.validate_range()
