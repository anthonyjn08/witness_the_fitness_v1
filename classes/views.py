from django.shortcuts import render
from .models import Classes


def all_classes(request):

    classes = Classes.objects.all()

    context = {
        'classes': classes
    }

    return render(request, 'classes/classes.html', context)
