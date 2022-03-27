from src.model.payment import Payment


class Employee:

    def __init__(self, name):
        self.name = name
        self.payments = []

    def add_payments(self, payment: Payment):
        self.payments.add(payment)
