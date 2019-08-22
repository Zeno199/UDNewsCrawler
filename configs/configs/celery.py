from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from datetime import timedelta
from crawler import tasks
import django
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')


app = Celery(
    'configs'
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

django.setup()

app.conf.CELERYBEAT_SCHEDULE = {
    'Crawler': {
            #'task': 'Auto_crawler',
            'task': 'tasks.Auto_crawler()',
            # UTC 16:00 == UTC+8 0:00 == 當天午夜檢查
            # 'schedule': crontab(minute=0, hour=16),
            'schedule': timedelta(seconds=10),
        },
}

'''app.conf.update(
    CELERYBEAT_SCHEDULE = {
        'Crawler': {
            'task': tasks.auto_crawler(),
            # UTC 16:00 == UTC+8 0:00 == 當天午夜檢查
            # 'schedule': crontab(minute=0, hour=16),
            'schedule': timedelta(seconds=60),
        },
        # 'test': {
        #     'task': 'deploy.tasks.add',
        #     'schedule': timedelta(seconds=5),
        # }
    }
)'''

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
