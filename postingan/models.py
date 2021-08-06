from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from tinymce.models import HTMLField
from profil.models import User_Avatar

# Create your models here.
class Komentar(models.Model):
    post_id = models.DecimalField(max_digits=50, decimal_places=0)
    user_id = models.DecimalField(max_digits=50, decimal_places=0)
    komen_date = models.DateTimeField(auto_now_add=True)
    komen = models.TextField(blank=False, null=False)

    def user(self):
        return User.objects.get(pk=self.user_id)

class Postingan(models.Model):
    user_id = models.DecimalField(max_digits=50, decimal_places=0)
    mock_url= models.TextField(blank=False, null=False)
    post_title = models.TextField(blank=True, null=True, default='Story')
    post_keyword = models.TextField(blank=True, null=True, default='Tell By Story')
    post_date = models.DateTimeField(auto_now_add=True)
    post_update = models.DateTimeField(auto_now=True)
    content = HTMLField()
    post_seen = models.DecimalField(max_digits=50, decimal_places=0, default=0)

    def user(self):
        return User.objects.get(pk=self.user_id)
    def commentCount(self):
        return Komentar.objects.filter(post_id=self.id).count()

class Prefered_Template(models.Model):
    user_id = models.DecimalField(max_digits=50, decimal_places=0)
    template_type = models.DecimalField(max_digits=50, decimal_places=0,default=1)