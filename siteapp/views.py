# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from . forms import LoginForm
from django.http import HttpResponse


# Create your views here.
def index(request):
	
	return render(request, 'index.html' )

def about(request):
	return render(request, 'about.html')

def categories(request):
	return render(request, 'categories.html')

def contact(request):
	return render(request, 'contact.html')

