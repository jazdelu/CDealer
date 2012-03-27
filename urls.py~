from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from cdealer.index.views import index_loader,contact
from cdealer.customer.views import register,login,logout,change_profile,change_pswd
from cdealer.category.views import get_all_categories
from cdealer.album.views import get_album_list,get_album
from cdealer.cart.views import add_item,view_cart,delete_item
from cdealer.order.views import create_order,get_orders
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index_loader),
    url(r'^index/',index_loader),
    url(r'^contact/',contact),
	url(r'^register/',register),
	url(r'^login/',login),
	url(r'^logout/',logout),
	url(r'^profile/change_profile/',change_profile),
	url(r'^profile/change_pswd/',change_pswd),
	url(r'^album/$',get_album_list),
	url(r'^album/(\d+)/',get_album),
	url(r'^cart/$',view_cart),
	url(r'^cart/add_item/$',add_item),
	url(r'^cart/delete_item/$',delete_item),
	url(r'^order/create_order/$',create_order),
	url(r'^order/my_orderlist/$',get_orders),
    # url(r'^cdealer/', include('cdealer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^files/',include('django_bfm.urls')),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/cdealer/static/css/'}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/cdealer/static/js/'}),
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/cdealer/static/images/'}),
)
