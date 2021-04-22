from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ij8LaFirrQj3BipLCjAHJOSZnZiPxb80FtLASJxEmTmYrrOuRLZMe33ga1Nn6xVvgv5lWiKt5bdIFmLjxwTLG2d009tfajgGU'
        
    }

    return render(request, template, context)
