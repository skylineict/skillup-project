from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=400)
    content = models.TextField()
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name

