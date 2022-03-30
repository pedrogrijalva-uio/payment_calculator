import unittest

from src.process.data_classification import get_employee_name, check_payment_data_format
from src.exceptions.data_exceptions import EmployeeNameException, PaymentDataException, PaymentDayInformationException
from src.process.data_classification import check_hour_payment_format


class TestDataClassification(unittest.TestCase):

    def test_should_throw_payment_day_information_exception_when_payment_date_is_incorrect(self):
        test_payment_date = "MO0:00-12:00"
        with self.assertRaises(PaymentDayInformationException):
            check_hour_payment_format(test_payment_date, "ME")

    def test_should_throw_exception_when_data_is_not_well_constructed(self):
        test_data = "RENEMO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
        with self.assertRaises(PaymentDataException):
            check_payment_data_format(test_data)

    def test_should_return_employee_name_when_reading_data_set(self):
        test_data = "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
        expected_employee_name = "RENE"
        employee_name = get_employee_name(test_data)
        assert employee_name == expected_employee_name

    def test_should_throw_exception_when_employee_name_contains_not_alphabetic_characters(self):
        test_data = "R1NE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
        with self.assertRaises(EmployeeNameException):
            get_employee_name(test_data)

    def test_should_throw_exception_when_employee_name_is_empty(self):
        test_data = "=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
        with self.assertRaises(EmployeeNameException):
            get_employee_name(test_data)
