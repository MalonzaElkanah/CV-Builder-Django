from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('profile/<int:profile_id>/', views.profile, name='profile'),
    path('add/profile/', views.add_new_profile, name='add-new-profile'),
    path('add/profile/<int:step>/section/<int:profile_id>/', views.add_profile, name='add-profile'),
    path('edit/profile/<int:profile_id>/', views.edit_profile, name='edit-profile'),
    path('pick/cv/<int:profile_id>/', views.pick_cv, name='pick-cv'),

    path('add/cv/', views.add_cv, name='add-cv'),
    path('edit/cv/<int:cv_id>/', views.edit_cv, name='edit-cv'),
    path('preview/cv/<int:cv_id>/profile/<int:profile_id>/', views.preview_cv, name='preview-cv'),
    path('view/cv/<int:cv_id>/', views.cv_view, name='view-cv'),
    path('cv/iframe/view/<int:cv_id>/profile/<int:profile_id>/', views.cv_iframe_view, name = 'cv-iframe-view'),
    path('cv/file/view/<int:cv_id>/profile/<int:profile_id>/', views.generate_cv_pdf, name = 'cv-file-view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
