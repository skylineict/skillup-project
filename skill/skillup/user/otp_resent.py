from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from .models import User
from .ots_email import send_otp, send_user
import pdb
from django.urls import reverse
from django.contrib.auth import logout


class Resentotp(View):
    def get(self, request):
        return render(request, 'user/resent_otp.html')
    

    def post(self, request):
        email = request.POST['email']
        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User with this email does not exist'}, status=400)
        
        if not user.is_verify:
            send_otp(email)  # This function should send a new OTP to the user's emai
            send_user(email)
            return JsonResponse({'success': 'OTP has been sent to your email'}, status=200)
        else:
            return JsonResponse({'error': 'Email already verified'}, status=400)

      
