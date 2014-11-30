from django.db import models

# Create your models here.


class SoilMoistureControl(models.Model):
	moisture= models.IntegerField(default=0)
	date= models.DateTimeField(auto_now_add=True,blank=True)
	arduinoID= models.IntegerField(default=0) 
