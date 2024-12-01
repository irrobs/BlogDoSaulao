from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'show_image')

    def show_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50"/>'
        return "No Image"
    show_image.allow_tags = True  # Necessário para renderizar HTML no admin
    show_image.short_description = "Imagem"

admin.site.register(Post, PostAdmin)

