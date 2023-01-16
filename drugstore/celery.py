import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drugstore.settings')

app = Celery('drugstore')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'spammer': {
        'task': 'main.tasks.spam_attack',
        'schedule': 10.0,
    }
}

app.autodiscover_tasks()
