from django.shortcuts import render
from django.http import HttpResponse

import admin_module
# Create your views here.

from .models import election_posts, candidate

import pandas as pd

def add_candidate_list(request):

    if request.method == 'POST':
        file = request.FILES['candidate_list']
        curr_cand_list = pd.read_csv(file)
       
        for x in reversed(curr_cand_list.index):
            print(curr_cand_list['first_name'][x], curr_cand_list['last_name'][x])
            cand = candidate(
                first_name = curr_cand_list['first_name'][x],
                last_name  = curr_cand_list['last_name'][x],
                adm_no     = curr_cand_list['adm_no'][x],
                apply_position = curr_cand_list['apply_position'][x],
                position_id = curr_cand_list['position_id'][x],
                candidate_id  = curr_cand_list['candidate_id'][x]
            )

            cand.save()

        return HttpResponse('<script>alert("Candidate List Successfully Saved...")</script>')
    else:
        return render(request, 'admin_module/add_candidates.html') 

def add_election_posts(request):

    if request.method == 'POST':
        file = request.FILES['election_post_list']
        curr_post_list = pd.read_csv(file)
        
        for x in reversed(curr_post_list.index):
            print(curr_post_list['position_name'][x], curr_post_list['post_id'][x])
            post = election_posts(
                post_id       = curr_post_list['post_id'][x],
                position_name = curr_post_list['position_name'][x],
                depts         = curr_post_list['depts'][x],
                gender        = curr_post_list['gender'][x],
                year          = curr_post_list['year'][x],
                degree        = curr_post_list['degree'][x]
            )

            post.save()
   
        return HttpResponse('<script>alert("Candidate List Successfully Saved...")</script>')
    else:
        return render(request, 'admin_module/add_election_posts.html') 

