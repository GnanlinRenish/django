from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect ('app')
        else:
            return render(request,'login.html',{'error':'error'})
    else:
        return render(request,'login.html')