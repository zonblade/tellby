from django import forms
from tinymce.models import HTMLField
from django.db import models
from profil.models import User_Avatar, User_LinkTree
#
class MoreInfoForm(forms.Form):
    bio = models.CharField(max_length=300,blank=True,null=True)
    facebook = models.CharField(max_length=300,blank=True,null=True)
    instagram = models.CharField(max_length=300,blank=True,null=True)
    twitter = models.CharField(max_length=300,blank=True,null=True)

    class Meta:
        fields = ['bio','facebook','instagram','twitter']

class AvatarForm(forms.Form):
    user_id = models.DecimalField(max_digits=50, decimal_places=0, default=0)
    avatar = models.ImageField(null=True,blank=True, upload_to='static/img/avatar/')

    class Meta:
        model = User_Avatar
        fields = ['avatar']
class LinkForm(forms.Form):
    class Meta:
        model = User_LinkTree
        fields = ['img','link','title','order']