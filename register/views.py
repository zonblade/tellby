from django.shortcuts import render, redirect
from django.urls import path, include
from django.contrib.auth import get_user_model
from .forms import RegisterForm
import random
import re
import requests, json
from itertools import chain
from datetime import datetime
from hashlib import md5, sha1, sha512
from throttle.decorators import throttle
from verification.models import Inactive_user
# Create your views here.
@throttle(zone='default')
def register(response):
    email_err = False
    username_err = False
    length_err = False
    register_success = False
    form = RegisterForm(response.POST)
    if response.method == "POST":
        User = get_user_model()
        names = response.POST['username']
        emails = response.POST['email']
        if User.objects.filter(username=names).exists():
            print('username exist!')
            username_err = True
        else:
            if len(names) > 6 :
                if User.objects.filter(email=emails).exists():
                    print('email exist!')
                    email_err = True
                else:
                    form = RegisterForm(response.POST)
                    username = response.POST.get('username')
                    if re.match(r'^[a-z0-9_-]+$', username):
                        if form.is_valid():
                            form.save()

                            #kirim verifikasi!
                            verif_email = response.POST.get('email')
                            verif_uname = username
                            verif_ui = User.objects.get(username=username)
                            verif_uid = verif_ui.id

                            verif_k_data = verif_uid + random.getrandbits(128), "-url-", verif_uname, verif_email
                            verif_k_hash = sha512(str(verif_k_data).encode("UTF-8")).hexdigest()[:128]
                            verif_final_hash = verif_k_hash
                            verif_url = 'https://cdns.tell.by/???/verify.php'  #remove secret key
                            verif_key = '???'  #remove secret key
                            verif_ok = {'key' : verif_key,'url_key':verif_final_hash ,'user_id': verif_uid, 'username': verif_uname,'email': verif_email }
                            r = requests.post(verif_url,data=verif_ok)
                            masuk_inac = Inactive_user(user_id=verif_uid,verif_key=verif_final_hash)
                            masuk_inac.save()

                            form = RegisterForm()
                            register_success = True
                        #return redirect('/auth/login/')
                    else:
                        username_err = True
            else:
                length_err = True
    else:
        form = RegisterForm()

    context = {
        "Head":"TellBy",
        "Judul":"TellBy",
        "cdn":"https://cdn.tell.by",
        "form" : form,
        "email_err" : email_err,
        "length_err" : length_err,
        "username_err": username_err,
        "register_success":register_success
    }
    if response.user.is_authenticated == True:
        return redirect('/')
    else:
        return render(response, 'register/register.html', context)
