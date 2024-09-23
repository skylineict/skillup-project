from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Student_Project,UserProjectStatus
from django.shortcuts import get_object_or_404
import pdb
from django.utils import timezone

# Create your views here.
class ProjectDatials(LoginRequiredMixin,View):
    login_url= 'login'
    def get(self,request,project_id):
         
         
        project = get_object_or_404(Student_Project, project_id=project_id,
                                     cohort__in=request.user.cohorts.all() )
        user_project_status, created = UserProjectStatus.objects.get_or_create(user=request.user, projects=project)
        if project.end_date <= timezone.now():
          user_project_status.status = 'complete'
        
        else:
            user_project_status.status = 'progress'
            user_project_status.save()
            context = {
                'project':project,
                'user_project_status':user_project_status
                }
     
        return render(request, 'dash/project_details.html', context=context)

    
class ProjectVeiw(LoginRequiredMixin,View):
    login_url= 'login'
    def get(self, request):
       return render(request, 'dash/projectview.html')
    
    
    def post(self, request):
        return render(request, 'dash/projectview.html')
    
    
    