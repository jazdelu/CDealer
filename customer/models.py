# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

PSWD_Q_CHOICES=(
    (u'father',u'父亲的生日？'),
    (u'mother',u'母亲的生日？'),
    (u'pet',u'宠物的名字？'),
    (u'hometown',u'出生地？'),
)

class Customer(models.Model):
	user=models.OneToOneField(User)
	idnum=models.CharField(max_length=18,verbose_name='身份证号码')
	pswd_q=models.CharField(max_length=32,verbose_name='密码提示问题',choices=PSWD_Q_CHOICES)
	pswd_a=models.CharField(max_length=16,verbose_name='密码提示答案')
	address=models.CharField(max_length=64,verbose_name='地址',blank=True)
	postcode=models.IntegerField(max_length=6,verbose_name='邮政编码',blank=True)
	phonenum=models.CharField(max_length=16,verbose_name='电话号码',blank=True)

	def save(self, *args, **kwargs):
		try:
			existing = Customer.objects.all().get(user=self.user)
			self.id = existing.id #force update instead of insert
		except Customer.DoesNotExist:
			pass
		models.Model.save(self, *args, **kwargs)

	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Customer.objects.create(user=instance)
	post_save.connect(create_user_profile, sender=User)
