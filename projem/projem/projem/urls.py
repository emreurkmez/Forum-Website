"""
URL configuration for projem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appMy.views import *
from django.conf.urls.static import static
from django.conf import settings
from appUser.views import *
from appMy import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexPage, name='indexPage'),
    path('login',loginUser ,name='loginUser'),
    path('register',registerUser ,name='registerUser'),
    path('welcome',welcome ,name='welcome'),
    path('search/', views.search_results, name='search_results'),
    path('logout/', views.user_logout, name='logout'),
    path('', include('appMy.urls')),
    path('create_content/', views.create_content, name='create_content'),
    path('create_content_success/', views.create_content_success, name='create_content_success'),
    path('new_news/', views.new_news, name='new_news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
