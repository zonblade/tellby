import random
import re
import requests, json
from itertools                      import chain
from datetime                       import datetime
from hashlib                        import md5, sha1, sha512
from throttle.decorators            import throttle
from postingan.models               import Postingan
from tellby_components.emailconfirm import ConfirmEmailSEND
from django.shortcuts               import render, redirect
from django.contrib.auth.models     import User
from django.http                    import HttpResponse
from tellby_components.verification import ActiveUser, XActiveUser
from tellby_components.postingan    import endlessPagination
from .models                        import User_more_info, User_LinkTree
from .forms                         import MoreInfoForm, AvatarForm, LinkForm


# Create your views here.
@throttle(zone='default')
def user_profile(request, username):
    #biography information  
    obj_user        = User.objects.get(username=username)
    active_pub      = ActiveUser(obj_user.id)
    active          = ActiveUser(request.user.id)
    postingan_obj   = Postingan.objects.filter(user_id=obj_user.id).order_by('-id')
    post_obj_count  = postingan_obj.count()
    postingan_obj   = endlessPagination(request,postingan_obj,9)
    #check if post empty
    post_empty      = True
    if post_obj_count >= 1:
        post_empty  = False
    #kosong atau engga db nya
    usr_more_q      = User_more_info.objects.filter(user_id=obj_user.id)
    usr_more        = usr_more_q.count()
    usr_more_print  = False
    if usr_more:
        usr_more_print = User_more_info.objects.get(user_id=obj_user.id)
    # END CONTENT STREAM
    context = {
        "Head"              :"Profile "+obj_user.username,
        "Judul"             :"TellBy",
        "cdn"               :"https://cdn.tell.by",
        "user_data"         :obj_user,
        "user_story"        :postingan_obj,
        "user_data_more"    :usr_more_print,
        "no_post"           :post_empty,
        "active"            :active,
        "active_pub"        :active_pub
    }
    if request.method == 'POST':
        if 'ajax.render' in request.POST:
            if request.POST.get('ajax.render') == 'profile.render':
                return render(request, 'ajax/profile.html', context)
            elif request.POST.get('ajax.render') == 'profile.sub.render':
                return render(request, 'ajax/profile_sub.html', context)
            elif request.POST.get('ajax.render') == 'profile.more.render':
                return render(request, 'components/profile_post_more.html', context)
            elif request.POST.get('ajax.render') == 'email.send.request':
                email = request.POST.get('emailConfirm')
                username = request.user.username
                ids = request.user.id
                Confirmation = ConfirmEmailSEND(email,username,ids)
                return Confirmation
            elif request.POST.get('ajax.render') == 'email.place.render':
                return render(request,'components/confirmEmail.html',{'active':active})
            elif request.POST.get('ajax.render') == 'profile.edit.modal':
                return render(request,'components/profile_edit_modal.html', context)
            else:
                return HttpResponse('0')
        else:
            return HttpResponse('0')
    else:
        return render(request, 'django/profile.html', context)


def profile_linktree(request, username, *args, **kwargs):
    #biography information
    obj_user        = User.objects.get(username=username)
    active_pub      = ActiveUser(obj_user.id)
    active          = ActiveUser(request.user.id)
    postingan_obj   = Postingan.objects.filter(user_id=obj_user.id).order_by('-id')
    post_obj_count  = postingan_obj.count()
    postingan_obj   = endlessPagination(request,postingan_obj,9)
    #check if post empty
    post_empty      = True
    if post_obj_count >= 1:
        post_empty  = False
    #kosong atau engga db nya
    usr_more_q      = User_more_info.objects.filter(user_id=obj_user.id)
    usr_more        = usr_more_q.count()
    usr_more_print  = False
    if usr_more:
        usr_more_print = User_more_info.objects.get(user_id=obj_user.id)

    usr_link_list   = ''
    usr_link        = User_LinkTree.objects.filter(user_id=obj_user.id).count()
    if usr_link:
        usr_link_list = User_LinkTree.objects.filter(user_id=obj_user.id).order_by('-order')

    # END CONTENT STREAM
    context = {
        "Head"              :"Link "+obj_user.username,
        "Judul"             :"TellBy",
        "cdn"               :"https://cdn.tell.by",
        "user_data"         :obj_user,
        "user_story"        :postingan_obj,
        "user_data_more"    :usr_more_print,
        "user_link"         :usr_link_list,
        "no_post"           :post_empty,
        "active"            :active,
        "active_pub"        :active_pub
    }
    if request.method == 'POST':
        if 'ajax.render' in request.POST:
            if request.POST.get('ajax.render') == 'profile.link.render':
                return render(request, 'ajax/profile_link.html',context)
            else:
                return HttpResponse('0')
        else:
            return HttpResponse('0')
    else:
        return render(request, 'django/profile_link.html', context)




