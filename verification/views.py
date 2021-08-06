import random
import re
import os
import requests, json
from itertools import chain
from datetime import datetime
from hashlib import md5, sha1
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from throttle.decorators import throttle
from django.forms.models import model_to_dict
from django.shortcuts import render
from .models import active_user, Inactive_user
# Create your views here.
def verification(request, key, *args, **kwargs):
    User = get_user_model()
    inactive_check = Inactive_user.objects.filter(verif_key=key).count()
    if inactive_check:
        in_user = Inactive_user.objects.get(verif_key=key)
        in_user_id = in_user.user_id
        user_data = User.objects.get(id=in_user_id)
        save = active_user(user_id=in_user_id)
        save.save()
        in_user.delete()
        context = {
            "username": user_data,
            "Head":"Email Verification",
            "Judul":"TellBy",
            "cdn":"https://cdn.tell.by",
        }
        return render(request,'verif.html',context)
    else:
        return redirect('/')