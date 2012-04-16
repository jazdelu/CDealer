# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from cdealer.cart.utils import create_or_get_cart
from cdealer.album.models import Album

def index_loader(request):
	gallery=Album.objects.filter(setToGallery=True)
	new_list=Album.objects.all().order_by('-release_date')
	return render_to_response('index.html',{'gallery':gallery,'new_list':new_list[:8]},context_instance=RequestContext(request))

def contact(request):
    return render_to_response('contact.html',context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html',context_instance=RequestContext(request))
