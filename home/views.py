from django.shortcuts import render

# Create your views here.


def index(request):
    """ A command to return the home page """

    return render(request, 'home/index.html')
