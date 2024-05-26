from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from home.models import Film
from .models import Vote
from result.reco import recommend



class ResultView(generic.ListView):
    
    template_name = "result.html"
    context_object_name = "random_films"
    
    def get_queryset(self):
        film = self.kwargs['title']

        id_check = Film.objects.filter(french_title = film)[0].id

        list_id = recommend(id_check)

        return Film.objects.filter(id__in=list_id)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/about')

        return super().dispatch(request, *args, **kwargs)

def vote(request, film_id):
    film_id = film_id.split('?')[0]
    vote = Vote.objects.filter(id = film_id)[0]
    vote.vote_count += 1
    vote.save()
    
    return render(request,'home.html')
