from django import forms
from django.forms import ModelForm
from . import models

class UserForm(ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'
    password = forms.CharField(widget=forms.PasswordInput)

class TaskForm(ModelForm):
    class Meta:
        model = models.Task
        exclude = ['user']
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))