# Create your views here.
from cdealer.cart.models import Cart,CartItem
from cdealer.album.models import Album
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
def add_item(request):
	cart=request.session['cart']
	url=request.path
	if request.method=='POST':
		album_id=int(request.POST['item_id'])
		amount=int(request.POST['amount'])
		cart_items=CartItem.objects.filter(cart=cart)
		for item in cart_items:
			if album_id==item.product.id:
				item.amount+=amount
				item.save()
				return HttpResponseRedirect(request.META['HTTP_REFERER'])
		else:
			cart_item=CartItem()
			cart_item.cart=cart
			cart_item.product=Album.objects.get(id=album_id)
			cart_item.amount=amount
			cart_item.save()
		return HttpResponseRedirect(request.META['HTTP_REFERER'])
	else:
		pass
	
def view_cart(request):
	cart=request.session['cart']
	cart_items=CartItem.objects.filter(cart=cart)
	return render_to_response('cart.html',{'cart_items':cart_items},context_instance=RequestContext(request))

def delete_item(request):
	cart=request.session['cart']
	if(request.method=='GET'):
		item_id=request.GET['item_id']
		CartItem.objects.filter(id=int(item_id)).delete()
		request.session['cart']=cart
	else:
		pass
	return HttpResponseRedirect(request.META['HTTP_REFERER'])
