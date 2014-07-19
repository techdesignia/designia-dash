# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages 

def site_render(request,page,tv):
    if not request.user.is_authenticated():
        messages.error(request,'Please login!')
        return redirect('login')
    return render(request,page,tv)

def home(request):
    print request.user.is_authenticated()
    tv = {}
    return render(request,'common-index.html',tv)
