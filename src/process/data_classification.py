import re

from src.constants import PAYMENT_DAYS
from src.exceptions.data_exceptions import EmployeeNameException, PaymentDataException, PaymentDayInformationException
from src.model.payment import Payment


def check_payment_data(payment_data):
    if len(payment_data.split("=")) != 2:
        raise PaymentDataException


def get_employee_name(worked_hours_data):
    employee_name = worked_hours_data.split("=")[0]
    if employee_name.isalpha():
        return employee_name
    raise EmployeeNameException("Invalid name")


def check_payment_format(payment_by_day, payments):
    for payment_day in PAYMENT_DAYS:
        payment_re = "^" + payment_day + "\d{2}:?\d{2}:?-\d{2}:?\d{2}:?"
        payment_is_valid = re.match(payment_re, payment_by_day)
        if not payment_is_valid:
            raise PaymentDayInformationException
        payments.add(Payment(payment_day, get_payment_hour_range(payment_day, payment_by_day)))


def get_payment_hour_range(payment_day, payment_by_day):
    return payment_by_day.split(payment_day)[1]
