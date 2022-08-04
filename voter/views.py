from django.shortcuts import render, redirect

from django.http import HttpResponse
from admin_module.models import student_detail
# Create your views here.

from presiding_officer.views import otp_from_presiding_officer
from presiding_officer.views import change_otp    #here to generate new otp after verification to
                                                   #avoid entering with same otp again

from admin_module.models import election_posts, candidate  
from .models             import votes              #to update votes

from django.contrib import messages


adm_no = ''      #making it global variable to swap b/w functions




#function for voter to login using OTP and admission number
def voter_login(request):

    if request.method == 'POST':
        global adm_no
        adm_no = request.POST['adm_no']

        OTP = otp_from_presiding_officer()
        print('OTP from preciding officer module: ', OTP) #to understand data flow in terminal
        print('OTP from voter: ', request.POST['otp'])    #to understand data flow in terminal

        if OTP == request.POST['otp']:                    #checking entered OTP and produced OTP
            change_otp()
            if student_detail.objects.filter(adm_no = adm_no).exists():  #to check if person with entered adm no exits
                pass
            else:
                 context = {}
                 context['signin_status'] = False
                 return render(request, 'voter/login.html', context)
            
            request.session['adm_no'] = request.POST['adm_no']
            return render(request, 'voter/instructions.html', {'adm_no': adm_no})
            

        else:
            context = {}
            context['signin_status'] = False
            return render(request, 'voter/login.html', context)

    else:
        return render(request, 'voter/login.html')


#function to confirm details with the student/voter itself
#the student details shown with the adm no entered during login
def confirm_details(request):
    
    student = student_detail.objects.all().filter(adm_no = adm_no)[0]
    print(student)

    context = {}
    context['student'] = student    
    return render(request, 'voter/confirm_details.html', context)


#to check for available posts that a particular student can vote
#NOTE: For this prototype, only 7 posts considered
#      Can add more posts whenever required
def voter_criteria(department, year, gender, degree):

    chairperson         = 101
    vice_chairperson    = 102
    cs_rep              = 103
    bt_rep              = 104
    first_year_rep      = 105
    lady_rep            = 106
    first_year_cs_rep   = 107

    print('---------------INSIDE VOTER CRITERIA-------------')
    print('Department: ', department)
    print('Year:', year)
    print('Gender: ', gender)
    print('Degree: ', degree)
   
    eligible_posts = set(())         #class set to not enter a post twice
    eligible_posts.add(chairperson)       #since everyone is allowed to vote for this post
    eligible_posts.add(vice_chairperson)  #same as chairperson

    if department == 'CSE':               #cs rep
        eligible_posts.add(cs_rep)

        if year == 1:                     #first year cs rep
            eligible_posts.add(first_year_cs_rep)
    
    if department == 'BT':                #bt rep
        eligible_posts.add(bt_rep)

    if year == 1:                         #first year rep
        eligible_posts.add(first_year_rep)
    
    if gender == 'F':                     #lady rep
        eligible_posts.add(lady_rep)

    if department == 'CSE' and year == 1: #first year cs rep
        eligible_posts.add(first_year_cs_rep)

    print(eligible_posts)
    return eligible_posts




#All logic and functions related to showing the eligble posts in frontend 
#and to get the votes of corresponding candidates
#and update the votes number in the database
def vote(request):

    student = student_detail.objects.all().filter(adm_no = adm_no)[0]
    print(student.name)
    print(student.department)
    print(student.gender)
    print(student.year)
    print(student.degree)

    can_vote = voter_criteria(student.department, student.year, student.gender, student.degree)
    print('Eligible vote categories',can_vote)

    if request.method == 'POST':

        for post_id in can_vote:

            person_to_vote = str(request.POST[str(post_id)])
            print('For post', post_id, 'Response: ', person_to_vote) #to print in terminal

            curr_post = votes.objects.all().filter(position_id = post_id)[0]
            
            #NOTE: person_to_vote contains 2 chars, not just a number so to get the number only ,below code           
            if person_to_vote[0] == '1':
                print('this is 1')
                curr_post.candidate1 = curr_post.candidate1 + 1
            elif person_to_vote[0] == '2':
                print('this is 2')
                curr_post.candidate2 = curr_post.candidate2 + 1
            else:
                print('this is 3')
                curr_post.candidate3 = curr_post.candidate3 + 1

            #incrementing total votes
            curr_post.total_votes = curr_post.total_votes + 1

            curr_post.save()
        
        print('Votes successfully registered...')

        messages.info(request, ('Voted Successfully...'))
        return redirect('voter_login')

    posts = {}

    '''
    ------------BASIC FORMAT OF CONTEXT TO BE PASSED TO TEMPLATE (for reference)--------------

    context ={
        posts = {
            '101' : {
                'candidates': {candidate list},
                'post_name' : position name of 101, eg, Chairperson, Vice Chairperson, etc
            },
            '102' : {
                'candidates' : {candidate list},
                'post_name' : position name of 102
            }

        }
    }
    ------------------------------------------------------------------------------------------
    '''
    for post in can_vote:
        curr_post = election_posts.objects.all().filter(post_id = post)[0] #to get the post name
        curr_post_cand = candidate.objects.all().filter(position_id = post) #to get candidates for this post
        
        posts[str(post)] = {
            'candidates' : curr_post_cand,
            'post_name'  : curr_post.position_name
        }
    print(posts)

    print('------INSIDE FOR LOOP TO DISPLAY CONTEXT-----')

    for post in posts:
        print('POST: ', post)

        for cand in posts[post]['candidates']:
            print(cand)
        print(posts[post]['post_name'])
        
            
    context = {}
    context['posts'] = posts
   
    
    return render(request, 'voter/vote.html', context)




