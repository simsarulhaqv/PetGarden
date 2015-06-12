from django.db import models
from add_plant.models import Plant

# Create your models here.

class PlantDetailPost(models.Model):
	name = models.CharField(max_length=30)
	temperature = models.IntegerField()
	moisture = models.IntegerField()
	humidity = models.IntegerField()



	def __unicode__(self):
		return self.name