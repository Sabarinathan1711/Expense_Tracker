from datetime import datetime
from config import DATE_FORMAT

def get_today_date():
    return datetime.now().strftime(DATE_FORMAT)

def validate_amount(value):
    try:
        amount = float(value)
        return amount > 0
    except ValueError:
        return False
