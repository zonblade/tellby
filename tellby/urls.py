"""tellby URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import home_view, home_public
from register.views import register
from postingan.views import postingan_view, postingan_create, postingan_edit, postingan_delete
from profil.views import user_profile, search_story, search_profile, edit_profile, profile_linktree
from explore.views import explore, search_hashtag, explore_images
from pages.views import page_404
from gallery.views import image_gallery
from verification.views import verification

handler404 = page_404
handler403 = page_404
handler503 = page_404
handler500 = page_404

urlpatterns = [
    path('', home_view, name='home'),
    path('hm/', home_public),
    path('auth/daftar/', register),
    path('auth/', include('django.contrib.auth.urls')),
    #path('messages/', include('obrolan.urls')),
    path('verify/<slug:key>/', verification),
    path('mix-max-tools/', admin.site.urls),
    path('explore/', explore, name="explore"),
    path('explore/images/', explore_images, name="explore_images"),
    path('explore/<slug:GetUsername>/user/', search_profile),
    path('explore/<slug:GethashTag>/hashtag/', search_hashtag),
    path('p/create/', postingan_create),
    path('p/<slug:GETmock_url>/', postingan_view),
    path('p/<slug:GETmock_url>/edit/', postingan_edit),
    path('p/<slug:GETmock_url>/delete/', postingan_delete),
    path('<slug:username>/', user_profile, name='profile_main'),
    path('<slug:username>/link/', profile_linktree),
    path('<slug:username>/gallery/', image_gallery),
    path('<slug:username>/edit/', edit_profile, name='profile_edit'),
    path('<slug:username>/search/<slug:GetSearch>/', search_story),
]
