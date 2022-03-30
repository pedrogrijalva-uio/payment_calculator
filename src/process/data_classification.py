import re

from src.exceptions.data_exceptions import EmployeeNameException, PaymentDataException, PaymentDayInformationException
from src.model.payment import Payment


def check_payment_data_format(payment_data):
    if len(payment_data.split("=")) != 2:
        raise PaymentDataException


def get_employee_name(worked_hours_data):
    employee_name = worked_hours_data.split("=")[0]
    if employee_name.isalpha():
        return employee_name
    raise EmployeeNameException("Invalid name")


def set_payments_by_day(worked_hours_data):
    employee_payments = []
    payments_for_employee = worked_hours_data.split("=")[1].split(",")
    for payment in payments_for_employee:
        check_hour_payment_format(payment)
        payment_day = payment[0:2]
        payment = Payment(payment_day, get_payment_hour_range(payment_day, payment))
        payment.calculate_payment()
        employee_payments.append(payment)
    return employee_payments


def check_hour_payment_format(payment_day_and_hours):
    payment_re = "^[A-Z][A-Z]\d{2}:?\d{2}:?-\d{2}:?\d{2}:?"
    payment_is_valid = re.match(payment_re, payment_day_and_hours)
    if not payment_is_valid:
        raise PaymentDayInformationException


def get_payment_hour_range(payment_day, payment_by_day):
    return payment_by_day.split(payment_day)[1]
