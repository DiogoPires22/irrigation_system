from django.db import models

# Create your models here.


class SoilMoistureControl(models.Model):
	moisture= models.IntegerField(default=0)
	date= models.DateTimeField(auto_now_add=True,blank=True)
	
	
	
class Status(models.Model):
	status = models.IntegerField(default=1)
