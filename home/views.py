from django.shortcuts import render


def index(request):
    """ View thats returns home page """
    return render(request, 'home/index.html')

