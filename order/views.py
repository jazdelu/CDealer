from cdealer.order.models import Order
from cdealer.order.forms import OrderForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.http import HttpResponseRedirect
# Create your views here.

def create_order(request):
	if request.method=='POST':
		form=OrderForm(request.POST)
		form.initial={'cart':request.session['cart']}
		if form.is_valid():
			order=form.save()
			if request.user.is_authenticated():
				order.user=request.user
			else:
				order.user=None
			order.save()
			del request.session['cart']
			return render_to_response('order_success.html',{'order':order},context_instance=RequestContext(request))
		else:
			return render_to_response('order_success.html',{'form':form},context_instance=RequestContext(request))
	else:
		form=OrderForm()
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def get_orders(request):
	orders=[]
	if request.user.is_authenticated():
		orders=Order.objects.filter(user=request.user)
	else:
		if request.method=='GET':
			orders=Order.objects.filter(seriesnum=request.GET['s'])
	return render_to_response('order_list.html',{'orders':orders},context_instance=RequestContext(request))

def get_order(request,num):
	if request.method=='GET':
		order=Order.objects.get(id=num)
	return render_to_response('order_detail.html',{'order_detail.html'},context_instance=RequestContext(request))

	
	
