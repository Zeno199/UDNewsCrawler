import scrapy
import requests
import time
import datetime
import logging
from django.apps import apps
from django.utils.timezone import make_aware


base_url = 'https://nba.udn.com'
start_url = 'https://nba.udn.com/nba/index?gr=www'
headers = {'User-agent': 'Mozilla/5.0'}

def crawl_nba():

    res = requests.get(url = start_url, headers = headers)
    selector = scrapy.Selector(text = res.text)
   
    for news_item in selector.css('#news_body'):
        focus_news = {
            'titles': news_item.css('h3::text').getall(),
            'descriptions': news_item.css('p::text').getall(),
            'links': news_item.css('a::attr(href)').getall(),
            'img_urls': [],
            'contents':[],
            'ctimes':[]
        }

    #  
    # find foucs news content & time
    #
    for link in focus_news['links']:
        res = requests.get(url = base_url+link, headers = headers)
        time.sleep(1)
        selector = scrapy.Selector(text = res.text)
        ctime = selector.css('div.shareBar__info--author span::text').get()
        ctime = datetime.datetime.strptime(ctime, '%Y-%m-%d %H:%M')
        content = selector.css('div#story_body_content span p *::text').getall()[4:]
        content = ''.join(content)
        img = selector.css('.photo_center a img::attr(data-src)').get()
        focus_news['img_urls'].append(img)
        focus_news['contents'].append(content)
        focus_news['ctimes'].append(ctime)
    
    return focus_news

def save(data):
    News = apps.get_model('crawler', 'News')
    for title, description, content, img_url, ctime in zip(data['titles'], data['descriptions'], data['contents'], data['img_urls'], data['ctimes']):
        if News.objects.filter(title = title).exists():
            logging.info("News exists, Pass") 
            print("Pass")
            continue
        try:
            news_obj = News.objects.create(
                title = title,
                description = description,
                content = content,
                img_url = img_url,
                created_at = ctime
            )
            news_obj.save()
        except:
            logging.info(title+" can't be created, Pass") 
            print(title+" can't be created")

def show():
    News = apps.get_model('crawler', 'News')
    n = News.objects.all()
    for news in n :
        print(news.title)
        print(news.description)
        print(news.content)
        print(news.img_url)
        print(news.created_at)




