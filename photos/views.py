from django.shortcuts import render, get_object_or_404
from .models import Photo

# Create your views here.


def photos(request):
    """ A view to return all photos page including the user searching """

    photos = Photo.objects.all()
    print(photos)
    context = {
       'photos': photos,
    }

    return render(request, 'photos/photos.html', context)


def photos_detail(request, photo_id):
    """ A view to show certain photo informartion"""

    photos = get_object_or_404(Photo, pk=photo_id)

    context = {
       'photos': photos,
    }

    return render(request, 'photos/photos_detail.html', context)
