from unittest.util import _MAX_LENGTH
from django.db import models

class azubi_tbl(models.Model):    
  Id = models.IntegerField(max_length=6, unique=True)
  name = models.CharField(max_length=20, null=True)
  birthdate = models.DateField()
  address = models.CharField(max_length=30, default='',null=True)
  phoneNo = models.IntegerField(default='',null=True)
  email = models.CharField(max_length=30,null=True) 

  def __str__(self):
    return str(self.name)

class kaufmann(models.Model):
  Id = models.ForeignKey(azubi_tbl, on_delete=models.CASCADE)
  name = models.CharField(max_length=20, null=True)
  salary = models.IntegerField(max_length=4)

  def __self__(self):
    return str(self.Id)