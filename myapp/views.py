from django.shortcuts import render
from .models import News, Category, City
from taggit.views import Tag

def category(request):      
    categories = Category.objects.all()
    return {"categories": categories}


def city(request):
    city = City.objects.all()
    return {'city':city}


def news_list(request):
    news = News.objects.all()
    contex = {
        'news':news
    }
    return render(request,'home.html',contex)


def category_blog(request, slug):
    category = Category.objects.get(slug=slug)
    news = News.objects.filter(category=category)
    
    context = {
        "news":news,
        'category':category
    }
    
    return render(request,'category_news.html',context)


def city_blog(request, slug):
    city = City.objects.get(slug=slug)
    news = News.objects.filter(city=city)
    
    context = {
        'news':news,
    }
    
    return render(request, 'city_news.html', context)

def new_detail(request,slug):
    new = News.objects.get(slug=slug)
    last_news = News.objects.order_by('-created_at')
    news_category = News.objects.filter(category = new.category)
    new.views += 1
    new.save()
    
    context = {
        'new':new,
        'last_news':last_news,
        'news_category':news_category
    }
    
    return render(request,'detail.html',context)
    


def tag_list(request, slug):
    tag = Tag.objects.get(slug = slug)
    news = News.objects.filter(tags=tag)

    context = {
        'news': news,
    }
    return render(request, 'home.html', context)