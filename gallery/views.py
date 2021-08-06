import random
import os
import requests, json
from hashlib                        import md5, sha1
from django.shortcuts               import render, redirect
from django.contrib.auth.models     import User
from django.core.paginator          import Paginator
from django.http                    import HttpResponse
from .models                        import Image_Gallery
from profil.models                  import User_more_info
from tellby_components.verification import ActiveUser
from tellby_components.postingan    import endlessPagination

# Create your views here.
def image_gallery(request, username, *args, **kwargs):

    active = ActiveUser(request.user.id)

    obj_user            = User.objects.get(username=username)
    usr_more            = User_more_info.objects.filter(user_id=obj_user.id).count()
    usr_more_print      = False
    img_success         = False
    if usr_more:
        usr_more_print  = User_more_info.objects.get(user_id=obj_user.id)

    img_print   = Image_Gallery.objects.filter(user_id=obj_user.id).order_by('-id')
    img_count   = Image_Gallery.objects.filter(user_id=obj_user.id).count()
    img_empty   = False
    img_obj     = endlessPagination(request,img_print,12)
    if not img_count:
        img_empty = True

    if request.user.is_authenticated:
        if username == request.user.username:
            if request.POST:
                if 'gpost' in request.POST:
                    mockUrl_data    = request.user.id + random.getrandbits(128), request.user.username, "-gallery!", request.user.username
                    mockUrl_hash    = sha1(str(mockUrl_data).encode("UTF-8")).hexdigest()[:45]
                    mockUrl_fin     = md5(str(mockUrl_hash).encode("UTF-8")).hexdigest()[:45]
                    if img_count < 100:
                        img = Image_Gallery(user_id=request.user.id,img_name=mockUrl_hash)
                        img.save()

                        URL         = 'https://cdn.tell.by/data.cgi@key=???' #remove key
                        myfile      = request.FILES.get('gallery')
                        sv_key      = {'secretkey' : '???','image_name_hash':mockUrl_hash ,'secret_user_id': request.user.id } #remove secret key
                        files       = {'upfile' : myfile}
                        r           = requests.post(URL,data=sv_key, files = files)
                        img_success = True
                        return redirect('/'+username+'/gallery/',sep='')
                    else:
                        return HttpResponse('100')
                else:
                    return HttpResponse('0')

                if 'gdpost' in request.POST:
                    filename        = request.POST.get('img_name')
                    file = os.path.isfile('/var/www/tell_by/src/tellby/static/img/galeri/'+filename+'.jpg')
                    if file:
                        img_confirm = Image_Gallery.objects.get(img_name=filename)
                        if img_confirm.user_id == request.user.id:
                            img_del = Image_Gallery.objects.get(user_id=request.user.id,img_name=filename)
                            img_del.delete()
                            os.remove('/var/www/tell_by/src/tellby/static/img/galeri/'+filename+'.jpg')
                            return redirect('/'+username+'/gallery/',sep='')
                        else:
                            return HttpResponse('0')
                    else:
                        return HttpResponse('0')
                else:
                    return HttpResponse('0')

    context = {
        "Head"          :"Gallery",
        "Judul"         :"TellBy",
        "cdn"           :"https://cdn.tell.by",
        "user_data"     :obj_user,
        "more_info"     :usr_more_print,
        "img_print"     :img_print,
        "content_post"  :img_obj,
        "img_count"     :img_count,
        "img_empty"     :img_empty,
        "active"        :active
    }
    if request.method == 'POST':
        if 'profile.gallery.render' in request.POST:
            return render(request, 'ajax/gallery.html', context)

    return render(request, 'django/gallery.html', context)