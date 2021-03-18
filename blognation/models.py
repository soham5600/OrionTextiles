from django.db import models
from django.utils import timezone
# Create your models here.
CLOTH_CHOICES = ( 
    ("1", "100% Cotton"), 
    ("2", "Polycotton"), 
    ("3", "Polyviscos"), 
    ("4", "100% Polycotton")
)
class Data(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	cloth=models.CharField(max_length=100,choices=CLOTH_CHOICES,default="1")
	dimension=models.DecimalField(max_digits=100,decimal_places=3)

#Soham@1234