#coding=utf-8
from django.db import models

# Create your models here.

class Link(models.Model):
	name=models.CharField(max_length=32,verbose_name=u'名称')
	url=models.URLField(verbose_name=u'地址')

	def __unicode__(self):
		return self.name
