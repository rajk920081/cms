from django.db import models


# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    mobile=models.CharField(max_length=12)
    gender=models.CharField(max_length=10)
    # def __str__(self):
    #     return self.name