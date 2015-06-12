from django import forms
from .models import PlantDetailPost

class PlantDetailForm(forms.ModelForm):
	class Meta:
		model = PlantDetailPost
		fields = ["name","temperature","moisture","humidity"]

