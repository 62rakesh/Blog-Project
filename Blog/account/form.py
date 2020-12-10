from .models import *
from django import forms
from django.forms import ModelForm


class Registerform(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
