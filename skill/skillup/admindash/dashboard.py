from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
# from   .models import User,Profile, Faculty
# from user
# from .ots_email import send_otp
from django.contrib.auth import authenticate,login
# from .models import generate_otp
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
import pdb
from django.urls import reverse
from user.models import Profile,Faculty
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.paginator  import Paginator,EmptyPage,PageNotAnInteger



class Dash(LoginRequiredMixin, UserPassesTestMixin,View):
    login_url = login

    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect('login')
    

    def get(self,request):
        return render(request, 'admin/dash.html')
    
    def post(self,request):
        return render(request, 'admin/dash.html')
    
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
        


def userprofile(request):
    pending_admitted = Profile.objects.filter(admitted=False,
        department__isnull=False,
        state__isnull=False,
        level__isnull=False,
        department__gt='',
        state__gt='',
        level__gt='').order_by('-date')
    paginator = Paginator(pending_admitted,3)
    page_numb = request.GET.get('page')
    profiles = paginator.get_page(page_numb)
   
    
    profiles_list =  list(profiles.object_list.values('id','department','image','date','user__full_name'))

    return JsonResponse({
       'profiles':profiles_list,
       'num_pages': paginator.num_pages,
       'current_page': profiles.number
    })





def approved_admission(request, id):
    admission_approved = Profile.objects.get(id=id)
    admission_approved.admitted=True
    admission_approved.save()
    subject ="Congratulations! Your Admission to Skill-Up RSU Has Been Approved"
    body = "Congratulations on being selected to join this impactful initiative. \n We believe that your participation will be a valuable  \n contribution to the program and offer you numerous \n opportunities for growth and development."
    email_from = settings.EMAIL_HOST_USER
    to_email = [admission_approved.user.email]
    email_sent = EmailMessage(subject=subject, from_email=email_from, body=body, to=to_email)
    email_sent.send(fail_silently=True)
    response_data = {
            'success': "Approved successfully",
            'profile_id': admission_approved.id
        }
    return JsonResponse(response_data)
   









    
