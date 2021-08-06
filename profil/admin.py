from django.contrib import admin
from .models import User_more_info, User_Avatar, User_LinkTree

# Register your models here.
admin.site.register(User_more_info)
admin.site.register(User_Avatar)
admin.site.register(User_LinkTree)