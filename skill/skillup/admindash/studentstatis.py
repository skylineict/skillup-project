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
from user.models import Profile,Faculty,User, CourseList
from cohorts.models import CohortGroup
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.paginator  import Paginator,EmptyPage,PageNotAnInteger
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from user .passcodegen import generate_passcode
from django.db.models import Q
from django.db.models import Count
from django.shortcuts import get_object_or_404

class UserStatics(LoginRequiredMixin,UserPassesTestMixin,View):
     login_url = login

     
     def test_func(self):
        return self.request.user.is_staff
     def handle_no_permission(self):
         return redirect('login')
     
     def get(self,request):
 
        all_courses_count = CourseList.objects.count()
        courses = CourseList.objects.annotate(num_user=Count('courselist')
                                              )
        
        user_with_course = Profile.objects.filter(course__isnull=False).count()


        context = {
            'courses_num': all_courses_count,
            'users_courses': user_with_course,
            'courses': courses
        }

    
        # pdb.set_trace()
                
        return render(request, 'admin/useratatices.html', context=context)
     
    #  def post(self,request):
        
    #     name = request.POST.get('name')
    #     whatsapp = request.POST.get('url') # Using 'whatsapp' for the group link
    #     print(name)

    #     if not name:
    #         return JsonResponse({'error': 'Cohort name is required'}, status=400)
    #     if not whatsapp:
    #         return JsonResponse({'error': 'Cohort whatsapplink is required'}, status=400)

    #     # Create a new cohort group
    #     cohort = CohortGroup.objects.create(name=name, whatsapp=whatsapp)
    #     return JsonResponse({'success': 'Cohort created successfully', 'cohort_id': cohort.id}, status=201)
        

def user_courseList(request, course_id):
    
     if not course_id:
        return JsonResponse({'error': 'Course ID is required'}, status=400)
        
     course = get_object_or_404(CourseList, id=course_id)
     students = Profile.objects.filter(course=course)
     student_list = list(students.values('id', 'department', 'image', 'date', 'course__name', 'user__full_name', 'user__email'))
     
     return JsonResponse({'student_list': student_list})
  

class UserDetailsVeiw(LoginRequiredMixin,UserPassesTestMixin,View):
     login_url = login

     
     def test_func(self):
        return self.request.user.is_staff
     def handle_no_permission(self):
         return redirect('login')
      
     def get(self, request, course_id):
         course_id = get_object_or_404(CourseList, id=course_id)
        
         context = {
            'course': course_id,
            }
        
         return render(request, 'admin/userDetaisl_by.html', context=context)
     


# class UserDetailsVeiw(LoginRequiredMixin,UserPassesTestMixin,View):
#      login_url = login

     
#      def test_func(self):
#         return self.request.user.is_staff
#      def handle_no_permission(self):
#          return redirect('login')
      
#      def get(self, request, course_id):
#          course = get_object_or_404(CourseList, id=course_id)
#          users = Profile.objects.filter(course=course)
#          context = {
#             'course': course,
#             'users': users,}
        
#          return render(request, 'admin/userDetaisl_by.html', context=context)
     
