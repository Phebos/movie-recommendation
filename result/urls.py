from django.urls import path
from . import views

urlpatterns = [
    path("vote/<str:film_id>", views.vote, name="vote"),
    path('<str:title>', views.ResultView.as_view(), name='result'),
]