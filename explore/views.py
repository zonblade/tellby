from django.shortcuts               import render, redirect
from django.contrib.auth.models     import User
from postingan.models               import Postingan
from gallery.models                 import Image_Gallery
from tellby_components.home         import CommonWord, RandomUser
from tellby_components.verification import ActiveUser
from tellby_components.postingan    import endlessPagination

# Create your views here.
def explore(request, *args, **kwargs):
    if request.user.is_authenticated:
        context = {
            "Head"  :"Explore",
            "Judul" :"TellBy",
            "cdn"   :"https://cdn.tell.by",
        }
        return redirect('/')
    else:
        return redirect('/')

#IMAGE EXPLORE
def explore_images(request, *args, **kwargs):
    if request.user.is_authenticated:
        IMGG_Result_Q   = Image_Gallery.objects.filter().order_by('?')
        IMGG_Result     = endlessPagination(request,IMGG_Result_Q,12)
        most_common         = CommonWord('alltime',10)
        most_common_m       = CommonWord('month',10)
        most_common_c       = len(CommonWord('Xall',0))
        UserRecom       = RandomUser()
        active          = ActiveUser(request.user.id)
        context = {
            "Head"            :"Explore Images",
            "Judul"           :"TellBy",
            "cdn"             :"https://cdn.tell.by",
            "IMGG_Result"     :IMGG_Result,
            "UserRecom"       :UserRecom,
            "popular_hashtag" :most_common,
            "month_hashtag"   :most_common_m,
            "active"          :active
        }
        if 'ajax.render' in request.POST:
            if request.POST.get('ajax.render') == 'explore.home.image':
                return render(request,'ajax/explore_img.html',context)

            if request.POST.get('ajax.render') == 'explore.home.image.more':
                return render(request,'content/explore_img_more.html',context)

        return render(request,'django/explore_img.html',context)
    else:
        return redirect('/')

#SEARCH HASHTAG
def search_hashtag(request, GethashTag):
    if request.user.is_authenticated:
        most_common         = CommonWord('alltime',10)
        most_common_m       = CommonWord('month',10)
        most_common_c       = len(CommonWord('Xall',0))
        UserRecom   = RandomUser()
        active      = ActiveUser(request.user.id)
        #getting hashtag content
        GetHasTG                = str('#' + GethashTag)
        ContentPostingan        = Postingan.objects.filter(content__contains=GetHasTG).order_by('-id')
        ContentPostinganCount   = ContentPostingan.count()
        ContentPostingan        = endlessPagination(request,ContentPostingan,9)
        #getting hashtag value
        user_err        = False
        if ContentPostinganCount == 0:
            user_err    = True
        #?p=1
        context = {
            "Head"              :GethashTag,
            "Judul"             :"TellBy",
            "cdn"               :"https://cdn.tell.by",
            "post_user"         :User,
            "content_post"      :ContentPostingan,
            "err"               :user_err,
            "query"             :GethashTag,
            "UserRecom"         :UserRecom,
            "popular_hashtag"   :most_common,
            "month_hashtag"     :most_common_m,
            "active"            :active
        }

        if 'ajax.render' in request.POST:
            if request.POST.get('ajax.render') == 'hashtag.popular':
                return render(request,'ajax/explore_hashtag.html',context)

        return render(request,'django/explore_hashtag.html',context)
    else:
        return redirect('/')