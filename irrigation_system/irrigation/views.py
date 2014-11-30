from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext,loader

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