import random
import requests
import collections
import re
from django.contrib.auth import get_user_model

def CommonWord(tipe,howmany):
    link = "https://cdn.tell.by/get.php?commonword="+tipe
    f = requests.get(link)
    common_hashtag = f.text
    words = re.findall(r'\w+', common_hashtag.lower())
    if 'Xall' in tipe:
        most_common = collections.Counter(words)
    else:
        most_common = collections.Counter(words).most_common(howmany)
    return most_common

def RandomUser():
    User = get_user_model()
    #get random user recomendation
    UserCount = User.objects.all().count()
    res = [random.randrange(1, UserCount, 1) for i in range(20)]
    UserRecom = User.objects.filter(id__in=res)
    return UserRecom