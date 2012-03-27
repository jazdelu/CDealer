# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from cdealer.cart.utils import create_or_get_cart
from cdealer.category.models import Category

def index_loader(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def contact(request):
    return render_to_response('contact.html',context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html',context_instance=RequestContext(request))
