from django.contrib import admin
from .models import User,Faculty,Profile,CourseList,Investment

# Register your models here.r
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'dp_no', 'full_name', 'phone', 'is_verify', 'otp', 'otp_sent_at','otp_time', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_verify')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'dp_no', 'full_name', 'phone', 'otp')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_verify', 'groups', 'user_permissions')}),
    )


@admin.register(Faculty)
class FacultiesAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','faculty','department','state','level', 'passcode', 'course','admitted','date']

@admin.register(CourseList)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']



@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ['user','amount_invested','profit_percent','start_time','end_time', 'profit']

