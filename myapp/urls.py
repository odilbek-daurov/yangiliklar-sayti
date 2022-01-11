from .views import category, news_list
from django.urls import path

urlpatterns = [
    path('', news_list, name='news_list'),
    
]

