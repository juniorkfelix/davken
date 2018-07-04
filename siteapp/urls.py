from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
	url(r'^$', views.index , name="index"),
	url(r'^index', views.index),
	url(r'^about$', views.about, name="about"),
	url(r'^categories$', views.categories, name="categories"),
	url(r'^contact$', views.contact, name="contact"),
	url(r'^login/$', login, {'template_name': 'login.html'})

]