from cdealer.category.models import Category

def categoryinfo(request):
	categories=Category.objects.all()
	return {'categories':categories}

	
