#coding=utf-8
from django.db import models
from cdealer.cart.models import Cart,CartItem
from django.contrib.auth.models import User
import datetime
# Create your models here.

STATUS_CHOICE=(
    (u'new',u'新订单'),
    (u'paid',u'已支付'),
    (u'deliver',u'已发货'),
    (u'discard',u'已作废'),
)
SHIPPING_CHOICE=(
	(u'post',u'平邮'),
	(u'deliver',u'快递'),
	(u'ems',u'EMS')
)
PAYMENT_CHOICE=(
	(u'alipay',u'支付宝'),
	(u'bank',u'网银'),
)

class Order(models.Model):
    d=datetime.datetime.today()
    seriesnum=models.CharField(max_length=32,verbose_name=u'订单流水号',default=d.strftime('%Y%m%d%H%M%S%f'),unique=True)
    cart=models.ForeignKey(Cart,verbose_name=u'所购专辑')
    user=models.ForeignKey(User,verbose_name=u'下单用户',blank=True,null=True)
    receiver_name=models.CharField(max_length=32,verbose_name=u'收货人姓名')
    receiver_phone=models.CharField(max_length=16,verbose_name=u'收货人电话')
    receiver_postcode=models.CharField(max_length=6,verbose_name=u'邮政编码')
    receiver_address=models.TextField(verbose_name=u'收件人地址')
    shipping=models.CharField(max_length=8,verbose_name=u'送货方式',choices=SHIPPING_CHOICE)
    payment=models.CharField(max_length=8,verbose_name=u'支付方式',choices=PAYMENT_CHOICE)
    status=models.CharField(max_length=8,choices=STATUS_CHOICE,verbose_name=u'订单状态',default='new')
    date=models.DateTimeField(auto_now_add=True,verbose_name=u'下单时间')

    def __unicode__(self):
        return self.seriesnum

    def total_price(self):
        return self.cart.total_price()

    def amount_of_item(self):
        return self.cart.amount_of_item()
    def get_items(self):
        items=CartItem.objects.filter(cart=self.cart)
        return items

    
