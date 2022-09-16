from tkinter import Widget
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from hello.models import LogMessage
from hello.models import Application

#This form is so that tickets can be raised by the user
class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("assign","email","subject","applicationname","message","severity",)  # NOTE: the trailing comma is required

#This form is so that applications can be raised by the user
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("applicationname","contactemail","description",)  # NOTE: the trailing comma is required

#This form is so that users can be created by the user
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user