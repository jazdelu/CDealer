#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from cdealer.customer.models import Customer
import datetime

PSWD_Q_CHOICES=(
    (u'father',u'父亲的生日？'),
    (u'mother',u'母亲的生日？'),
    (u'pet',u'宠物的名字？'),
    (u'hometown',u'出生地？'),
)

class RegisterForm(forms.Form):

	username=forms.CharField(max_length=16,min_length=6,label=u'用户名')
	password=forms.CharField(max_length=16,min_length=8,widget=forms.PasswordInput(),label=u'密码')
	cpassword=forms.CharField(max_length=16,min_length=8,widget=forms.PasswordInput(),label=u'确认密码')
	email=forms.EmailField(label=u'电子邮件')
	idnum=forms.CharField(max_length=18,label=u'身份证号码')
	pswd_q=forms.ChoiceField(choices=PSWD_Q_CHOICES,label=u'密码提示问题')
	pswd_a=forms.CharField(max_length=8,label=u'密码提示答案')
	first_name=forms.CharField(max_length=8,label=u'姓',required=False)
	last_name=forms.CharField(max_length=16,label=u'名',required=False)
	phonenum=forms.CharField(max_length=16,label=u'电话号码',required=False)
	postcode=forms.IntegerField(label=u'邮政编码',required=False)
	address=forms.CharField(label=u'地址',required=False,widget=forms.Textarea)


	def clean_cpassword(self):
		password=self.cleaned_data['password']
		cpassword=self.cleaned_data['cpassword']
		if(cmp(password,cpassword)!=0):
			raise forms.ValidationError(u'两次输入的密码不一致')
		return cpassword
	
	def clean_username(self):
		un=self.cleaned_data['username']
		try:
			u=User.objects.get(username=un)
		except(User.DoesNotExist):
			pass
		else:
			raise forms.ValidationError(u'用户名已存在')
			return username

class LoginForm(forms.Form):
	username=forms.CharField(max_length=16,min_length=6,label=u'用户名')
	password=forms.CharField(max_length=16,min_length=8,widget=forms.PasswordInput(),label=u'密码')
	isremember=forms.BooleanField(required=False,label=u'记住密码')

class ChangeForm(forms.Form):
	username=forms.CharField(max_length=16,min_length=6,label=u'用户名',widget=forms.TextInput(attrs={'readonly':'readonly'}))
	first_name=forms.CharField(max_length=8,label=u'姓',required=False)
	last_name=forms.CharField(max_length=16,label=u'名',required=False)
	phonenum=forms.CharField(max_length=16,label=u'电话号码',required=False)
	postcode=forms.IntegerField(label=u'邮政编码',required=False)
	address=forms.CharField(label=u'地址',required=False,widget=forms.Textarea)

class PswdQForm(forms.Form):
	pswd_q=forms.ChoiceField(choices=PSWD_Q_CHOICES,label=u'密码提示问题')
	pswd_a=forms.CharField(max_length=8,label=u'密码提示答案')

class PswdForm(forms.Form):
	opswd=forms.CharField(max_length=16,min_length=8,widget=forms.PasswordInput(),label=u'旧密码')
	npswd=forms.CharField(max_length=16,min_length=8,widget=forms.PasswordInput(),label=u'新密码')
	cpswd=forms.CharField(max_length=16,min_length=8,widget=forms.PasswordInput(),label=u'确认新密码')

	def clean_cpswd(self):
		npswd=self.cleaned_data['npswd']
		cpswd=self.cleaned_data['cpswd']
		if(cmp(npswd,cpswd)!=0):
			raise forms.ValidationError(u'两次输入的密码不一致')
		return cpswd
	
    
