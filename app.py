import json
import os

from src.model.payment_report import PaymentReport

ROOT_DIR = os.path.dirname(__file__)

if __name__ == "__main__":
    payments_file = ROOT_DIR + "/test/data/data.txt"
    try:
        payment_report = PaymentReport()
        payment_report.create_employees_payment_report(payments_file)
        payment_report.print_payment_results()
    except Exception as error:
        print("Error reading payments file. Review the data.")

