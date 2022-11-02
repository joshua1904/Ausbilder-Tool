from django.db import models


class department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

  
class Azubi(models.Model):
    topic = models.ForeignKey(department, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    birthday = models.DateField()
    department = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.
