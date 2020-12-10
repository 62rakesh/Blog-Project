from django import forms
from django.forms import ModelForm
from .models import *


class Postform(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['slug']


class Categoryform(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        exclude = ['slug']


class Contactform(ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
