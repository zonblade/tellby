import random
import bleach
#from bleach_allowlist import print_tags, print_attrs, all_styles
from itertools                      import chain
from datetime                       import datetime
from hashlib                        import md5, sha1
from django.shortcuts               import render, redirect
from django.contrib.auth.models     import User
from django.http                    import HttpResponse
from throttle.decorators            import throttle
from .models                        import Postingan, Komentar
from .forms                         import PostinganForm, KomenForm
from tellby_components.home         import CommonWord, RandomUser
from tellby_components.verification import ActiveUser
from tellby_components.postingan    import endlessPagination
from tellby_components.bleach_list  import print_tags, print_attrs, all_styles

# Create your views here.
@throttle(zone='default')
def postingan_delete(request, GETmock_url):
    active              = ActiveUser(request.user.id)
    if request.POST:
        if request.user.is_authenticated:
            if active:
                if 'ajax.render' in request.POST:
                    if request.POST.get('ajax.render') == 'story.delete':
                        ContentPostingan = Postingan.objects.get(mock_url=GETmock_url)
                        if ContentPostingan:
                            UserStarter = User.objects.get(id=ContentPostingan.user_id)
                            if request.user.id == UserStarter.id:
                                p_d = Postingan.objects.get(mock_url=GETmock_url)
                                p_d.delete()
                                Postingan.objects.all()
                                Komentar.objects.filter(post_id=ContentPostingan.id).delete()
                                Komentar.objects.all()
                                return render(request, 'ajax/delete_post_success.html', {})
                            else:
                                return HttpResponse('0')
                        else:
                            return HttpResponse('0')
                    else:
                        return HttpResponse('0')
                else:
                    return HttpResponse('0')
            else:
                return HttpResponse('0')
        else:
            return HttpResponse('0')
    else:
        return redirect('/p/'+GETmock_url,sep='')



def postingan_edit(request, GETmock_url):
    if request.user.is_authenticated:
        active              = ActiveUser(request.user.id)
        ContentPostingan    = Postingan.objects.get(mock_url=GETmock_url)
        UserStarter         = User.objects.get(id=ContentPostingan.user_id)
        empty_err           = False
        formPostingan       = PostinganForm(request.POST or None)
        if active:
            if request.POST.get('ajax.render') == 'story.edit.change':
                if 'ajax.render' in request.POST:
                    if request.user.id == UserStarter.id:
                        if formPostingan.is_valid():
                            conPostingan    = request.POST.get('content')
                            conTitle        = request.POST.get('content-title')
                            conKeyword      = request.POST.get('content-keyword')
                            if not conTitle:
                                conTitle    = 'Story'
                            if not conKeyword:
                                conKeyword  = 'Tell By '+ request.user.username +'//Story'
                            if conPostingan:
                                ContentPostingan    = Postingan.objects.get(mock_url=GETmock_url)
                                UserStarter         = User.objects.get(id=ContentPostingan.user_id)
                                if request.user.id == UserStarter.id:
                                    b               = Postingan.objects.get(mock_url=GETmock_url)
                                    b.content       = bleach.clean(conPostingan, print_tags, print_attrs, all_styles)
                                    b.post_title    = conTitle
                                    b.post_keyword  = conKeyword
                                    b.save()
                                    formPostingan   = PostinganForm()
                                    return HttpResponse('1')
                            else:
                                return HttpResponse('0')
                        else:
                            return HttpResponse('0')
                    else:
                        return HttpResponse('0')
                else:
                    return HttpResponse('0')

            content_sanitize = bleach.clean(ContentPostingan.content, print_tags, print_attrs, all_styles)
            context = {
                "Head"      :"Edit Story",
                "Judul"     :"TellBy",
                "cdn"       :"https://cdn.tell.by",
                "form"      :formPostingan,
                "konten"    :ContentPostingan,
                "konten_sanitize":content_sanitize,
                "empty_err" :empty_err
            }
            if 'ajax.render' in request.POST:
                if request.POST.get('ajax.render') == 'story.edit.nochange':
                    return render(request, 'ajax/edit_post_ots.html', context)

            return redirect('/p/'+GETmock_url,sep='')
        else:
            return HttpResponse('0')
    else:
        return HttpResponse('0')



