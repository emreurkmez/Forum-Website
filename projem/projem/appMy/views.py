from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .models import Post
from django.contrib.auth import logout
from .forms import ContentForm
from .models import Content
from .models import News,Profile
from .forms import ProfileForm
import random

def indexPage(request):
    new_news = News.objects.all()

    news_with_profile = []
    for news_item in new_news:
        profile_photo_url = '/static/default_profile_photo.png'  # Varsayılan profil fotoğrafı URL
        if news_item.user_name:
            try:
                profile = Profile.objects.get(user__username=news_item.user_name)
                profile_photo_url = profile.profile_photo.url if profile.profile_photo else '/static/default_profile_photo.png'
            except Profile.DoesNotExist:
                pass
        
        news_with_profile.append({
            'news': news_item,
            'profile_photo_url': profile_photo_url,
        })

    context = {
        'news_with_profile': news_with_profile,
    }

    return render(request, 'index.html', context)


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
        if User.objects.filter(username=username).exists():
            username_bool = False
            messages.warning(request, "Bu kullanıcı adı zaten kullanılıyor!")
        if User.objects.filter(email=email).exists():
            email_bool = False
            messages.warning(request, "Bu email zaten başkası tarafından kullanılıyor!")
         
        if password_bool and email_bool and username_bool:
            user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username, password=password1)
            user.save()
            
            # Profil fotoğrafını kaydetmek için profil formunu kullanın
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = user  # Kullanıcıyı bağlayın
                profile.save()
                
            return redirect("loginUser")
      
    else:
        form = ProfileForm()
        
    context['form'] = form
    return render(request, 'register.html', context)
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

def content_list(request):
    content = Content.objects.all()
    return render(request, 'content_list.html', {'content': content})

def create_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('create_content_success')
    else:
        form = ContentForm()

    content_list = Content.objects.all()
    return render(request, 'create_content.html', {'form': form, 'content_list': content_list})

def create_content_success(request):
    return render(request, 'create_content_success.html')  
 
def new_news(request):
    new_news = News.objects.all().order_by('-id')[:10]
    return render(request, 'index.html', {'new_news': new_news})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'index.html', {'news': news})
 
def my_view(request):
    news_list = News.objects.all()
    return render(request, 'index.html', {'news_list': news_list}) 

