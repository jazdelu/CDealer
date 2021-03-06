# Create your views here.
from cdealer.album.models import Album
from cdealer.category.models import Category
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

def get_album_list(request):
	albums=[]
	if request.method=='GET':
		albums=Album.objects.all()
		if request.GET.get('q',''):
			albums=Album.objects.filter(name__contains=request.GET['q'])
		if request.GET.get('a',''):
			albums=Album.objects.filter(artist=request.GET['a'])
		if request.GET.get('c',''):
			c=Category.objects.get(id=int(request.GET['c']))
			albums=c.entries.all()
	else:
		albums=Album.objects.all()
	return render_to_response('album_list.html',{'albums':albums},context_instance=RequestContext(request))

def get_album(request,i):
	d=0
	try:
		d=int(i)
	except ValueError:
		raise Http404()
	album=Album.objects.get(id=d)
	return render_to_response('details.html',{'album':album},context_instance=RequestContext(request))
	
	
	
	
