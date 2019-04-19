# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display=('title','slug','author')
	search_fields=('author__username','title')
	prepopulated_fields={'slug':('title',)}
	date_hierarchy = ('created')
#class ImagesAdmin(admin.ModelAdmin):
#	list_display=('post','image')
admin.site.register(Post,PostAdmin)	
#admin.site.register(Images,ImagesAdmin)	