from celery import shared_task
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from .models import Post, User, Category
from django.utils import timezone
from datetime import timedelta


@shared_task()
def subscribers_notification_task(pk,content,username,**params):
        html_content = render_to_string(
            'news/subscribers_notification.html',
            {
                'user': username,
                'text': content,
                'link': f'{settings.SITE_URL}/post/{pk}',
                }
            )

        msg = EmailMultiAlternatives(**params)
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@shared_task()
def weekly_notification_task():
    last_week = timezone.now() - timedelta(days=7)
    posts = Post.objects.filter(post_date__gte=last_week)
    categories = posts.values_list('post_categories__category_name', flat=True)
    subscribers = Category.objects.filter(category_name__in=categories).values_list('subscribers', flat=True)
    subscribers_ids = set(filter(lambda x: x is not None, subscribers))

    for user in User.objects.filter(pk__in=subscribers_ids):
        html_content = render_to_string(
            'news/weekly_notification.html',
            {
                'user': user.username,
                'posts': filter(lambda x: x.post_categories.all().filter(pk__in=user.categories.all()).exists(), posts),
                'link': settings.SITE_URL,
            }
        )

        msg = EmailMultiAlternatives(
            subject='Публикации за прошедшую неделю',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )

        msg.attach_alternative(html_content, 'text/html')
        msg.send()