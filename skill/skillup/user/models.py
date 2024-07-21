from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
import pyotp
from datetime import timedelta
from django.utils import timezone

def generate_otp():
    # Generate a base32 secret for TOTP
    secret = pyotp.random_base32()
    # Create a TOTP object with the secret
    totp = pyotp.TOTP(secret)
    # Get the current OTP
    otp = totp.now()
    # Use only the last 3 digits to ensure a shorter dp_no
    return f"opolo{otp[-2:]}"

class User(AbstractUser):
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(unique=True, max_length=20)
    dp_no = models.CharField(max_length=200, unique=True)
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    is_verify = models.BooleanField(default=False)
    otp = models.CharField(max_length=50, blank=True, null=True)
    otp_time = models.DateTimeField(auto_now_add=True, null=True)

    USERNAME_FIELD = 'dp_no'
    REQUIRED_FIELDS = ['email', 'username']

    def __str__(self):
        return self.username
    
    def is_otp_expired(self): 
        if not self.otp_time:  # If OTP has not been sent yet
            return True
        validity_period = timedelta(hours=2)  # Assuming OTP is valid for 2 hours
        current_time = timezone.now()
        time_difference = current_time - self.otp_time
        return time_difference > validity_period

class Faculty(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'


    def __str__(self):
        return self.name
    
    
status = (
    ('reject', 'reject'),
     ('pending', "pending"),

)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profiles")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="faculties", blank=True, null=True)
    department = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile')
    admitted = models.BooleanField(default=False)  # Field to track admission status
    date = models.DateTimeField(auto_now=True)
    status = models.CharField( max_length=300,default='pending')
    
    def __str__(self):
        return self.user.username





# @receiver(pre_save, sender=User)
# def set_unique_dp_no(sender, instance, **kwargs):
#     if not instance.dp_no:
#         instance.dp_no = generate_otp()
#     while User.objects.filter(dp_no=instance.dp_no).exists():
#         instance.dp_no = generate_otp()
