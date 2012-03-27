#coding=utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from cdealer.customer.models import Customer

class CustomerInline(admin.StackedInline):
    model = Customer
    fk_name = 'user'
    max_num = 1
    verbose_name='用户信息'
    verbose_name_plural='用户信息'
    
class CustomerAdmin(UserAdmin):
    inlines = [CustomerInline,]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','date_joined',)

    
admin.site.unregister(User)
admin.site.register(User, CustomerAdmin)
