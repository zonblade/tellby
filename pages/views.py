from django.shortcuts import render
from django.http      import HttpResponse
from tellby_components.verification import ActiveUser

# Create your views here.
def page_404(request, *args, **kwargs):
    active              = ActiveUser(request.user.id)
    context = {
        "Head":"OOPPPSSS",
        "Judul":"TellBy",
        "cdn":"https://cdn.tell.by",
        "active":active
    }
    if request.POST:
        return HttpResponse('0')
    else:
        return render(request,'404.html',context)