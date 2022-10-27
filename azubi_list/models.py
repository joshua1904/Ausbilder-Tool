from distutils.command.build_scripts import first_line_re
from email.policy import default
from django.db import models

# Create your models here.
class My_List(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class AzubiData(models.Model):
    topic = models.ForeignKey(My_List, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    birthday = models.CharField(max_length=32, default="Leer")


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

