from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:profile_id>/', views.profile, name='profile'),
    path('add/profile/', views.add_new_profile, name='add-new-profile'),
    path('add/profile/<int:step>/section/<int:profile_id>/', views.add_profile, name='add-profile'),
    path('edit/profile/<int:profile_id>/', views.edit_profile, name='edit-profile'),
]
