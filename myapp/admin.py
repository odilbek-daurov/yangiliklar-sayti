from django.contrib import admin
from .models import Category, City,News
@admin.register(Category)
class CategoryNews(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
@admin.register(City)
class CategoryNews(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
@admin.register(News)
class CategoryNews(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
