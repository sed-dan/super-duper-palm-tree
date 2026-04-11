from datetime import timedelta
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from django.db.models.signals import pre_save, m2m_changed
from django.dispatch import receiver
from .models import Post, User, Category
from django.conf import settings
from django.template.loader import render_to_string


@receiver(pre_save, sender=Post)
def post_limit(sender, instance, *args, **kwargs):
    if instance.pk:
        return
    before_datetime = timezone.now() - timedelta(days=1)
    posts_count = Post.objects.filter(post_author=instance.post_author, post_date__gte=before_datetime).count()
    if posts_count >= 3:
        raise PermissionDenied('Вы не можете создавать более 3-х публикаций в сутки!')


@receiver(m2m_changed, sender=Post.post_categories.through)
def subscribers_notification(sender, instance, action, **kwargs):
    if action == 'post_add':
        categories = instance.post_categories.values_list('category_name', flat=True)
        subscribers = Category.objects.filter(category_name__in=categories).values_list('subscribers', flat=True)
        for user in User.objects.filter(pk__in=subscribers):
            html_content = render_to_string(
                'news/subscribers_notification.html',
                {
                    'user': user.username,
                    'text': instance.post_content,
                    'link': f'{settings.SITE_URL}/post/{instance.pk}',
                }
            )

            msg = EmailMultiAlternatives(
                subject=f'{instance.post_header}',
                body='',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user.email],
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()