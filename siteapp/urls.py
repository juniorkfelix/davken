from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index , name="index"),
	url(r'^index', views.index),
	url(r'^about$', views.about, name="about"),
	url(r'^categories$', views.categories, name="categories"),
	url(r'^contact$', views.contact, name="contact"),
	url(r'^form$', views.get_name, name="form"),

]