import pyotp
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils import timezone
from .models import User
from django.conf import settings




def generate_otp():
    totp = pyotp.TOTP(pyotp.random_base32())  # OTP expires in 30 minutes
    return totp.now()



def send_otp(email):
    subject = "One Time Password (OTP) Generation"
    otp = generate_otp()
    user = User.objects.get(email=email)
    user.otp = otp
    user.is_otp_expired = timezone.now()  # Record the timestamp when OTP was sent
    user.save()
    body = f"Hi {user.username}, your OTP verification code is: {otp}. This code expires in two hours."
    email_from = settings.EMAIL_HOST_USER
    email_sent = EmailMessage(subject=subject, from_email=email_from, body=body, to=[email])
    email_sent.send(fail_silently=True)


def send_user(email):
    subject = "Welcome to Skill-RSU"
    user = User.objects.get(email=email)
    body = f"Hi {user.username},You are just a few steps away \n Below is your dept No:{user.dp_no}. \n   . Use it to log in to your account with your password. \n "
    email_from = settings.EMAIL_HOST_USER
    email_sent = EmailMessage(subject=subject, from_email=email_from, body=body, to=[email])
    email_sent.send(fail_silently=True)

