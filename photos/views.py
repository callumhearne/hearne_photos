from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Photo
from .forms import PhotoForm

# Create your views here.


def photos(request):
    """ A view to return all photos page including the user searching """

    photos = Photo.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                photos = photos.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            photos = photos.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('photos'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            photos = photos.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
       'photos': photos,
       'search_term': query,
       'current_sorting': current_sorting,

    }

    return render(request, 'photos/photos.html', context)


def photo_detail(request, photo_id):
    """ A view to show certain photo information"""

    photo = get_object_or_404(Photo, pk=photo_id)

    context = {
       'photo': photo,
    }

    return render(request, 'photos/photo_detail.html', context)


def add_photo(request):
    """ Add a photo to the store """
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added photo!')
            return redirect(reverse('add_photo'))
        else:
            messages.error(request, 'Failed to add photo. Please ensure the form is valid.')
    else:
        form = PhotoForm()
        
    template = 'photos/add_photo.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
