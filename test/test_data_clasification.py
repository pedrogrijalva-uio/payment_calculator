import unittest

from src.data_clasification.data_clasification import get_employee_name
from src.exceptions.data_exceptions import EmployeeNameException


class TestDataClassification(unittest.TestCase):

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
