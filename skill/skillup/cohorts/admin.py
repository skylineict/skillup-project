from django.contrib import admin
from .models import CohortGroup

# Register your models here.

@admin.register(CohortGroup)
class Cohorts(admin.ModelAdmin):
    list_display = ['name','description','created_at','whatsapp']