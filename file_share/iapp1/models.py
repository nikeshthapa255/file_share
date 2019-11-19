from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=100,default='')
    created_on=models.DateTimeField(auto_now_add=True)
    profile_pic=models.ImageField(upload_to='profile_pic',blank=True)
    def __str__(self):
        return self.user.name
