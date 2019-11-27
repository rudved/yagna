from django.db import models

# Create your models here.
class SavingsAccount(models.Model):
    acno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blc = models.DecimalField(max_digits=30,decimal_places=2)
