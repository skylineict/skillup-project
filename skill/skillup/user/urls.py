from django.urls import path
from .views import Register,Email_verification,Login,Profiles,logout_view
from .otp_resent import Resentotp




urlpatterns = [
    path('', Register.as_view(), name='register'),
    path('emailverify', Email_verification.as_view(), name='email_otp'),
    path('login', Login.as_view(), name='login'),
    path('profile', Profiles.as_view(), name='profile'),
    path('logout',logout_view, name='logout'),
      path('resent',Resentotp.as_view(), name='resent'),

]
