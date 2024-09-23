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
from projects.models import TaskSubmission, UserProjectStatus, Student_Project
from cohorts.models import CohortGroup


class Add_Projectview(LoginRequiredMixin, UserPassesTestMixin,View):
    login_url = login

    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect('login')
    

    def get(self,request):
         cohorts = CohortGroup.objects.all()
         return render(request, 'admin/add_project.html', {'cohorts': cohorts})
       
       

    
    def post(self,request):
        project_name = request.POST.get('project_name')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        task_required_score = request.POST.get('score')
        cohort_ids = request.POST.getlist('cohorts')  # Multiple cohorts
        print("your cohort is", cohort_ids)
        if not project_name or not start_date or not description or not end_date or not task_required_score:
            return JsonResponse({'error': 'Please fill out all required fields.'}, status=400)
        
        project = Student_Project.objects.create(
            project_name=project_name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            task_required_score=task_required_score,
            user=request.user  
        )

          # Assign cohorts to the project
        for cohort_id in cohort_ids:
            cohort = CohortGroup.objects.get(id=cohort_id)
            project.cohort.add(cohort)
            for user in cohort.users.all():
                print(user)

                # Create a UserProjectStatus instance with default 'pending' status for each user
                UserProjectStatus.objects.create(
                    status='pending',
                    user=user,  # Each user in the cohort
                    projects=project)
                
        return JsonResponse({'success': 'Project created and assigned to cohorts successfully.'},status=200)
        # render(request, 'admin/add_project.html')