#yang belum di convert ke render type!
def search_story(request, username, GetSearch):
    obj_user            = User.objects.get(username=username)
    postingan_objs      = Postingan.objects.filter(user_id=obj_user.id, content__contains=GetSearch).order_by('-id')
    postingan_obj       = endlessPagination(request,postingan_objs,9)
    #biography information
    usr_more            = User_more_info.objects.filter(user_id=obj_user.id).count()
    usr_more_print      = False
    if usr_more:
        usr_more_print  = User_more_info.objects.get(user_id=obj_user.id)
    #check ada gak
    post_obj_count      = postingan_objs.count()
    post_empty          = True
    if post_obj_count >= 1:
        post_empty      = False
    #check active user
    active              = ActiveUser(obj_user.id)

    # END CONTENT STREAM
    context = {
        "Head"          :"Search",
        "Judul"         :"TellBy",
        "cdn"           :"https://cdn.tell.by",
        "user_data"     :obj_user,
        "postingan_obj" :postingan_obj,
        "content_post"  :postingan_obj,
        "post_empty"    :post_empty,
        "more_info"     :usr_more_print,
        "active"        :active
    }
    if 'profile.search.render' in request.POST:
        return render(request, 'django/in_profile_search.html', context)

    return render(request, 'django/in_profile_search.html', context)

def search_profile(request, GetUsername):
    user_err = False
    if request.user.is_authenticated:
        #get user
        obj_user_fil    = User.objects.filter(username__contains=GetUsername).order_by('-id')
        list_user       = list(obj_user_fil)
        obj_user        = random.sample(list_user, len(list_user))
        #get page
        Contentuser     = endlessPagination(request,obj_user,9)
        #passing objects
        obj_user_count  = obj_user_fil.count()
        if obj_user_count == 0:
            user_err    = True

        active              = ActiveUser(request.user.id)
        # END CONTENT STREAM
        context = {
            "Head"      :"Search",
            "Judul"     :"TellBy",
            "cdn"       :"https://cdn.tell.by",
            "user_data" :Contentuser,
            "err"       :user_err,
            "query"     :GetUsername,
            "active"        :active
        }
        return render(request, 'global_profile_search.html', context)
    else:
        return redirect('/')



