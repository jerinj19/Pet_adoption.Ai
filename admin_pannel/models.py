from django.db import models

class Admin_add(models.Model):
    Add_name=models.CharField(max_length=15,null=True,blank=True)
    Add_location=models.CharField(max_length=20,null=True,blank=True)
    Add_images=models.ImageField(upload_to="add_images",null=True,blank=True)
