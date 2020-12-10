from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .form import *


# Create your views here.


def index(request):
    context = {}
    return render(request, 'createBlog/index.html', context)


def blog(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'createBlog/addblog.html', context)


def post(request):
    post = Post.objects.order_by('-postdate')
    form = Postform()
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            form.save()
    context = {'post': post,
               'form': form}
    return render(request, 'createBlog/post.html', context)


def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post')
    context = {'item': post}
    return render(request, 'createBlog/delete_post.html', context)


def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = Postform(instance=post)
    if request.method == 'POST':
        form = Postform(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post')
    context = {'form': form}
    return render(request, 'createBlog/update_post.html', context)


def detail(request, pk):
    post = Post.objects.all()
    context = {'post': post}
    return render(request, 'createBlog/detail.html', context)


def category(request):
    category = Category.objects.all()
    form = Categoryform()
    if request.method == 'POST':
        form = Categoryform(request.POST)
        if form.is_valid():
            form.save()

    context = {'category': category,
               'form': form}
    return render(request, 'createBlog/category.html', context)


def delete_cat(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category')
    context = {'category': category}
    return render(request, 'createBlog/delete_cat.html', context)


def update_cat(request, pk):
    category = Category.objects.get(id=pk)
    form = Categoryform(instance=category)
    if request.method == 'POST':
        form = Categoryform(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    context = {'form': form}
    return render(request, 'createBlog/update_cat.html', context)


def contact(request):
    form = Contactform()
    if request.method == "POST":
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'A ticket is raised successfully')
            return redirect('contact')
    context = {'form':form}
    return render(request, 'createBlog/contact.html',context)

