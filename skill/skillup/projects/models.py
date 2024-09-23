from typing import Iterable
from django.db import models
from user.models import User
from cohorts.models import CohortGroup
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone
from datetime import datetime
# Create your models here.


class Student_Project(models.Model):
    project_id= ShortUUIDField(unique=True, length=10, prefix='project_id', max_length=20, alphabet='project_id395533', editable=False)
    project_name = models.CharField(max_length=255) 
    description = models.TextField()
    start_date = models.DateTimeField() 
    end_date = models.DateTimeField() 
    task_required_score = models.IntegerField(max_length=200) 
    cohort =models.ManyToManyField(CohortGroup, related_name='tasks')  # T
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    def __str__(self):
        return self.project_name  # The teacher who created the task
project_status = (
    ('pending', 'Pending'),
     ('completed', "completed"),
     ('progress', "progress"),)
    
class UserProjectStatus(models.Model):
     status = models.CharField(max_length=20, choices=project_status, default='pending')
     user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='project_status')
     projects =  models.ForeignKey(Student_Project,on_delete=models.CASCADE, related_name='status')

     def __str__(self):
         return f"{self.user.full_name} - {self.projects.project_name}"
     
     def save(self,*args, **kwargs):
         if isinstance(self.projects.end_date, str):
             self.projects.end_date = datetime.strptime(self.projects.end_date, '%Y-%m-%dT%H:%M')
         # Convert the project's end_date to a timezone-aware datetime
         if timezone.is_naive(self.projects.end_date):
            self.projects.end_date = timezone.make_aware(self.projects.end_date, timezone.get_current_timezone())
         
         if self.projects.end_date <= timezone.now():
             self.status = 'completed'
         super().save(*args, **kwargs)
     
 


    



class TaskSubmission(models.Model):
    task_id= ShortUUIDField(unique=True, length=10, prefix='task_id', max_length=20, alphabet='task_id34905', editable=False)
    projects = models.ForeignKey(Student_Project, on_delete=models.CASCADE, related_name='submissions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_submissions')
    submission_url = models.URLField(blank=True, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    score = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.projects.project_name

class MonthlyScoreAllocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='monthly_allocations')
    required_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Track when the score was created

    def __str__(self):
        return f"{self.cohort.name} - Required Score: {self.required_score}"   

