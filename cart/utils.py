from cdealer.cart.models import Cart

def create_or_get_cart(request):
	cart=Cart()
	try:
		cart=request.session['cart']
	except KeyError:
		if request.user.is_authenticated():
			cart.user=request.user
		else:
			cart.user=None;
		cart.session=request.session.session_key
		cart.save()
		request.session['cart']=cart
	return {'cart':cart}
		

