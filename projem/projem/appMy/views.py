from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .models import Post
from django.contrib.auth import logout
from .models import Category, Post
from .forms import PostForm




import random
def indexPage(request):
   context = {}
   return render(request, 'index.html',context)

# LOGİN START
def loginUser(request):
   context = {}
   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      
      user = authenticate(username=username, password=password) 
      if user is not None:
         login(request, user)
         
         if user.userinfo.subscribe:
            return redirect("profileUser")
         
         return redirect('subscribeUser')
      else:
         
         messages.warning(request, "Kullanıcı adı veya şifre yanlış!")
         return redirect('loginUser')      
      
   
   return render(request, 'login.html',context)
# LOGİN END

# REGİSTER START

def registerUser(request):
   context = {}
   
   if request.method == "POST":
      fname = request.POST.get("fname")
      lname = request.POST.get("lname")
      email = request.POST.get("email")
      username = request.POST.get("username")
      password1 = request.POST.get("password1")
      password2 = request.POST.get("password2")
      
      password_bool = email_bool = username_bool = True 
      if password1 != password2:
         password_bool = False
         messages.warning(request, "Şifreler aynı değil!")
      if User.objects.filter(username=username).exists(): # exists list içinde obje varsa True yoksa False döndürür
         username_bool = False
         messages.warning(request, "Bu kullanıcı adı zaten kullanılıyor!")
      if User.objects.filter(email=email).exists(): # exists liste içerisi boşsa None döndürür
         email_bool = False
         messages.warning(request, "bu email zaten başkası tarafından kullanılmış!")
         
      if password_bool and email_bool and username_bool:
         user = User.objects.create_user(first_name = fname, last_name=lname, email=email, username=username, password=password1) # obje oluştur
         user.save() # objeyi yani kullanıcıyı kaydet
         return redirect("loginUser")
      
      
   return render(request, 'register.html',context)
# REGİSTER END

# WELCOME START
def welcome(request):
   context = {}
   return render(request, 'welcome.html',context)
   
# WELCOME END

def search_results(request):
    search_term = request.GET.get('q')
    results = Post.objects.filter(title__icontains=search_term)
    return render(request, 'search_results.html', {'results': results})
 
#  logoutstart
def user_logout(request):
    logout(request)
    return redirect('indexPage')
#  logoutend

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('forum_home')  # Forum anasayfasına yönlendir
    else:
        form = PostForm()
    return render(request, 'forum_app/create_post.html', {'form': form})