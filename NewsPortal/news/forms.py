from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["post_author"].empty_label = "Выберите автора"

    class Meta:
        model = Post
        fields = ["post_author", "post_header", "post_content", "post_categories"]
        labels = {
            "post_author": "Автор",
            "post_header": "Заголовок",
            "post_content": "Содержание",
            "post_categories": "Категория"
        }
        widgets = {"post_content": forms.Textarea(attrs={'class': 'form-textarea', 'rows': 5, 'cols': 38})}