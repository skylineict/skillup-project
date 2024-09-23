from django.contrib import admin
from .models import Student_Project, TaskSubmission,UserProjectStatus

# Register your models here.


@admin.register(Student_Project)
class StudentprojectAdmin(admin.ModelAdmin):
    list_display = ['project_name','project_id','description','start_date','end_date','task_required_score','user']



@admin.register(TaskSubmission)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','submission_url','submission_date','approved','score']
    


@admin.register(UserProjectStatus)
class ProjectstatusAdmin(admin.ModelAdmin):
    list_display = ['user','status','projects']
