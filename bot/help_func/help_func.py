from datetime import datetime
import secrets
from bot.db.sqlite import *


def get_date():
    current_date = datetime.now()
    day = current_date.day
    day = str(day).rjust(2, '0')
    month = current_date.month
    month = str(month).rjust(2, '0')
    year = current_date.year
    date = f"{day}-{month}-{year}"

    return date
