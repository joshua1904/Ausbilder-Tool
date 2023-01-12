import datetime
from .models import Azubi, DayCheck

def get_day() -> datetime.datetime:
    return datetime.date.today()

# Gibt zurück ob der 01.09. ist
def is_new_training_year() -> bool:
    is_day_already_checked()
    today = get_day()
    if today == datetime.date(today.year, 9, 1):
        return True
    return False

def change_training_year_if_neccessary():
    if not is_day_already_checked() and is_new_training_year():
        change_training_year_of_all()


def is_day_already_checked():
    if len(list(DayCheck.objects.all())) > 0:
        daycheck = DayCheck.objects.all()[0]
    else:
        daycheck = DayCheck(day= get_day(), changed= 0)
        daycheck.save()
    if daycheck.day != get_day():
        daycheck.day = get_day()
        daycheck.changed = 1
        daycheck.save()
        return False
    return True


def change_training_year_of_all():
    azubis= list(Azubi.objects.all())
    for azubi in azubis:
        azubi.year += 1
        azubi.save()

