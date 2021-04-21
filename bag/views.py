from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ This will show the shopping bag """

    return render(request, 'bag/bag.html')
