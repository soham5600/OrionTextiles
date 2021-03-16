from django.db import models
from django.utils import timezone
# Create your models here.
class Data(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	cloth=models.TextField()
	dimension=models.DecimalField(max_digits=100,decimal_places=3)

#Soham@1234