from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from photos.models import Photo


def bag_contents(request):

    bag_items = []
    total = 0
    photo_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            photo = get_object_or_404(Photo, pk=item_id)
            total += item_data * photo.price
            photo_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'photo': photo,
            })
        else:
            photo = get_object_or_404(Photo, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * photo.price
                photo_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'photo': photo,
                    'size': size,
                })

    """ This will work out the delievery depending on how much is in the bag """
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'ohoto_count': photo_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
