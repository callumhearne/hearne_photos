from django.contrib import admin
from .models import Photos, models
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


admin.site.register(Photos)
