# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post,Contact,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display=('title','slug','author')
	search_fields=('author__username','title')
	prepopulated_fields={'slug':('title',)}
	date_hierarchy = ('created')

admin.site.register(Post,PostAdmin)	

class ContactAdmin(admin.ModelAdmin):
	list_display=('Name','Email')
	
admin.site.register(Contact,ContactAdmin)	
admin.site.register(Comment)	

	
	