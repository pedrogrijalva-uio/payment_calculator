from datetime import datetime, timedelta

from src.constants import PAYMENT_RULES, PAYMENT_WEEKDAYS, PAYMENT_WEEKEND
from src.exceptions.data_exceptions import InvalidHourRangeException, InvalidHourValueException


class Payment:

    def __init__(self, payment_day, hour_range):
        self.total = 0
        self.payment_day = payment_day
        self.start_hour, self.end_hour = self._payment_hour_ranges(hour_range)
        self.start_hour_range, self.end_hour_range = None, None
        self.payment_hour_range = ""

    def calculate_payment(self):
        self.validate_payment_hour_range()
        self.check_matching_hour_range()
        self.calculate_worked_hours()

    def _payment_hour_ranges(self, hour_range):
        hour_ranges = hour_range.split("-")
        start_hour = self._hour_string_to_date(hour_ranges[0])
        end_hour = self._hour_string_to_date(hour_ranges[1])
        return start_hour, end_hour

    def _hour_string_to_date(self, hour_range):
        try:
            payment_hour = datetime.strptime(hour_range, "%H:%M")
            if hour_range == "00:00":
                payment_hour = payment_hour + timedelta(days=1)
            return payment_hour
        except ValueError:
            raise InvalidHourValueException

    def validate_payment_hour_range(self):
        if self.start_hour >= self.end_hour:
            raise InvalidHourRangeException

    def count_worked_hours(self):
        return self.end_hour - self.start_hour

    def check_matching_hour_range(self):
        for key, value in PAYMENT_RULES.items():
            self.start_hour_range, self.end_hour_range = self._payment_hour_ranges(key)
            if self.start_hour >= self.start_hour_range and self.end_hour <= self.end_hour_range:
                self.payment_hour_range = key
                return
        raise InvalidHourRangeException

    def __get_hour_price(self):
        if self.payment_day in PAYMENT_WEEKDAYS:
            return PAYMENT_RULES[self.payment_hour_range]["weekday"]
        elif self.payment_day in PAYMENT_WEEKEND:
            return PAYMENT_RULES[self.payment_hour_range]["weekend"]

    def calculate_worked_hours(self):
        worked_hours = self.count_worked_hours()
        hours, remainder = divmod(worked_hours.seconds, 3600)
        self.total = hours * self.__get_hour_price()
