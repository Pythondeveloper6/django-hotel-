from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, related_name='user_profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/')
    phone_number = models.CharField(max_length=16)
    address = models.CharField(max_length=50)


    def __str__(self):
        return str(self.user)