def postingan_view(request, GETmock_url):
    ContentPostingan    = Postingan.objects.get(mock_url=GETmock_url)
    active              = ActiveUser(ContentPostingan.user_id)
    UserStarter         = User.objects.get(id=ContentPostingan.user_id)
    Komentar_obj        = Komentar.objects.filter(post_id=ContentPostingan.id).order_by('-id')
    Komentar_obj        = endlessPagination(request,Komentar_obj,4)
    komen_err           = False
    story_gone          = False

    if ContentPostingan.user_id != request.user.id and request.user.is_authenticated:
        update_seen             = Postingan.objects.get(pk = ContentPostingan.id)
        update_seen.post_seen   = ContentPostingan.post_seen + 1
        update_seen.save()

    if request.user.is_authenticated:
        formKomen   = KomenForm(request.POST or None)
        komen_auth  = False
        komen_err   = False
        komen_auth  = request.POST.get('helvetica')
        if 'komen' in request.POST:
            if not komen_auth:
                if formKomen.is_valid():
                    conKomen = request.POST.get('komen')
                    if conKomen:
                        conKomen    = bleach.clean(conKomen, print_tags, print_attrs, all_styles)
                        k           = Komentar(user_id=request.user.id, post_id=ContentPostingan.id, komen=conKomen)
                        k.save()
                        formKomen   = KomenForm()
                        return HttpResponse('1')
                    else:
                        return HttpResponse('0')
                else:
                    return HttpResponse('0')
            else:
                return HttpResponse('0')

    content_sanitize = bleach.clean(ContentPostingan.content, print_tags, print_attrs, all_styles)

    context = {
        "Head"          :ContentPostingan.post_title,
        "Judul"         :"TellBy",
        "cdn"           :"https://cdn.tell.by",
        "StoryKey"      :ContentPostingan.post_keyword,
        "StoryDesc"     :ContentPostingan.content,
        "user_post"     :UserStarter,
        "content_post"  :ContentPostingan,
        "content_sanitize":content_sanitize,
        "komentar"      :Komentar_obj,
        "story_gone"    :story_gone,
        "komen_err"     :komen_err,
        "active"        :active
    }

    if request.method == 'POST':
        if 'ajax.render' in request.POST:
            if request.POST.get('ajax.render') == 'story.view.render':
                return render(request, 'ajax/postingan.html', context)
            if request.POST.get('ajax.render') == 'story.comment.render':
                return render(request, 'ajax/komen_postingan.html', context)
            else:
                return HttpResponse('0')
        else:
            return HttpResponse('0')
    else:
        return render(request, 'django/postingan.html', context)



def postingan_create(request, *args, **kwargs):
    # postingan MOCK URL
    if request.user.is_authenticated:
        #INPUT CONTENT TO DATABASE!
        active          = ActiveUser(request.user.id)
        formPostingan   = PostinganForm(request.POST or None)
        mockUrl_data    = request.user.id + random.getrandbits(128), "-postingan-", request.user.username
        mockUrl_hash    = sha1(str(mockUrl_data).encode("UTF-8")).hexdigest()[:15]
        print(mockUrl_hash)

        context = {
            "Head"          :"Buat Story",
            "Judul"         :"TellBy",
            "cdn"           :"https://cdn.tell.by",
            "active"        :active
        }
        empty_err = False
        if request.method == 'POST':
            if active:
                if request.POST.get('ajax.render') == 'story.create':
                    if formPostingan.is_valid():
                        conPostingan    = request.POST.get('content')
                        conTitle        = request.POST.get('content-title')
                        conKeyword      = request.POST.get('content-keyword')
                        if not conTitle:
                            conTitle    = 'Story'
                        if not conKeyword:
                            conKeyword  = 'Tell By '+ request.user.username +'//Story'
                        if conPostingan:
                            conPostingan    = bleach.clean(conPostingan, print_tags, print_attrs, all_styles)
                            b               = Postingan(user_id=request.user.id, mock_url=mockUrl_hash, post_title=conTitle, post_keyword=conKeyword, content=conPostingan)
                            b.save()
                            formPostingan   = PostinganForm()
                            print('3LL:'+mockUrl_hash)
                            return HttpResponse('3LL:'+mockUrl_hash)
                        else:
                            return HttpResponse('0')
                    else:
                        return HttpResponse('0')
                elif request.POST.get('ajax.render') == 'story.page.create':
                    return render(request, 'ajax/buat_postingan.html', context)
                else:
                    return HttpResponse('0')
            else:
                return HttpResponse('9')
        else:
            if active:
                return render(request, 'django/buat_postingan.html', context)
            else:
                return redirect('/')
    else:
        return redirect('/')