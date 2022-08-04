from django.urls import path
from . import views

urlpatterns = [
    path('', views.voter_login, name = 'voter_login'),
    path('confirm_details',views.confirm_details, name = 'voter_confirm_details'),
    path('vote', views.vote, name = 'voter_vote')
    
]