from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from photos.models import Photo

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified photo to the shopping bag """

    photo = get_object_or_404(Photo, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'photo_size' in request.POST:
        size = request.POST['photo_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 f'Updated size {size.upper()} +'
                                 f'{photo.Location} quantity to +'
                                 f'{bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 f'Added size {size.upper()} +'
                                 f'{photo.Location} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             f'Added size {size.upper()} +'
                             f'{photo.Location} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request,
                             f'Updated {photo.Location} +'
                             f'quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request,
                             f'Added {photo.Location} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified photo to the specified amount"""

    photo = get_object_or_404(Photo, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'photo_size' in request.POST:
        size = request.POST['photo_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             f'Updated size {size.upper()} +'
                             f'{photo.Location} quantity to +'
                             f'{bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(request,
                                 f'Removed size {size.upper()} +'
                                 f' {photo.Location} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request,
                             f'Updated {photo.Location} +'
                             f' quantity to {bag[item_id]}')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the photo from the shopping bag"""

    try:
        photo = get_object_or_404(Photo, pk=item_id)
        size = None
        if 'photo_size' in request.POST:
            size = request.POST['photo_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request,
                             f'Removed size {size.upper()} +'
                             f' {photo.Location} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
