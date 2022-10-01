from django.shortcuts import render


def index(request):
    """ View thats returns index page """
    return render(request, 'home/index.html')

