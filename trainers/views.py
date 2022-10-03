from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Trainers


class TrainerList(generic.ListView):
    model = Trainers
    queryset = Trainers.objects.all()
    template_name = 'trainers/trainers.html'
    paginate_by = 6


class TrainerDetail(View):
    """
    Recipe detail view to display full recipe when clicked on.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Trainers.objects.all()
        trainer = get_object_or_404(queryset, slug=slug)
        
        return render(
            request,
            "trainers/trainer_detail.html",
            {
                "trainer": trainer,
            },
        )
