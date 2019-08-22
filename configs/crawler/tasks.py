from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task.schedules import crontab  
from celery.decorators import periodic_task
from . import crawl
import json, requests, os
import logging
from django.apps import apps
# Get an instance of a logger
logger = logging.getLogger('django.request')

@shared_task(name='Auto_crawler')
def Auto_crawler():
    print('Execute Celery')
    data = crawl.crawl_nba()
    crawl.save(data)
    '''for data in zip_data:
        news_state = CHECK_EXIST(data)
        if news_state:
            continue
        else:
            news_id = SAVE_NEWS(data)
            new_news_ids.append(news_id)
    if new_news_ids:
        logger.info('Sccessfully got new news')
        return APIHandler.catch(data={'news_ids':new_news_ids}, code='001')
    else:
        logger.info('Nothing new')
        return APIHandler.catch(data='Nothing new', code='000')'''