from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
# from   .models import User,Profile, Faculty
# from user
# from .ots_email import send_otp
from django.contrib.auth import authenticate,login
# from .models import generate_otp
from django.contrib.auth.mixins import LoginRequiredMixin
import pdb
from django.urls import reverse
from user.models import Profile,Faculty



class Dash(LoginRequiredMixin,View):
    login_url= 'login'
    def get(self,request):
        return render(request, 'dash/dash.html')
    
    def post(self,request):
        return render(request, 'dash/dash.html')
    
def studentchart(request):
    faculties = Faculty.objects.all()
    faculty_data = []

    for faculty in faculties:
        total_students = faculty.faculties.count()
        admitted_students = faculty.faculties.filter(admitted=True).count()
        faculty_data.append({
        'faculty_name': faculty.name,
        'total_students': total_students,
        'admitted_students': admitted_students,
        
        })
        
    
    
        data = {
        'faculty_data': faculty_data,
    }
        
    return JsonResponse({'data': data},safe=False)
        
