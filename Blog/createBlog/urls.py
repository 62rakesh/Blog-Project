from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blog/',views.blog,name='blog'),
    path('post/',views.post,name='post'),
    path('delete_post/<str:pk>/',views.delete_post,name='delete_post'),
    path('update_post/<str:pk>/',views.update_post,name='update_post'),
    path('detail/<str:pk>/',views.detail,name='detail'),
    path('category/',views.category,name='category'),
    path('delete_cat/<str:pk>/',views.delete_cat,name='delete_cat'),
    path('update_cat/<str:pk>/',views.update_cat,name='update_cat'),
    path('contact/',views.contact,name='contact'),
]