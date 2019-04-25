from django.conf.urls import  url
from .import views
from django.contrib.auth import views as auth_views
urlpatterns=[
	url(r'^$',views.index,name="index"),
	url(r'^index/$',views.index,name="index"),
	url(r'^contact/$',views.contact,name="contact"),
	
	url(r'^create/$',views.create,name="create"),
	url(r'^blog/(?P<id>\d+)/(?P<slug>[\w-]+)/$',views.post_detail, name="post_detail"),

	
]
