from django.urls import path
from . import views

urlpatterns = [
    path('', views.photos, name='photos'),
    path('<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('add/', views.add_photo, name='add_photo'),
    path('edit/<int:photo_id>/', views.edit_photo, name='edit_photo'),


]
