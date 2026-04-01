import random
from .models import Post
from django import forms

post_types = ['A','N']

authors_id = [3, 4, 5]

def gen_posts():
    for i in range(4, 50):
        kwargs = {
            "post_author_id": random.choice(authors_id),
            "article_news": random.choice(post_types),
            "post_header": f"Заголовок поста{i}",
            "post_content": f"Содержание поста{i}"}
        Post.objects.create(**kwargs)

    print("Успешно")


def create_or_edit(context, request_path):
    if "create" in request_path:
        title = "Добавить "
    else:
        title = "Редактировать "
    if "news" in request_path:
        title += "новость"
    else:
        title += "статью"

    context['create_or_edit'] = title
    return context


