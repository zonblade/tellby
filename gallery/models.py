from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

#
class Image_Gallery(models.Model):
    user_id = models.DecimalField(max_digits=65, decimal_places=0, default=0)
    img_name = models.CharField(max_length=300,blank=False,null=False)
    img_date = models.DateTimeField(auto_now_add=True)
    img_seen = models.DecimalField(max_digits=50, decimal_places=0, default=0)