from datetime import datetime

from django.shortcuts import render
from django.template.loader import render_to_string

from django.apps import apps
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.generic import TemplateView
from django.core import serializers
import json
#from rest_framework.renderers import JSONRenderer
from django.views.generic import View
import simplejson

# Create your views here.

class HelloView(TemplateView): 
    template_name = 'hello_world.html' 
    def get(self, request): 
        return render( request, self.template_name, {
        'current_time': str(datetime.now()),
    }) 

#class IndexView(TemplateView):
class NewsList(View):

    template_name = 'index.html' 
    
    def get(self, request):
        
        # Detected connected tables
        '''from django.db import connection
        tables = connection.introspection.table_names()
        print('tables...'+ str(tables))'''

        News = apps.get_model('crawler', 'News')
        try:
            latest = News.objects.order_by('-created_at')[:10]
            news_list = []
            for news in latest:
                data = {
                    'id': news.id,
                    'title': news.title,
                    'description': news.description,
                    'img_url': news.img_url,
                    'created_at': news.created_at
                }
                news_list.append(data)
        except Exception as e:
            print('Error:', e)
            news_list = None

        #return Response(news_list)
        #html = render_to_string( self.template_name, {'news_list': news_list} )
        #res = {'html': html}
        #return HttpResponse( simplejson.dumps(res))
        return render(request, self.template_name, {'news_list': news_list})

class News_Detail(TemplateView): 
    
    template_name = 'news.html'
    
    def get(self, request, news_id):
        News = apps.get_model('crawler', 'News')
        try:
            news = News.objects.get(id = news_id)
            news_detail = {
                'title' : news.title,
                'content' : news.content,
                'img_url' : news.img_url,
                'created_at' : news.created_at
            }
            #return render(request, self.template_name, {'news': data}) 
        except Exception as e:
            print('Error:', e)
            return HttpResponseNotFound("<h1>News Not Found</h1>")

        return render(request, self.template_name, {'news_detail': news_detail}) 

