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
        range_hours = "11:00-10:00"
        payment = Payment("MO", range_hours)

        with self.assertRaises(InvalidHourRangeException):
            payment.validate_range()

    def test_should_raise_invalid_hour_range_exception_when_hour_range_does_not_matches_rules(self):
        received_range_hour = "00:01-10:00"
        payment = Payment("MO", received_range_hour)

        with self.assertRaises(InvalidHourRangeException):
            payment.check_matching_hour_range()

    def test_should_set_payment_hour_range_when_received_range_hour_is_correct(self):
        received_range_hour = "10:00-12:00"
        payment = Payment("MO", received_range_hour)
        expected_payment_range = "09:01-18:00"

        payment.check_matching_hour_range()

        self.assertEqual(expected_payment_range, payment.payment_hour_range)

    def test_should_return_payment_value_when_using_correct_range(self):
        received_range_hour = "10:00-12:00"
        payment = Payment("MO", received_range_hour)
        expected_payment = 30
        payment.payment_hour_range = "09:01-18:00"

        payment.calculate_worked_hours(2)

        self.assertEqual(expected_payment, payment.total)
