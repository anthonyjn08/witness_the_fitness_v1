from django.shortcuts import render, get_object_or_404
from .models import Classes


def all_classes(request):

    classes = Classes.objects.all()

    context = {
        'classes': classes
    }

    return render(request, 'classes/classes.html/', context)

