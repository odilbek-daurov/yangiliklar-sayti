from .views import  news_list, category_blog, city_blog, new_detail,tag_list
from django.urls import path

urlpatterns = [
    path('', news_list, name='news_list'),
    path('category/<slug:slug>',category_blog, name='category_blog'),
    path('city/<slug:slug>', city_blog, name='city_blog'),
    path('new/<slug:slug>', new_detail, name='new_detail'),
    path('tag/<slug:slug>', tag_list, name='tag_list'),
]

