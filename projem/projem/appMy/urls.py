from django.urls import path
from . import views

urlpatterns = [
    path('content/', views.content_list, name='content_list'),
    path('create/', views.create_content, name='create_content'),
]
