from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255, default="Unnamed")
    summary = RichTextField(max_length=100 ,default="No summary provided")  # Adiciona um valor padrão
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title