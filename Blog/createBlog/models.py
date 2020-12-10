from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Category(models.Model):
    objects = None
    title = models.CharField(max_length=650)
    description = models.CharField(max_length=500)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS = (
        ('PUBLISHED', 'PUBLISHED'),
        ('DRAFT', 'DRAFT'),
    )
    title = models.CharField(max_length=500, null=True)
    body = models.CharField(max_length=1000, null=True)
    postdate = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=50, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100,choices=STATUS,default='DRAFT')
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class contact(models.Model):
    firstname = models.CharField(max_length=30,null=True)
    lastname = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=20,null=True)
    address = models.TextField(max_length=50,null=True)
    description = models.TextField(max_length=256,null=True)

    def __str__(self):
        return self.firstname
