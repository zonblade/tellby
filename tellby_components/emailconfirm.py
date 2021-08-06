
import random
import re
import requests, json
from django.contrib.auth.models     import User
from django.http                    import HttpResponse
from django.shortcuts                   import render, redirect
from django.urls                        import path, include
from itertools                          import chain
from datetime                           import datetime
from hashlib                            import md5, sha1, sha512
from verification.models                import active_user, Inactive_user

def MailSender(verif_uid,verif_uname,verif_email,verif_final_hash):
    verif_url           = 'https://cdns.tell.by/???/verify.php'  #remove secret key
    verif_key           = '???'  #remove secret key
    verif_ok            = {'key' : verif_key,'url_key':verif_final_hash ,'user_id': verif_uid, 'username': verif_uname,'email': verif_email }
    r = requests.post(verif_url,data=verif_ok)
    ue          = User.objects.get(id=verif_uid)
    ue.email    = verif_email
    ue.save()
    print('mail sent')

def ConfirmEmailSEND(email,username,ids):
    inactive            = Inactive_user.objects.filter(user_id=ids).count()
    verif_email         = email
    verif_uname         = username
    verif_uid           = ids
    inactive            = inactive
    verif_k_data        = verif_uid + random.getrandbits(128), "-url-", verif_uname, verif_email
    verif_k_hash        = sha512(str(verif_k_data).encode("UTF-8")).hexdigest()[:128]
    verif_final_hash    = verif_k_hash
    print(verif_email)
    if verif_email:
        valids          = User.objects.filter(email=verif_email).count()
        print(valids,'valid')
        if valids < 1:
            print(inactive, 'inactive')
            if inactive:
                print('in inactive')
                ma              = Inactive_user.objects.get(user_id=verif_uid)
                ma.verif_key    = verif_final_hash
                ma.save()
                avcek           = active_user.objects.filter(user_id=verif_uid).count()
                if avcek:
                    print(avcek,'on avcek')
                    avdel       = active_user.objects.get(user_id=verif_uid)
                    avdel.delete()
                    MailSender(verif_uid,verif_uname,verif_email,verif_final_hash)
                    return HttpResponse('#')
                else:
                    print('not on avcheck')
                    MailSender(verif_uid,verif_uname,verif_email,verif_final_hash)
                    return HttpResponse('#')
            elif not inactive:
                print('not in inactive')
                masuk_inac      = Inactive_user(user_id=verif_uid,verif_key=verif_final_hash)
                masuk_inac.save()
                avcek           = active_user.objects.filter(user_id=verif_uid).count()
                if avcek:
                    print(avcek,'on avcek')
                    avdel       = active_user.objects.get(user_id=verif_uid)
                    avdel.delete()
                    MailSender(verif_uid,verif_uname,verif_email,verif_final_hash)
                    return HttpResponse('%')
                else:
                    print('not on avcheck')
                    MailSender(verif_uid,verif_uname,verif_email,verif_final_hash)
                    return HttpResponse('#')
            else:
                return HttpResponse('&')
        elif inactive and valids == 1:
            print('valid but inactive')
            EmailExist = User.objects.filter(email=verif_email).count()
            print(EmailExist)
            if EmailExist:
                UserEmail = User.objects.filter(id=verif_uid, email=verif_email).count()
                if UserEmail:
                    print('A same owner')
                    return HttpResponse('&')
                else:
                    print('A different owner')
                    return HttpResponse('*')
            else:
                print('email does not exist?')
        else:
            print('valid but active')
            EmailExist = User.objects.filter(email=verif_email).count()
            print(EmailExist)
            if EmailExist:
                UserEmail = User.objects.filter(id=verif_uid, email=verif_email).count()
                if UserEmail:
                    print('A same owner')
                    return HttpResponse('@')
                else:
                    print('A different owner')
                    return HttpResponse('*')
            else:
                print('email does not exist?')
    else:
        return HttpResponse('0')