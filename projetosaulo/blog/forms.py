from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'summary', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-title'}),
            'summary': forms.Textarea(attrs={'class': 'form-summary'}),
            'content': forms.Textarea(attrs={'class': 'form-content'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-file'}),
        }
    
        labels = {
            'title': 'Título',
            'summary': 'Resumo',
            'content': 'Conteúdo',
            'image': 'Imagem',
        }
