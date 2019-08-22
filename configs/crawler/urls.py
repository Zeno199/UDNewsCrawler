from django.urls import path

from .views import HelloView, NewsList, News_Detail

urlpatterns = [  
  path('hello/', HelloView.as_view()),
  path('', NewsList.as_view()),
  path('news_detail/<int:news_id>', News_Detail.as_view()),
]