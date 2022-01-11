from django.shortcuts import HttpResponse, render
from .models import News, Category, City

def category(request):      
    categories = Category.objects.all()
    return {"categories": categories}

def news_list(request):
    news = News.objects.all()
    contex = {
        'news':news
    }
    return render(request,'home.html',contex)
    

