#coding=utf-8
from django import forms
from cdealer.order.models import Order

class OrderForm(forms.ModelForm):
	class Meta:
		model=Order
		exclude=('status','seriesnum','user')
		
