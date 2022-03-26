import re

from src.exceptions.data_exceptions import EmployeeNameException


def get_employee_name(worked_hours_data):
    employee_name = worked_hours_data.split("=")[0]
    if re.findall("/^[A-Z]+$/g]", employee_name):
        return employee_name
    raise EmployeeNameException("Invalid name")
