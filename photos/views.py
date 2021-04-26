from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

def photos_other(request):
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

    return render(request, 'photos/photos_other.html', context)


def photos_ne(request):
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

    return render(request, 'photos/photos_ne.html', context)



def photo_detail(request, photo_id):
    """ A view to show certain photo information"""

    photo = get_object_or_404(Photo, pk=photo_id)

    context = {
       'photo': photo,
    }

    return render(request, 'photos/photo_detail.html', context)


@login_required
def add_photo(request):
    """ Add a photo to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            form.save()
            messages.success(request, 'Successfully added photo!')
            return redirect(reverse('photo_detail', args=[photo.id]))
        else:
            messages.error(request, 'Failed to add photo. Please ensure the form is valid.')
    else:
        form = PhotoForm()
       
    template = 'photos/add_photo.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_photo(request, photo_id):
    """ Edit a photo in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    photo = get_object_or_404(Photo, pk=photo_id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated photo!')
            return redirect(reverse('photo_detail', args=[photo.id]))
        else:
            messages.error(request, 'Failed to update photo. Please ensure the form is valid.')
    else:
        form = PhotoForm(instance=photo)
        messages.info(request, f'You are editing {photo.Location}')

    template = 'photos/edit_photo.html'
    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, template, context)


@login_required
def delete_photo(request, photo_id):
    """ Delete a photo from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
       
    photo = get_object_or_404(Photo, pk=photo_id)
    photo.delete()
    messages.success(request, 'Photo deleted!')
    return redirect(reverse('photos'))
