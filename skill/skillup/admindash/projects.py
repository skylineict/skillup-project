from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
import json
# from   .models import User,Profile, Faculty
# from user
# from .ots_email import send_otp
from django.contrib.auth import authenticate,login
# from .models import generate_otp
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
import pdb
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from user.models import Profile,Faculty,User, CourseList
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from django.conf import settings
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from cohorts.models import CohortGroup

class Projects(LoginRequiredMixin,UserPassesTestMixin,View):
     login_url = login

     
     def test_func(self):
        return self.request.user.is_staff
     
     def handle_no_permission(self):
         return redirect('login')
     
     
     def get(self,request):
                return render(request, 'admin/projects.html')
        
    
