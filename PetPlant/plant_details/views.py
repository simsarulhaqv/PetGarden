from django.shortcuts import render
from django.http import HttpResponse
from .forms import PlantDetailForm
from .models import PlantDetailPost

# Create your views here.

def blog_view(request):
	print PlantDetailPost.objects.all()
	detail_dictionary = {}
	detail_dictionary["plant_info"]=PlantDetailPost.objects.all().order_by("-id")
	return render(request,"plant_detail.html",detail_dictionary)

