from src.model.employee import Employee
from src.process.data_classification import get_employee_name, set_payments_by_day
from src.process.read_file import read_payment_data


class PaymentReport:

    def __init__(self):
        self.employees = None

    def create_employees_payment_report(self, file_path):
        payments_by_employee = read_payment_data(file_path)
        self.employees = [self.create_employee(worked_hours_data) for worked_hours_data in payments_by_employee]

    def create_employee(self, worked_hours_data):
        employee_name = get_employee_name(worked_hours_data)
        employee = Employee(employee_name)
        employee.payments.extend(set_payments_by_day(worked_hours_data))
        employee.calculate_total_payment()
        return employee

    def print_payment_results(self):
        for employee in self.employees:
            print(f"The amount to pay {employee.name} is: {employee.total_payment} USD")




