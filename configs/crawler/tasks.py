from __future__ import absolute_import, unicode_literals
import datetime
from celery.task.base import periodic_task

from celery import shared_task
from celery.task.schedules import crontab  

from . import crawl
import logging
from django.apps import apps


# Get an instance of a logger
logger = logging.getLogger('django.request')

@shared_task(name='Auto_crawler')
#@periodic_task(run_every=datetime.timedelta(seconds=10))
def Auto_crawler():
    print('Execute Celery')
    data = crawl.crawl_nba()
    crawl.save(data)