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

class AddListUser(LoginRequiredMixin,UserPassesTestMixin,View):
     login_url = login

     
     def test_func(self):
        return self.request.user.is_staff
     def handle_no_permission(self):
         return redirect('login')
     def get(self,request):
                return render(request, 'admin/adduserlist.html')
        
    

def studentadd(request):
      admitted = User.objects.filter(profiles__admitted=True, cohorts__isnull=True).order_by('-profiles__date')
      admitted_list = list(admitted.values('id', 'profiles__department', 'profiles__image', 'profiles__date', 'profiles__course__name', 'full_name', 'email'))
        # admitted_list = list(adminitted.object_list.values('id', 'department', 'image', 'date','course','user__full_name'))
      return  JsonResponse({
            "admitted_list": admitted_list
        })


def listcourses(request):
      allcourses = CourseList.objects.all()
      list_courses = list(allcourses.values('id', 'name'))
      return JsonResponse({
            'list_courses': list_courses
      })




def fitterbycourse(request):
  course_id = request.GET.get('course_id')
  if not course_id:
        return JsonResponse({'error': 'Course ID is required'}, status=400)
  else:
       students_admitted = User.objects.filter(
            profiles__admitted=True,  # Admitted users
            cohorts__isnull=True,  # Users not in any cohort
            profiles__course_id=course_id  # Filter by course
        ).order_by('-profiles__date')
       student_list = list(students_admitted.values('id', 'profiles__department','profiles__image','profiles__date', 
            'profiles__course__name', 
            'full_name', 
            'email'))
  return JsonResponse({
            'student_list': student_list
       })


def users_search(request):
  search = request.GET.get('query')
  if not search:
        return JsonResponse({'error': 'search is required'}, status=400)
  else:
       user_search = Profile.objects.filter(
           
            Q(course__name__icontains=search)| 
            Q(user__full_name__icontains=search) |
            Q(user__email__icontains=search),
             admitted=True,
           )
       search_list = list(user_search.values('id', 'department', 'image', 'date', 'course__name', 'user__full_name','user__email'))
  return JsonResponse({
            'student_list': search_list
       })



@login_required
@require_POST
def add_user_to_cohort(request):
    try:
        datas = json.loads(request.body)
        user_ids = datas.get('student_ids', [])
        cohort_id = datas.get('cohort_id')

        if not user_ids or not cohort_id:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

        cohort = get_object_or_404(CohortGroup, id=cohort_id)
        
        # Check cohort size limit (max 20 members)
        if cohort.users.count() >= 20:
            return JsonResponse({'error': 'Cohort already has 20 members, no more can be added.'}, status=400)

        users = User.objects.filter(id__in=user_ids)
        already_in_cohort = []
        newly_added_users = []

        # Check if each user is already in the cohort before adding
        for user in users:
            if cohort.users.filter(id=user.id).exists():
                already_in_cohort.append(user.full_name)  # Assuming 'full_name' exists on User model
            else:
                # Add only users who are not in the cohort, and only if the cohort is below 20 users
                if cohort.users.count() < 20:
                    cohort.users.add(user)
                    newly_added_users.append(user.full_name)
                else:
                    return JsonResponse({'error': 'Cohort has reached its member limit (20 members).'}, status=400)
        
        cohort.save()

        if already_in_cohort:
            return JsonResponse({
                'error': 'Some users are already in the cohort',
                'already_in_cohort': already_in_cohort
            }, status=400)

        if newly_added_users:
            return JsonResponse({
                'success':'Users added to cohort successfully'
            })
        else:
            return JsonResponse({'error': 'No new users were added to the cohort.'}, status=400)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)


# here is the code that list all the code and id of each cohort 
@login_required
def Cohort_List(request):
      allcohorts = CohortGroup.objects.all()
      cohort_list = list(allcohorts.values('id', 'name'))
      return JsonResponse({
            'cohort_list': cohort_list
      })



       
           

        
    
