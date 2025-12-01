from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=15,unique=True,null=True,blank=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)

    def __str__(self):
        return self.user.username

class UserOTP(models.Model):
    phone=models.CharField(max_length=15)
    otp=models.CharField(max_length=6)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone