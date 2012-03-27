from django.contrib import admin 
from cdealer.order.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display=('seriesnum','receiver_name','status','date',)
    search_fields=('seriesnum','date','user',)
    list_filter=('status',)
    readonly_fields=('seriesnum',)
    fields=('seriesnum','status','receiver_name','receiver_phone','receiver_postcode','receiver_address',)

admin.site.register(Order,OrderAdmin)
