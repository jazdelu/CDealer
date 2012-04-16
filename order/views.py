#coding=utf-8
from cdealer.order.models import Order
from cdealer.order.forms import OrderForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from datetime import datetime
# Create your views here.

def checkout(request):
	if request.method=='POST':
		form=OrderForm(request.POST)
		if form.is_valid():
			order=form.save()
			order.cart=request.session['cart']
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
	return render_to_response('checkout.html',{'form':form},context_instance=RequestContext(request))

def get_orders(request):
	orders=[]
	if request.user.is_authenticated():
		orders=Order.objects.all()
		if request.method=='POST':
			if request.POST['from']:
				fromdate=datetime.strptime(request.POST['from'],"%Y-%m-%d")
				orders=orders.filter(date__gt=fromdate)
			if request.POST['to']:
				todate=	datetime.strptime(request.POST['to'],"%Y-%m-%d")
				orders=orders.filter(date__lt=todate)
		return render_to_response('order_list.html',{'orders':orders},context_instance=RequestContext(request))
	elif request.method=='POST':
		orders=Order.objects.filter(seriesnum=request.POST.get('s',''))
		if orders:
			return render_to_response('order_list.html',{'orders':orders},context_instance=RequestContext(request))
		else:
			return render_to_response('search.html',{'error':u'订单流水号输入有误'},context_instance=RequestContext(request))
	else:
		return render_to_response('search.html',context_instance=RequestContext(request))

def get_order(request,num):
	if request.method=='GET':
		try:
			order=Order.objects.get(seriesnum=request.GET['q'])
		except Order.DoesNotExist:
			return render_to_response('search.html',{'message':u'您输入的订单流水号不存在'},context_instance=RequestContext(request))
	return render_to_response('order_detail.html',{'order':order},context_instance=RequestContext(request))

def payment(request):
	if request.method=='GET':
		oid=request.GET['']
	
