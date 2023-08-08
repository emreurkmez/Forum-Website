from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='content_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    topic_count = models.PositiveIntegerField(default=0)
    post_count = models.PositiveIntegerField(default=0)
    response_date = models.DateTimeField(null=True, blank=True)
    user_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

   
