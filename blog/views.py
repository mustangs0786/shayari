# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Post
#from django.forms import modelformset_factory
from .forms import CreateForm
# Create your views here.
def index(request):
	post = Post.objects.all().order_by('-id')
	
	context = {
		'post':post,
		}	
	return render (request, 'blog/index.html',context)
	
def contact(request):
	return render (request, 'blog/contact.html')	


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
	post = Post.objects.get(id=id)
	context={
		'post':post,
		}
	return render(request,'blog/post_detail.html',context)	
