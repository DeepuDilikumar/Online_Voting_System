from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
from admin_module.models import student_detail

import pandas as pd
def add_student(request):
    if request.method == 'POST':
        file = request.FILES['student_list']
        curr_student_list = pd.read_csv(file)
       
        for x in reversed(curr_student_list.index):
            print(curr_student_list['name'][x], curr_student_list['roll_no'][x])
            student = student_detail(
                name = curr_student_list['name'][x],
                roll_no = curr_student_list['roll_no'][x],
                adm_no  = curr_student_list['admission_no'][x],
                department = curr_student_list['department'][x],
                year = curr_student_list['year'][x],
                gender = curr_student_list['gender'][x],
                degree = curr_student_list['degree'][x],
                phone_no = curr_student_list['phone_no'][x],

                
            )

            student.save()

        return HttpResponse('<script>alert("Student List Successfully Uploaded...")</script>')

def presiding_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is not None:
           #return HttpResponse("user is authenticated")
           login(request, user)
           request.session['username'] = username
           request.session['employee_id'] = request.POST['employee_id']

           return redirect('presiding_officer_home')
        else:
            messages.info(request, ('Invalid Email ID or Employee ID or Password!!!'))
            return redirect('presiding_officer_login')
               
    else:
        return render(request, 'presiding_officer/login.html')

def home(request):
    return render(request, 'presiding_officer/home.html')

def options(request):
    return render(request, 'presiding_officer/options.html')

import math
import random
#from voter.views import OTP as otp

OTP = ''


#for security purposes to change otp value after first verification in voter module
def change_otp(): 
    digits = "0123456789"
    global OTP   #to make the OTP variable global

    OTP = ''

    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]


def otp_from_presiding_officer(): #for sending the otp to voter module for verificiation
    return OTP

def generate_otp(request):
   
    digits = "0123456789"

    global OTP   #to make the OTP variable global
    OTP = ''

    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]

    print('OTP IS: ',OTP)

    context = {}
    context['generate_OTP'] = True
    context['OTP'] = OTP

    otp = str(OTP)

    #return HttpResponse('<script>window.alert("The newly generated OTP: ", otp)</script>')
    return render(request, 'presiding_officer/generateOTP.html', {'otp' : otp})

#to add student list
import pandas as pd #for reading csv files

def add_student(request):
    if request.method == 'POST':
        file = request.FILES['student_list']
        curr_student_list = pd.read_csv(file)
       
        for x in reversed(curr_student_list.index):
            print(curr_student_list['name'][x], curr_student_list['roll_no'][x])
            student = student_detail(
                name = curr_student_list['name'][x],
                roll_no = curr_student_list['roll_no'][x],
                adm_no  = curr_student_list['admission_no'][x],
                department = curr_student_list['department'][x],
                year = curr_student_list['year'][x],
                gender = curr_student_list['gender'][x],
                degree = curr_student_list['degree'][x],
                phone_no = curr_student_list['phone_no'][x],
                
                staff_adv_username = request.session['username']

            )

            student.save()

        context = {}
        context['list_uploaded'] = True

        messages.info(request, ('Student List Uploaded successfully...'))
        return redirect('presiding_officer_options')

    else:
        return render(request, 'presiding_officer/add_student.html')

def presiding_logout(request):
    logout(request)
    return redirect('presiding_officer_login')


def see_student_list(request):
    
    curr_student_list = student_detail.objects.filter(staff_adv_username = request.session['username'])
    for x in curr_student_list:
        print(x)

    context = {}
    context['student_list'] = curr_student_list

    return render(request, 'presiding_officer/show_students.html', context)
