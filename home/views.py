from django.shortcuts import render

# Create your views here.


def index(request):
    """ A command to return the home page """

    return render(request, 'home/index.html')


def faq(request):
    """ A command to return the home page """

    return render(request, 'home/faq.html')


def policy(request):
    """ A command to return the home page """

    return render(request, 'home/policy.html')
