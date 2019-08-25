from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from datetime import timedelta
import django

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')

app = Celery('crawler.Auto_crawler')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
    )


'''BROKER_URL = 'pyamqp://guest:guest@wlocalhost:5672//' #read docs
CELERY_IMPORTS = ('crawler.tasks', )'''


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')


'''app.conf.CELERYBEAT_SCHEDULE = {
    'Crawler': {
            #'task': 'Auto_crawler',
            'task': 'crawler.tasks.Auto_crawler',
            # UTC 16:00 == UTC+8 0:00 == 當天檢查
            # 'schedule': crontab(minute=0, hour=16),
            'schedule': timedelta(seconds=10),
        },
}'''

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
