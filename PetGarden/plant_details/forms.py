from django import forms
from .models import PlantDetailPost

class PlantDetailForm(forms.ModelForm):
	class Meta:
		model = PlantDetailPost
		fields = ["CTIMES","TEMP","HUMID","MOIST","LIGHT","SURFTEMP","LEAFMOIST","RTIME"]

