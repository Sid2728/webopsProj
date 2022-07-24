from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='Alcheringa_login'),
    path('home/',views.homepage,name='Alcheringa_home'),
    path('home/createpost/',views.createpage,name='Alcheringa_createpost'),
    path('home/mypost/', views.myposts, name='Alcheringa_myposts')
]