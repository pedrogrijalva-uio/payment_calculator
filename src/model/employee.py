from src.model.payment import Payment
from functools import reduce


class Employee:

    def __init__(self, name):
        self.name = name
        self.payments = []
        self.total_payment = 0

    def calculate_total_payment(self):
        total_payments = [payment.total for payment in self.payments]
        self.total_payment = reduce((lambda x, y: x + y), total_payments)
