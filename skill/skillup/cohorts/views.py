from django.shortcuts import render

# Create your views here.
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
from user.models import Profile,Faculty,User 
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.paginator  import Paginator,EmptyPage,PageNotAnInteger
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from user .passcodegen import generate_passcode
from .models import CohortGroup




class ListAdminCohort(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = login
    def test_func(self):
        return self.request.user.is_staff 
    def handle_no_permission(self):
         return redirect('login')
    
    def get(self,request):
                pdb.set_trace
                cohort_list = CohortGroup.objects.count()
                context = {
                       'cohort_list':cohort_list
                }
                return render(request, 'admin/cohortlist.html', context=context)
    
    def post(self,request):
                return render(request, 'admin/cohortlist.html')



class CreateCohort(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = login
    def test_func(self):
        return self.request.user.is_staff 
    def handle_no_permission(self):
         return redirect('login')
    
    def post(self, request):
        name = request.POST.get('name')
        whatsapp = request.POST.get('url') 
       
        if not name:
            return JsonResponse({'error': 'Cohort name is required'}, status=400)
        if not whatsapp:
            return JsonResponse({'error': 'Cohort whatsapplink is required'}, status=400)
        
        if CohortGroup.objects.filter(name=name).exists():
               return JsonResponse({'error': 'Cohort name already exist, try gain'}, status=400)
        
        if CohortGroup.objects.filter(whatsapp=whatsapp).exists():
               return JsonResponse({'error': 'whatsapp group link  already exist, try gain'}, status=400)
              

        # Create a new cohort group
        cohort = CohortGroup.objects.create(name=name, whatsapp=whatsapp)
        return JsonResponse({'success': 'Cohort created successfully'}, status=201)
                
        
class CohortList(LoginRequiredMixin,UserPassesTestMixin,View):
     login_url = login

     
     def test_func(self):
        return self.request.user.is_staff
     def handle_no_permission(self):
         return redirect('login')
      
     def get(self, request):
           
           cohorts = CohortGroup.objects.all()
        
           cohort_list = []
           for cohort in cohorts:
                 profiles = list(cohort.users.values(
                       'id',
                       'profiles__image',
                       'email',
                       'full_name' ))   
                      
                 cohort_data = {
                      'id': cohort.id,
                      'name': cohort.name,
                      'whatsapp': cohort.whatsapp,
                     'members': profiles}
                 cohort_list.append(cohort_data)
           return JsonResponse({'cohort_list':cohort_list})

            
                
            
 
    
def DeleteCohortList(request, cohort_id):
    try:
        cohorts = CohortGroup.objects.get(pk=cohort_id)
        cohorts.delete()
        response_data = {
                'success': "Cohort deleted successfully"
            }
    except CohortGroup.DoesNotExist:
            response_data = {
                'error': "Cohort not found"
            }
            return JsonResponse(response_data, status=404)

    return JsonResponse(response_data)

                 



           
          
       

