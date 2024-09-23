from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
import pyotp
from datetime import timedelta
from django.utils import timezone
from decimal import Decimal

class User(AbstractUser):
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(unique=True, max_length=20)
    dp_no = models.CharField(max_length=200, unique=True)
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    is_verify = models.BooleanField(default=False)
    otp = models.CharField(max_length=50, blank=True, null=True)
    otp_time = models.DateTimeField(auto_now_add=True, null=True)
    otp_sent_at = models.DateTimeField(blank=True, null=True)
    suspension = models.BooleanField(default=False)

    USERNAME_FIELD = 'dp_no'
    REQUIRED_FIELDS = ['email', 'username']

    def __str__(self):
        return self.full_name
    
    def is_otp_expired(self): 
        if not self.otp_sent_at:  # If OTP has not been sent yet
            return True
        validity_period = timedelta(hours=2)  # Assuming OTP is valid for 2 hours
        current_time = timezone.now()
        time_difference = current_time - self.otp_sent_at
        return time_difference > validity_period
    

# def generate_otp():
#     while True:
#         code = random.randint(10, 2000)
#         formatted_code = f"{code:01}"  # 4 digits to cover up to 2000
#         dp_no = f"opolo{formatted_code}"
#         if not User.objects.filter(dp_no=dp_no).exists():
#             return dp_no

class Faculty(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'


    def __str__(self):
        return self.name

class CourseList(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


    def __str__(self):
        return self.name

    
status = (
    ('reject', 'reject'),
     ('pending', "pending"),

)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profiles")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="faculties", blank=True, null=True)
    course = models.ForeignKey(CourseList,on_delete=models.CASCADE, related_name='courselist',blank=True, null=True)
    department = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile')
    admitted = models.BooleanField(default=False)  # Field to track admission status
    date = models.DateTimeField(auto_now=True)
    status = models.CharField( max_length=300,default='pending')
    passcode = models.CharField(max_length=10, blank=True, null=True, unique=True)  # Add this field


    
    def __str__(self):
        return self.user.username



class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2)
    profit_percent = models.DecimalField(max_digits=5, decimal_places=2, default=2.0)  # 2% profit
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def save(self,*args, **kwargs):
        if not self.end_time:
            self.end_time =  self.start_time + timedelta(minutes=20)
            return super().save(*args, **kwargs)
    def calculate_profit(self):
        time_passed = (timezone.now() - self.start_time).total_seconds() // 300  # 5 minutes = 300 seconds
        max_intervals = 4  # 20 minutes total, so 4 intervals
        intervals = min(time_passed, max_intervals)
        percentage = self.profit_percent / Decimal(100)
        intervals_decimal = Decimal(intervals)
        self.profit = self.amount_invested * percentage* intervals_decimal
        return self.profit
    
    def is_matured(self):
        return timezone.now() >= self.end_time

    def delete_if_matured(self):
        # Delete the investment if it is matured
        if self.is_matured():
            self.delete()

    def __str__(self):
        return f"{self.user.username} - {self.amount_invested}"

# class CourseList(models.Model):
#     name = models.CharField(max_length=200)
#     class Meta:
#         verbose_name = 'course'
#         verbose_name_plural = 'courses'


#     def __str__(self):
#         return self.name




# @receiver(pre_save, sender=User)
# def set_unique_dp_no(sender, instance, **kwargs):
#     if not instance.dp_no:
#         instance.dp_no = generate_otp()
#     while User.objects.filter(dp_no=instance.dp_no).exists():
#         instance.dp_no = generate_otp()
