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


class CohortList(LoginRequiredMixin,View):
    login_url= 'login'
    def get(self,request):
        return render(request, 'dash/cohorts.html')
    
    def post(self,request):
        return render(request, 'dash/cohorts.html')
    
