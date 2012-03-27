#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from cdealer.album.models import Album
# Create your models here.

class Cart(models.Model):
	user=models.ForeignKey(User,verbose_name=u"用户",blank=True,null=True)
	session=models.CharField(blank=True,max_length=100)
	creation_date=models.DateTimeField(verbose_name=u"创建日期",auto_now_add=True)
	modification_date=models.DateTimeField(verbose_name=u"修改日期",auto_now_add=True,auto_now=True)
	def __unicode__(self):
		return "%s,%s" % (self.user,self.session)

	def amount_of_item(self):
		count=0
		items=CartItem.objects.filter(cart=self)
		for item in items:
			count+=1
		return count

	def total_price(self):
		items=CartItem.objects.filter(cart=self)
		c=0;
		for item in items:
			c=c+item.get_price()*item.amount
		return c;	
	def get_items(self):
		items=CartItem.objects.filter(cart=self)
		return items

class CartItem(models.Model):
	cart=models.ForeignKey(Cart,verbose_name=u"购物车")
	product=models.ForeignKey(Album,verbose_name=u"专辑")
	amount=models.IntegerField()

	def __unicode__(self):
		return self.product

	def get_price(self):
		return self.product.price
	def total_price(self):
		return self.product.price*self.amount

