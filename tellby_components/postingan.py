import random
import requests
import collections
import re
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def endlessPagination(request,content_object,page_per_load):
    paginator = Paginator(content_object, page_per_load)
    page = request.POST.get('p', 1)
    #?p=1
    try:
        content_object = paginator.get_page(page)
        return content_object
    except PageNotAnInteger:
        content_object = paginator.get_page(1)
        return content_object
    except EmptyPage:
        content_object = paginator.get_page(paginator.num_pages)
        return content_object