# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from cdealer.category.models import Category

def get_all_categories(request):
	albums=Category.objects.all()
	return render_to_response('categories.html',{'albums',album},context_instance=RequestContext(request))
