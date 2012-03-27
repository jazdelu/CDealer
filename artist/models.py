#coding=utf-8
from django.db import models
from cdealer.category.models import Category

# Create your models here.

class Artist(models.Model):
    photo=models.ImageField(upload_to='artist',verbose_name=u'艺人照片')
    name=models.CharField(max_length=32,verbose_name=u'艺人姓名')
    category=models.ManyToManyField(Category,verbose_name=u'风格')
    website=models.URLField(verbose_name=u'个人主页',blank=True)
    intro=models.TextField(verbose_name=u'艺人简介',blank=True)
    def __unicode__(self):
        return self.name
   
    
