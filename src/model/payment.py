from datetime import datetime

from src.exceptions.data_exceptions import InvalidHourRangeException, InvalidHourValueException


class Payment:

    def __init__(self, payment_day, hour_range):
        self.total = 0
        self.payment_day = payment_day
        hour_ranges = hour_range.split("-")
        self.start_hour = hour_ranges[0]
        self.end_hour = hour_ranges[1]

    def validate_range(self):
        try:
            start_hour = datetime.strptime(self.start_hour, "%H:%M")
            end_hour = datetime.strptime(self.end_hour, "%H:%M")
            if start_hour > end_hour:
                raise InvalidHourRangeException
        except ValueError:
            raise InvalidHourValueException
