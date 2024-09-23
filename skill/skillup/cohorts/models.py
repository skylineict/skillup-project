from django.db import models
from user.models import User

# Create your models here.


class CohortGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    whatsapp = models.CharField( max_length=300)
    users = models.ManyToManyField(User, related_name='cohorts', blank=True) 


    def __str__(self):
        return self.name



    
 