from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.

class Posts(models.Model):
    user = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/')
    availability = models.DateTimeField(default=timezone.now)
    
    