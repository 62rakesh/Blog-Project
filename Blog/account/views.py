from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .form import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html', {'form': Registerform})
    else:
        if request.POST['password'] == request.POST['confirmpassword']:
            try:
                user = User.objects.create_user(request.POST['firstname'], email=request.POST['Emailid'],
                                                password=request.POST['password'])
                user.save()
                login(request, user)
                messages.info(request, 'New account is created')
                return redirect('dashboard')
            except IntegrityError:
                return render(request, 'account/register.html',
                              {'form': Registerform, 'error': 'The user name is already '
                                                              'exist'})
        else:
            return render(request, 'account/register.html', {'form': Registerform, 'error': 'Password did not match'})


def loginuser(request):
    return render(request, 'account/login.html')



