#coding=utf-8
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from cdealer.customer.forms import RegisterForm,LoginForm,ChangeForm,PswdForm

def register(request):
	if request.method=='POST':
		form=RegisterForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			user=User.objects.create_user(username=request.POST['username'],password=cd['password'],email=cd['email'])
			user.first_name=cd['first_name']
			user.last_name=cd['last_name']
			user.is_staff=False
			uf=user.get_profile()
			uf.idnum=cd['idnum']
			uf.address=cd['address']
			uf.postcode=cd['postcode']
			uf.phonenum=cd['phonenum']
			uf.pswd_q=cd['pswd_q']
			uf.pswd_a=cd['pswd_a']
			user.save()
			uf.save()
			return HttpResponseRedirect('/cdealer/index/')
	else:
		form=RegisterForm()

	return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))

def login(request):
	errors=[]
	if request.method=='POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			user=authenticate(username=request.POST['username'],password=request.POST['password'])
			if user is not None:
				if user.is_active:
					auth_login(request,user)
					return HttpResponseRedirect('/cdealer/index/')
			else:
				errors.append('用户名或者密码错误')
	else:
		form=LoginForm()
	return render_to_response('login.html',{'errors':errors,'form':form},context_instance=RequestContext(request))

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect('/cdealer/index/')

def change_profile(request):
	if request.user.is_authenticated():
		uf=request.user.get_profile()
		if request.method=="POST":
			form=ChangeForm(request.POST)
			if form.is_valid():
				u=User.objects.get(id=request.user.id)
				u.first_name=request.POST['first_name']
				u.last_name=request.POST['last_name']
				uf.phonenum=request.POST['phonenum']
				uf.postcode=request.POST['postcode']
				uf.address=request.POST['address']
				u.save()
				uf.save()
			return HttpResponseRedirect('/cdealer/index/')
		else:
			form=ChangeForm()

		return render_to_response("change_profile.html",{'form':form,'uf':uf},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/cdealer/index/')

def confirm_pswdQ(request):
	errors=[]
	if request.user.is_authenticated():
		if request.method=='POST':
			form=PswdQForm(request.POST)
			if form.is_valid():
				if(cmp(form.cleaned_data['pswd_a'],request.user.get_profile().pswd_a)==0):
					return HttpResponseRedirect('/cdealer/change_pswd/')
				else:
					errors.append(u'密码提示答案错误')
		else:
			form=PswdQForm(initial={'pswd_q':request.user.get_profile().pswd_q})
	else:
		return HttpResponseRedirect('/cdealer/index/')
	return render_to_response('confirm_pswdQ',{'form':form,'errors':errors},context_instance=RequestContext(request))

def change_pswd(request):
	error=''
	if request.user.is_authenticated():
		if request.method=='POST':
			form=PswdForm(request.POST)
			if form.is_valid():
				if not (request.user.check_password(form.cleaned_data['opswd'])):
					error=u'旧密码输入有误'
				else:
					request.user.set_password(form.cleaned_data['npswd'])
					request.user.save()
					return HttpResponseRedirect('/cdealer/index')
		else:
			form=PswdForm()
	else:
		return HttpResponseRedirect('/cdealer/index')
	return render_to_response('change_pswd.html',{'form':form,'error':error},context_instance=RequestContext(request))
				
			
