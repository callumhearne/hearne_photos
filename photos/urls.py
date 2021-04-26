from django.urls import path
from . import views

urlpatterns = [
    path('', views.photos, name='photos'),
    path('photos_other/', views.photos_other, name='photos_other'),
    path('photos_ne/', views.photos_ne, name='photos_ne'),
    path('<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('add/', views.add_photo, name='add_photo'),
    path('edit/<int:photo_id>/', views.edit_photo, name='edit_photo'),
    path('delete/<int:photo_id>/', views.delete_photo, name='delete_photo'),


]
