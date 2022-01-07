from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    re_path('add/profile/(?P<step>[1-6])/section/', views.add_profile, name='add-profile'),
    path('edit/profile/', views.edit_profile, name='edit-profile'),
]
