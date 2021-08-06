from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from tinymce.models import HTMLField

# Create your models here.from django.contrib.auth.models import User
class Inactive_user(models.Model):
    user_id = models.DecimalField(max_digits=50, decimal_places=0, default=0)
    verif_key = models.CharField(max_length=300,blank=True,null=True)

class active_user(models.Model):
    user_id = models.DecimalField(max_digits=50, decimal_places=0, default=0)
