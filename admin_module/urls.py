from django.urls import path
from . import views

urlpatterns = [
    path('add_election_posts', views.add_election_posts),
    path('add_candidate_list', views.add_candidate_list)
]