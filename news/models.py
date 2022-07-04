from django.db import models
from django.shortcuts import render
#from .models import News
# Create your models here.


class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.headline
    
def news(request):
    newss = News.objects.all()
    return render(request, 'news.html', {'newss':newss})

