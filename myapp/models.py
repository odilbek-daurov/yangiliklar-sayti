from django.db import models
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    
    def __str__(self) -> str:
        return self.name
    

class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    
    def __str__(self) -> str:
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updete = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to = 'media/')
    views = models.PositiveIntegerField(default=0)
    tags = TaggableManager()
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return self.title