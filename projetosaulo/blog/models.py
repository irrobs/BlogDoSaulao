from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    likes= models.ManyToManyField(User, related_name="post_like", blank=True)

    # Keep track of like cont
    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
