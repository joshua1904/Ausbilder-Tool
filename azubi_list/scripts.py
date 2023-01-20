import datetime
from .models import Azubi, DayCheck

############## funktionen für Datumsabfrage ##############
def get_day() -> datetime.datetime:
    return datetime.date.today()

# Gibt zurück ob der 01.09. ist
def is_new_training_year() -> bool:
    today = get_day()
    new_training_year =  datetime.date(today.year, 9, 1)
    if today == new_training_year or today > new_training_year:
        return True
    return False

def change_training_year_if_neccessary():
    if not is_day_already_checked() and is_new_training_year():
        change_training_year_of_all()


def is_day_already_checked():
    print("js,nf")
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
############## funktionen für Datumsabfrage ##############


############## funktionen für Sortieren ##############
def sort_azubi_2(azubis):
    azubis = list(azubis)
    azubis.sort(key = lambda azubi: (azubi.first_name, azubi.last_name))
    print(azubis)

def get_position(char: str):
    """gibt die alphabet nummer von einem char an (nur kleinbuchstaben)"""
    return ord(char)- 97 

def sort_azubis(azubi_list: list): 
    print(sort_azubi_2(azubi_list))
    solution_list = []   
    sorted_list_by_last_name =  sorted(azubi_list, key=lambda azubi: azubi.last_name)
    sorted_list_by_alphabet = list()
    for i in range(26):
        sorted_list_by_alphabet.append([])
    for azubi in sorted_list_by_last_name:
        sorted_list_by_alphabet[get_position(azubi.last_name.lower()[0])]
    
    for azubi_list in sorted_list_by_alphabet:
        solution_list += sorted(azubi_list, key= lambda azubi: azubi.first_name)
    
    return solution_list


############## funktionen für Sortieren ##############


