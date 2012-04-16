from cdealer.link.models import Link

def get_links(request):
	links=Link.objects.all().order_by('name')
	return {'links':links}
