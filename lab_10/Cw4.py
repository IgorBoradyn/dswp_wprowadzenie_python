from datetime import date
from dateutil import relativedelta


def calculate_age(birthday):
    today = date.today()

    diff = relativedelta.relativedelta(today, birthday)
    age_years = diff.years
    age_months = diff.months
    age_days = diff.days

    next_birthday = date(today.year, birthday.month, birthday.day)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    days_left = (next_birthday - today).days

    print(f"Dzisiaj masz {age_years} lat, {age_months} miesięcy i {age_days} dni.")
    print(f"Do twoich kolejnych urodzin pozostało {days_left} dni.")


calculate_age(date(1998, 9, 17))
