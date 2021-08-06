from django import forms
from tinymce.models import HTMLField
from django.db import models
#
class PostinganForm(forms.Form):
    content = HTMLField()

    class Meta:
        fields = ['content']


class KomenForm(forms.Form):
    komen = models.TextField(blank=False, null=False)

    class Meta:
        fields = ['komen']