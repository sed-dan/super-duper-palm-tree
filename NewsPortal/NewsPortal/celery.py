import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')

app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.conf.update(
    CELERY_TIMEZONE='UTC',
    CELERYD_POOL='solo',
)

app.conf.beat_schedule = {
    'weekly_notification_at_monday_8am': {
        'task': 'news.tasks.weekly_notification_task',
        'schedule': crontab(minute=0, hour=8, day_of_week='monday'),
    },
}