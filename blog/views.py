# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from .models import Post,Contact,Comment
#from django.forms import modelformset_factory
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect,Http404
from datetime import datetime
from django.urls import reverse
from django.core.exceptions import ValidationError
# Create your views here.
def index(request):
	post = Post.objects.all().order_by('-id')
	
	context = {
		'post':post,
		
		}	
	return render (request, 'blog/index.html',context)
	
def contact(request):
	if request.method == 'POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			contact=form.save(commit=False)
			contact.save()
			return redirect('index')
		
	else :
		form=ContactForm()
	p=Contact.objects.all()	
	context={
		'form':form,
		'p':p,
		}
	
	return render(request,'blog/contact.html',context)		


def create(request):
	if request.method == 'POST':
		form=CreateForm(request.POST, request.FILES)
		if form.is_valid():
			post=form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('index')
	else:
		form=CreateForm()		
	context={
		'form':form,
		}
	return render (request, 'blog/create.html',context)
	
def post_detail(request, id, slug ):
	post = Post.objects.get(id=id, slug=slug)
	comments = Comment.objects.filter(post=post).order_by('-id')
	if request.method == 'POST':
		comment_form=CommentForm(request.POST or None)
		if comment_form.is_valid():
			content = request.POST.get('content')
			comment = Comment.objects.create(post=post, user=request.user,content=content)
			comment.save()
			return HttpResponseRedirect(post.get_absolute_url())
			
	else:
		comment_form=CommentForm()
	context={
		'post':post,
		'comments':comments,
		'comment_form':comment_form,
		}
	return render(request,'blog/post_detail.html',context)	



	
	
	
def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect(reverse('index'))
				else:
					return HttpResponse("user is not active")
			else:
				return HttpResponse("User is none")
				
	else:
		form = UserLoginForm()

	context = {
		'form':form,
	}
	return render(request, 'blog/single.html', context)			
	
def user_logout(request):
	logout(request)
	return redirect('index')
	
	
#def register(request):
#	return render(request,'registration/register.html')
	
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user_login')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})	