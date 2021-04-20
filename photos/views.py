from django.shortcuts import render
from .models import Photos

# Create your views here.


def all_photos(request):
    """ A view to return all photos page including the user searching """

    Photos = Photos.objects.all()

    context = {
       'Photos': Photos,
    }

    return render(request, 'photos/all_photos.html', context)
