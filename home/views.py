from django.shortcuts               import render, redirect
from postingan.models               import Postingan
from django.contrib.auth.models     import User
from tellby_components.home         import CommonWord, RandomUser
from tellby_components.verification import ActiveUser
from tellby_components.postingan    import endlessPagination
from django.http                    import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    most_common         = CommonWord('alltime',10)
    most_common_m       = CommonWord('month',10)
    most_common_c       = len(CommonWord('Xall',0))
    UserRecom           = RandomUser()
    UserRecent          = User.objects.filter().order_by('-id')[:12]
    PostinganCount      = Postingan.objects.all().count()
    PostinganPopAll     = Postingan.objects.all().order_by('-post_seen')[:3]
    UserCount           = User.objects.all().count()
    if request.user.is_authenticated:
        active              = ActiveUser(request.user.id)
        #content processing!
        ContentPostingan    = Postingan.objects.all().order_by('-id')
        numbers             = endlessPagination(request,ContentPostingan,9)

        context = {
            "Head"            :"Home",
            "Judul"           :"TellBy",
            "cdn"             :"https://cdn.tell.by",
            "post_user"       :User,
            "UserRecom"       :UserRecom,
            'numbers'         :numbers,
            "popular_hashtag" :most_common,
            "month_hashtag"   :most_common_m,
            "PostinganCount"  :PostinganCount,
            "active"          :active
        }
        if request.method == 'POST':
            if 'ajax.render' in request.POST:
                if request.POST.get('ajax.render') == 'more.posts':
                    return render(request,'content/home_post.html',context)
                elif request.POST.get('ajax.render') == 'home.menu.more.posts':
                    return render(request,'content/home_post_menu.html',context)
                elif request.POST.get('ajax.render') == 'home.render':
                    return render(request,'ajax/home_2.html',context)
                elif request.POST.get('ajax.render') == 'story.create.render':
                    return render(request,'content/home_rightcon_create.html',context)
                else:
                    return HttpResponse('0')
            else:
                return HttpResponse('0')
        else:
            return render(request,'django/home_2.html',context)
    else:
        ContentPostingan    = Postingan.objects.all().order_by('-id')
        numbers             = endlessPagination(request,ContentPostingan,3)
        context = {
            "Head"            :"Home",
            "Judul"           :"TellBy",
            "cdn"             :"https://cdn.tell.by",
            "post_user"       :User,
            "UserRecom"       :UserRecent,
            'numbers'         :numbers,
            "popular_hashtag" :most_common,
            "month_hashtag"   :most_common_m,
            "UserCount"       :UserCount,
            "PostinganCount"  :PostinganCount,
            "PostinganPopAll" :PostinganPopAll,
            "most_common_c"   :most_common_c
        }
        return render(request,'home_public.html',context)
    #return render(request,'home_public.html',context)

def home_public(request):
    UserCount = User.objects.all().count()
    PostinganCount = Postingan.objects.all().count()
    context = {
        "Head"            :"Home",
        "Judul"           :"TellBy",
        "cdn"             :"https://cdn.tell.by",
        "UserCount"       :UserCount,
        "PostinganCount"  :PostinganCount
    }
    return render(request,'home_public.html',context)