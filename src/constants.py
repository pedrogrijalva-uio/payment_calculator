PAYMENT_WEEKDAYS = ["MO", "TU", "WE", "TH", "FR"]
PAYMENT_WEEKEND = ["SA", "SU"]
PAYMENT_DAYS = PAYMENT_WEEKDAYS + PAYMENT_WEEKEND

PAYMENT_RULES = {
    "00:01-09:00": {
        "weekday": 25,
        "weekend": 30
    },
    "09:01-18:00": {
        "weekday": 15,
        "weekend": 20
    },
    "18:01-00:00": {
        "weekday": 20,
        "weekend": 25
    }
}