def edit_profile(request, username, *args, **kwargs):
    if request.user.is_authenticated:
        obj_user        = User.objects.get(username=username)
        active          = ActiveUser(request.user.id)
        is_not_active   = Inactive_user.objects.filter(user_id=request.user.id).count()
        if is_not_active:
            inactive    = True
        else:
            inactive    = False

        if request.method == 'POST':
            print('post edit')
            if request.POST.get('ajax.render') == 'username.change':
                print('active and not inactive')
                usr_nm = request.POST.get('username.change.input')
                if usr_nm and len(usr_nm) > 6:
                    #get safe param!
                    if re.match(r'^[a-z0-9_-]+$', usr_nm):
                        valids = User.objects.filter(username=usr_nm).count()
                        if valids == 0:
                            u = User.objects.get(id=request.user.id)
                            u.username = usr_nm
                            u.save()
                            return HttpResponse('1')
                        else:
                            return HttpResponse('0X2')
                    else:
                        return HttpResponse('0X3')
                else:
                    return HttpResponse('0X4')
            else:
                if active:
                    if request.POST.get('ajax.render')      == 'social.change':
                        print('social changed')
                        if frm_more.is_valid():
                            #handling bio more!
                            usr_more        = User_more_info.objects.filter(user_id=request.user.id).count()
                            if usr_more == 1:
                                usr_more = True
                            else:
                                usr_more = False
                            usr_io          = request.POST.get('social.bio')
                            usr_fb          = request.POST.get('social.facebook')
                            usr_tw          = request.POST.get('social.twitter')
                            usr_ig          = request.POST.get('social.instagram')
                            usr_gh          = request.POST.get('social.github')
                            usr_db          = request.POST.get('social.dribbble')

                            if usr_more == 0:
                                 #add to database!
                                if usr_io:
                                    #add to database
                                    u = User_more_info(user_id=request.user.id,bio=usr_io)
                                    u.save()
                                    return HttpResponse('1')

                            if usr_more == 1:
                                #update database!
                                if not usr_fb:
                                    usr_fb = '#'
                                if not usr_tw:
                                    usr_tw = '#'
                                if not usr_ig:
                                    usr_ig = '#'

                                u = User_more_info.objects.get(user_id=request.user.id)
                                u.bio       = usr_io
                                u.facebook  = usr_fb
                                u.twitter   = usr_tw
                                u.instagram = usr_ig
                                u.github    = usr_gh
                                u.dribbble  = usr_db
                                u.save()
                                return HttpResponse('1')
                    elif request.POST.get('ajax.render')    == 'ava.change':
                        print('change avatar')
                        URL         = 'https://cdn.tell.by/data.cgi@key=???' #remove secret key
                        myfile      = request.FILES.get('content.render')
                        sv_key      = {'secretkey' : '???','secret_username':request.user.username ,'secret_user_id': request.user.id } #remove secret key
                        files       = {'upfile' : myfile}
                        r           = requests.post(URL,data=sv_key, files = files)
                        img_success = True
                        return HttpResponse('1')
                    elif request.POST.get('ajax.render')    == 'social.change':
                        print('social change')
                    else:
                        return HttpResponse('%')
                else:
                    return HttpResponse('$')
        else:
            return redirect('/'+username+'/')

        if request.user.username == username:
            av_form         = AvatarForm()
            frm_more        = MoreInfoForm(request.POST or None)
            #biography information
            img_success     = False
            usr_edit_err    = False
            usr_nm          = ''
            usr_em          = ''
            usr_link_list   = ''
            usr_link        = User_LinkTree.objects.filter(user_id=request.user.id).count()
            usr_more_print  = False

            if usr_link:
                usr_link_list = User_LinkTree.objects.filter(user_id=request.user.id).order_by('-order')

            if usr_more:
                usr_more_print = User_more_info.objects.get(user_id=request.user.id)

            if 'everif' in request.POST:
                verif_email         = request.POST.get('email')
                verif_uname         = request.user.username
                verif_uid           = request.user.id
                return ConfirmEmailSEND(verif_email,verif_uname,verif_uid)

            if 'aedit' in request.POST:
                URL         = 'https://cdn.tell.by/data.cgi@key=???' #remove secret key
                myfile      = request.FILES.get('avatar2')
                sv_key      = {'secretkey' : '???','secret_username':request.user.username ,'secret_user_id': request.user.id } #remove secret key
                files       = {'upfile' : myfile}
                r           = requests.post(URL,data=sv_key, files = files)
                img_success = True

            #add link tree!
            if 'ledit' in request.POST:
                Link_img     = request.POST.get('Linked_img')
                if not Link_img:
                    Link_img = 'https://cdn.tell.by/img/icon/fields.svg'

                Link_url = request.POST.get('Linked_url')
                Link_val = request.POST.get('Linked_val')
                Link_ord = request.POST.get('Linked_ord')
                Link_des = request.POST.get('Linked_des')
                if Link_val:
                    mockUrl_data    = request.user.id + random.getrandbits(128), "-url-", request.user.username, Link_val, Link_url
                    mockUrl_hash    = sha1(str(mockUrl_data).encode("UTF-8")).hexdigest()[:35]
                    lt              = User_LinkTree(user_id=request.user.id, mock=mockUrl_hash, img=Link_img, link=Link_url, desc=Link_des, title=Link_val, order=Link_ord)
                    lt.save()
                    return HttpResponse('0')

            if 'dellink' in request.POST:
                del_link_key        = request.POST.get('dellink')
                del_link_confirm    = User_LinkTree.objects.filter(user_id=request.user.id,mock=del_link_key).count()
                if del_link_confirm == 1:
                    User_LinkTree.objects.get(mock=del_link_key).delete()
                    User_LinkTree.objects.all()
                    return HttpResponse('0')

            #proccess the edit!
            if 'pedit' in request.POST:
                usr_nm = request.POST.get('username')
                usr_em = request.POST.get('email')
                if usr_nm and len(usr_nm) > 6:
                    #get safe param!
                    if re.match(r'^[a-z0-9_-]+$', usr_nm):
                        valids = User.objects.filter(username=usr_nm).count()
                        if valids == 0:
                            u = User.objects.get(id=request.user.id)
                            u.username = usr_nm
                            u.save()
                            return HttpResponse('1')
                        else:
                            return HttpResponse('0')
                    else:
                        return HttpResponse('0')
                else:
                    return HttpResponse('0')

                if usr_em:
                    valids = User.objects.filter(email=usr_em).count()
                    if valids == 0:
                        ue = User.objects.get(id=request.user.id)
                        ue.email = usr_em
                        ue.save()
                        dl = active_user.objects.get(user_id=request.user.id)
                        dl.delete()
                        return HttpResponse('1')
                    else:
                        return HttpResponse('0')

            elif 'sedit' in request.POST:
                if frm_more.is_valid():
                    #handling bio more!
                    usr_io = request.POST.get('bio')
                    usr_fb = request.POST.get('facebook')
                    usr_tw = request.POST.get('twitter')
                    usr_ig = request.POST.get('instagram')

                    if usr_more == 0:
                        #add to database!
                        if usr_io:
                            #add to database
                            u = User_more_info(user_id=request.user.id,bio=usr_io)
                            u.save()
                            return HttpResponse('1')

                    if usr_more == 1:
                        #update database!
                        if not usr_fb:
                            usr_fb = '#'
                        if not usr_tw:
                            usr_tw = '#'
                        if not usr_ig:
                            usr_ig = '#'

                        u = User_more_info.objects.get(user_id=request.user.id)
                        u.bio       = usr_io
                        u.facebook  = usr_fb
                        u.twitter   = usr_tw
                        u.instagram = usr_ig
                        u.save()
                        return HttpResponse('1')

            # processing the view
            context = {
                "Head"          :"Edit Profile",
                "Judul"         :"TellBy",
                "cdn"           :"https://cdn.tell.by",
                "user_data"     :obj_user,
                "more_info"     :usr_more_print,
                "usr_edit_err"  :usr_edit_err,
                "usr_edit_nm"   :usr_nm,
                "usr_edit_em"   :usr_em,
                "av_form"       :av_form,
                "linktree"      :usr_link_list,
                "img_success"   :img_success,
                "usr_more"      :usr_more,
                "active"        :active,
                "inactive"      :inactive
            }
            if 'ajax.render' in request.POST:
                if request.POST.get('ajax.render') == 'profile.edit.render':
                    return render(request, 'ajax/in_profile_edit.html',context)

            return render(request, 'django/in_profile_edit.html',context)
        else:
            return redirect('/'+username,sep='')
    else:
        return redirect('/')

