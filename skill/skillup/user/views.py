from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from .models import User,Profile, Faculty,CourseList
from .ots_email import send_otp, send_user
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
import pdb
from django.urls import reverse
from django.contrib.auth import logout




class Register(View):
    def get(self, request):
        return render(request, "user/register.html")
    
    def post(self, request):
            username = request.POST['username']
            email = request.POST['email']
            full_name = request.POST['full_name']
            password = request.POST['password']
            comfirm = request.POST['password1']
            phone = request.POST['phone']

            if password != comfirm:
                return JsonResponse({"error": "Passwords do not match"}, status=400)

            if not username.isalnum():
                return JsonResponse({"error": "Username should only contain alphanumeric characters"}, status=400)
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username is already taken"}, status=400)
            
            if User.objects.filter(phone=phone).exists():
                return JsonResponse({"error": "phone number is already taken"}, status=400)
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email is already registered"}, status=400)
            # dp_no = generate_otp()
            user = User.objects.create(username=username,
                                       email=email,
                                       full_name=full_name,
                                       phone=phone,
                                       dp_no=username)
            user.set_password(password)
            user.save()
            send_otp(email)
            send_user(user.email)
            return JsonResponse({"success": "Registration successful. Redirecting..."}, status=200)
    



class Email_verification(View):
     def get(self,request):
        
          return render(request, "user/email_otp.html")
     
     
     def post(self,request):
          otp_code = request.POST['otp']
          try:
               user = User.objects.get(otp=otp_code)
          except User.DoesNotExist:
                return JsonResponse({"error": "account with provided otp not found"},status=400)
          if not otp_code:
            return JsonResponse({"error": "Verification code is not provided"}, status=400)
          if user.is_otp_expired():
            send_otp(user.email)
            return JsonResponse({"error": " code expired. New code sent to your email"},status=400)
          if user.otp !=otp_code:
            return JsonResponse({"error": "Invalid verification code"}, status=400)
        
          if user.is_verify:
            return JsonResponse({"error": "email already verified"},status=400)
          user.is_verify = True
          user.save()

          
        #   Profile.objects.create(user=user)
          Profile.objects.get_or_create(user=user)
         
          return JsonResponse({"success": "Email Verify successfuly"},status=200)
     

class Login(View):
    def get(self,request):
        return render(request,"user/login.html")
    
    def post(self,request):
        dp_no = request.POST['dptno']
        password = request.POST['password']
        user = authenticate(dp_no=dp_no, password=password)
        if user is None:
            return JsonResponse({'error': "Invalid DP No or password"}, status=400)
          
        if not user.is_verify:
            send_otp(user.email)
            return JsonResponse({'verify': "Email is not verified,redirecting...."},status=400) 
        if not user.check_password(password):
             return JsonResponse({'error': "Incorrect password"},status=400) 
        login(request, user)  # Log the user in first
        
        try:
            profile = Profile.objects.get(user=user)
            if not profile.department or not profile.state or not profile.level:
                 
                  return JsonResponse({'is_profile': "please update profile  "},status=400) 
        except Profile.DoesNotExist:
             return JsonResponse({'profile': "procced in creatig profile "},status=400) 
           
              # Redirect to profile completion page if profile doesn't exist
        if user:
            if user.is_staff:
                  login(request, user)
                  return JsonResponse({'admin': "Login To Admin redrecting....."},status=200) 
            else:
                login(request, user)
            return JsonResponse({'success': "Login redrecting....."},status=200) 

        
        return render(request,"user/login.html")

class Profiles(LoginRequiredMixin,View):
    login_url = 'login'
   
    def get(self,request):
        try:
            user_profile = Profile.objects.get(user=request.user)
            if user_profile.faculty and user_profile.department and user_profile.level and user_profile.state:
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                      return JsonResponse({"profile_exit": "filled"}, status=200)
                else:
                    pass
               
        except Profile.DoesNotExist:
            pass

        faculties = Faculty.objects.all()
        courses = CourseList.objects.all()
        login_user = request.user
        context = {
            'faculties': faculties,
            'login_user': login_user,
            'courses':courses


        }
      
        # pdb.set_trace()
        return render(request, "user/profile.html",context=context)
    
    def post(self,request):
            faculty_name = request.POST['faculty']
            courses = request.POST['courses']
            department = request.POST['department']
            level = request.POST['level']
            state = request.POST['state']
            city = request.POST['city']
            profile_pic = request.FILES.get('file')
            if profile_pic:
                print(f"Received image: {profile_pic.name}")
                print(f"Image size: {profile_pic.size} bytes")
            else:
                print("No image receivedfv ndfndsnfndsnndns")


          
 
         
            if not faculty_name:
                return JsonResponse({"error": "Faculty is required"}, status=400)
            if not courses:
                return JsonResponse({"error": "course is required"}, status=400)
            if not department:
                return JsonResponse({"error": "Department is required"}, status=400)
            if not state:
                return JsonResponse({"error": "State is required"}, status=400)
            if not city:
                return JsonResponse({"error": "City is required"}, status=400)
            if not level:
                return JsonResponse({"error": "Level is required"}, status=400)
            if not profile_pic:
                return JsonResponse({"error": "picture  is required"}, status=400)
            try:
                faculty = Faculty.objects.get(name=faculty_name)
                course = CourseList.objects.get(name=courses)
                # pdb.set_trace()
            except Faculty.DoesNotExist:
                return JsonResponse({"error": f"Faculty with name '{faculty_name}' does not exist"}, status=400)


            updateprofile = Profile.objects.get(user=request.user)
            # pdb.set_trace()
            updateprofile.faculty = faculty
            updateprofile.department = department
            updateprofile.level = level
            updateprofile.state =state
            updateprofile.image = profile_pic
            updateprofile.course =course
            print(profile_pic)
            updateprofile.save()
            # return render(request, "user/profile.html")
            return JsonResponse({"success": "Profile updated successfully"}, status=200)
        
        # except Exception as e:
        #     return JsonResponse({"error": str(e)}, status=500)

        

        # return render(request, "user/profile.html")
def logout_view(request):
    try:
        logout(request)
        return JsonResponse({'success': 'Logout successful.'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
