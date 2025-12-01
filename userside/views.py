from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from userside.models import Userprofile
import random

from userside.models import Userprofile


def userdashboard(request):
    return render(request, "user_index.html")


def user_register_page(request):
    return render(request, "user_register.html")


def user_login_page(request):
    return render(request, "user_login.html")


def saveuser(request):
    if request.method == "POST":
        uname = request.POST.get('Uname')
        phone = request.POST.get('Mob_no')
        email = request.POST.get('Email')
        password = request.POST.get('pwd')
        if User.objects.filter(username=uname).exists():
            messages.error(request, "username already exists")
            return redirect(user_register_page)
        user = User.objects.create_user(username=uname, password=password, email=email)
        Userprofile.objects.create(user=user, phone=phone, email=email)
        messages.success(request, "Registeration is successfull ! please login")
        return redirect(user_login_page)

    return render(request, "user_register.html")
def loginUser(request):
    if request.method=="POST":
        uname=request.POST.get('U_name')
        password=request.POST.get('Pass_word')
        user=authenticate(username=uname,password=password)
        if user is not None:
            request.session['U_name']=uname
            request.session['Pass_word']=password
            login(request,user)
            messages.success(request,"login successfull")
            return redirect(userdashboard)
        else:
            messages.error(request,"Invalid username or password")
            return redirect(user_login_page)
    return redirect(user_login_page)