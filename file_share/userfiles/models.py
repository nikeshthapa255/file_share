from django.db import models
from django.contrib.auth.models import User


class Ufile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    #expires_on=models.DateTimeField(auto_now=True)
    name=models.CharField(max_length=100)
    fileloc= models.FileField(upload_to='User_files/', null=True, verbose_name="")
    def __str__(self):
        return self.name+" : "+ str(self.fileloc)
    


