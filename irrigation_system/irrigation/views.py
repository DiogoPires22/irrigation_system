from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext,loader
from django.views.decorators.csrf import csrf_protect

from django.core import serializers

# Create your views here.

from irrigation.models import SoilMoistureControl,Status




def index(request):
	teste=1
	template=loader.get_template("irrigation/index.html")
	return HttpResponse(template)




def logs(request):
	moistureList=SoilMoistureControl.objects.order_by('-date')[:5]
	status= Status.objects.all()[0]
	
	template=loader.get_template('irrigation/logs.html')
	context=RequestContext(request,{
		'moistureList':moistureList,
		'status':status
	})
	return HttpResponse(template.render(context))
	
	
def arduinos(request):
	arduinoList=Status.objects.all()
	template=loader.get_template('irrigation/arduinos.html')
	context=RequestContext(request,{
		'arduinoList':arduinoList
	})

	return HttpResponse(template.render(context))
	
	
def getMoisture(request):
	if request.method=='POST':
		moistureID=request.POST["lastID"]
		
	if moistureID:
		newMoistures= SoilMoistureControl.objects.order_by('id').filter(id__gt=moistureID)[:5]
		return HttpResponse(serializers.serialize("json",newMoistures),content_type="application/json")
	
	return HttpResponse("")
		

	
