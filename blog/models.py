# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
# Create your models here.
class Post(models.Model):
	title  = models.CharField(max_length=120)
	slug   = models.SlugField(max_length=120)
	body   = models.TextField()
	author = models.ForeignKey(User, related_name='blog_posts')
	created= models.DateTimeField(auto_now_add=True)
	updated= models.DateTimeField(auto_now=True)
	image = models.ImageField(upload_to='images/',blank=True, null=True)
	
	def __str__(self):
		return self.title
		
	#def get_absolute_url(self):
	#	return reverse("post_detail", args=[self.id , self.slug])

@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
	slug=slugify(kwargs['instance'].title)
	kwargs['instance'].slug=slug	
	
#class Images(models.Model):
#	post = models.ForeignKey(Post)
#	image = models.ImageField(upload_to='images/',blank=True, null=True)
	
#	def __str__(self):
#		return self.post.title + "__Image"