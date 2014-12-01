from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext,loader
from django.views.decorators.csrf import csrf_protect

from django.core import serializers

# Create your views here.

from irrigation.models import SoilMoistureControl


def index(request):
	moistureList=SoilMoistureControl.objects.order_by('-date')[:5]
	moistureLast=SoilMoistureControl.objects.order_by('-pk')[0]
	template=loader.get_template('irrigation/index.html')
	context=RequestContext(request,{
		'moistureList':moistureList,
		'lastmoisture':moistureLast,
	})

	return HttpResponse(template.render(context))
	
	
def getMoisture(request):
	if request.method=='POST':
		moistureID=request.POST["lastID"]
		
	if moistureID:
		newMoistures= SoilMoistureControl.objects.filter(id__gt=moistureID).order_by('-date')[:5]
		return HttpResponse(serializers.serialize("json",newMoistures),content_type="application/json")
	
	return HttpResponse("")
		

	
