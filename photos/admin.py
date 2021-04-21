from django.contrib import admin
from .models import Photo, models

# Register your models here.

class PhotosAdmin(models.Model):
    list_display = (
        'Location',
        'desc',
        'price',
        'img',
        'NE',
    )

    orderding = ('Location,')


admin.site.register(Photo)
