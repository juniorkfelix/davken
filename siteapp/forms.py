from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	class meta:
		model = User
		fields = ('username', 'password')
