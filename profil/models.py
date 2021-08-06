from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from tinymce.models import HTMLField

# Create your models here.from django.contrib.auth.models import User


class User_more_info(models.Model):
    user_id = models.DecimalField(max_digits=50, decimal_places=0, default=0)
    bio = models.CharField(max_length=300,blank=True,null=True)
    facebook = models.CharField(max_length=300,blank=True,null=True,default='#')
    instagram = models.CharField(max_length=300,blank=True,null=True,default='#')
    twitter = models.CharField(max_length=300,blank=True,null=True,default='#')
    github = models.CharField(max_length=300,blank=True,null=True,default='#')
    dribbble = models.CharField(max_length=300,blank=True,null=True,default='#')

class User_Verified(models.Model):
    user_id = models.DecimalField(max_digits=50, decimal_places=0, default=0)
    verified = models.CharField(max_length=1,blank=False,null=False,default='0')

class User_LinkTree(models.Model):
    user_id = models.DecimalField(max_digits=50, decimal_places=0, default=0)
    mock = models.CharField(max_length=300,blank=True,null=True)
    img = models.CharField(max_length=300,blank=True,null=True,default='https://cdn.tell.by/img/icon/eucalyptus.png')
    link = models.CharField(max_length=300,blank=True,null=True,default='#')
    desc = models.CharField(max_length=300,blank=True,null=True,default='#')
    title = models.CharField(max_length=300,blank=True,null=True,default='#')
    order = models.CharField(max_length=300,blank=True,null=True,default='0')

class User_Avatar(models.Model):
    user_id = models.DecimalField(max_digits=50, decimal_places=0, default=0)
    avatar =  models.CharField(max_length=300,blank=True,null=True)

    def detail(self):
        return User.objects.get(id=self.user_id)
class UserActivity(models.Model):
    user_id = models.DecimalField(max_digits=50, decimal_places=0, default=0)
    obj_type = models.DecimalField(max_digits=50, decimal_places=0, default=0)
    act_type = models.DecimalField(max_digits=50, decimal_places=0, default=0)
    obj_link = models.CharField(max_length=300,blank=True,null=True,default='#')
    obj_time = models.DateTimeField(auto_now_add=True)

