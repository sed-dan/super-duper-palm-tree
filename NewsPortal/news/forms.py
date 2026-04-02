from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["post_header", "post_content", "post_categories"]
        labels = {
            "post_header": "Заголовок",
            "post_content": "Содержание",
            "post_categories": "Категория"
        }
        widgets = {"post_content": forms.Textarea(attrs={'class': 'form-textarea', 'rows': 5, 'cols': 38})}