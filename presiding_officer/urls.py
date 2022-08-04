from django.urls import path
from . import views

urlpatterns = [
    path('add_student/', views.add_student),

    path('login', views.presiding_login, name = 'presiding_officer_login'),
    path('home',views.home, name='presiding_officer_home'),
    path('options', views.options, name = 'presiding_officer_options'),
    path('options/generate_otp', views.generate_otp, name = 'presiding_officer_generateOTP'),
    path('options/add_student', views.add_student, name = 'presiding_officer_addStudent'),
    path('show_student_list', views.see_student_list, name = 'presiding_officer_showList'),
    path('logout', views.presiding_logout, name = 'presiding_officer_logout')

]