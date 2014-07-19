# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages 

def site_render(request,page,tv):
    if not request.user.is_authenticated():
        messages.error(request,'Please login!')
        return render(request,'common-login.html',{})
    return render(request,page,tv)

def home(request):
    
    tv = {}
    return site_render(request,'common-index.html',tv)
