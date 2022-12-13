from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Sponsors


class SponsorList(generic.ListView):
    """
    A view to show all sponsors.
    """
    model = Sponsors
    queryset = Sponsors.objects.all().order_by('sponsor_name')
    template_name = 'sponsors/sponsors.html'
    paginate_by = 6
