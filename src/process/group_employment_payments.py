from data_classification import get_employee_name
from read_file import read_payment_data


def create_employee_payments(file_path):
    employees_names = set()
    raw_data = read_payment_data(file_path)
    for payment_line in raw_data:
        employees_names.add(get_employee_name(payment_line))

