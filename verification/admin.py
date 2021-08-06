from django.contrib import admin
from .models import Inactive_user, active_user

# Register your models here.
admin.site.register(Inactive_user)
admin.site.register(active_user)