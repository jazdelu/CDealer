#coding=utf-8
from django.db import models
from cdealer.category.models import Category
from cdealer.artist.models import Artist
from thumbs import ImageWithThumbsField
# Create your models here.

ISPROMOTION_CHOICES=(
    (u'y',u'是'),
    (u'n',u'否'),
)

class Album(models.Model):
    cover=ImageWithThumbsField(upload_to='cover',verbose_name=u'专辑封面', sizes=((50,50),(100,100),(300,300),))
    name=models.CharField(max_length=32,verbose_name=u'名字')
    category=models.ManyToManyField(Category,verbose_name=u'风格',related_name='entries')
    artist=models.ForeignKey(Artist,null=True,on_delete=models.SET_NULL,verbose_name=u'艺人')
    release_date=models.DateField(verbose_name=u'发行日期')
    intro=models.TextField(verbose_name=u'专辑简介')
    stock=models.IntegerField(verbose_name=u'库存量',max_length=4)
    price=models.IntegerField(verbose_name=u'价格',max_length=4)
    ispromotion=models.CharField(verbose_name=u'是否促销',max_length=2,choices=ISPROMOTION_CHOICES,default='n')

    def __unicode__(self):
        return self.name
    
