from django.db import models
from Ausbilder_Tool import settings

class Profession(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

  
class Azubi(models.Model):
    #sobald die Berufsgruppe Gelöscht werden kann sollte man eine Warnung aussprechen oder das on_delete programm abändern(sonst löschen sich alle Azubis aus der Berufsgruppe automatisch)
    topic = models.ForeignKey(Profession, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    birthday = models.DateField()
    address = models.CharField(max_length=30)
    PLZ = models.CharField(max_length=20)
    department = models.CharField(max_length=30)
    year = models.IntegerField()
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class DayCheck(models.Model):
    day = models.DateField()
    changed =models.IntegerField()

