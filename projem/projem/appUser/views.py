from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
import random

def loginUser(request):
   context = {}
   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      
      user = authenticate(username=username, password=password) # kullanıcı varsa kullanıcı adını yoksa None değeri döndürür
      # if user != None:
      if user is not None:
         login(request, user)
         return redirect('welcome')
      else:
         # context.update({"hata":"kullanıcı adı veya şifre yanlış!"})
         messages.warning(request, "Kullanıcı adı veya şifre yanlış!")
         return redirect('loginUser')      
      
   
   return render(request, 'login.html',context)