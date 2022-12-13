class TrainerList(generic.ListView):
    """
    A view to show all trainers.
    """
    model = Sponsors
    queryset = Sponsors.objects.all().order_by('sponsor_name')
    template_name = 'sponsors/sponsors.html'
    paginate_by = 6