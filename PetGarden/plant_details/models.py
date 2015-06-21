from django.db import models
from add_plant.models import Plant

# Create your models here.

class PlantDetailPost(models.Model):
	CTIMES = models.CharField(max_length=30)
	TEMP = models.IntegerField()
	HUMID = models.IntegerField()
	MOIST = models.IntegerField()
	LIGHT = models.IntegerField()
	SURFTEMP = models.IntegerField()
	LEAFMOIST = models.IntegerField()
	RTIME = models.IntegerField()


	def __unicode__(self):
		return self.CTIMES
		