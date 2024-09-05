from django.db import models

# Create your models here.
class emp(models.Model):
    name = models.CharField(max_length=200)
    emp_id = models.IntegerField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=10)
