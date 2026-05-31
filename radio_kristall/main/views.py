from django.shortcuts import render
from .models import News, Vacancies

def index(request):
    return render(request, 'main/index.html')

def news_list(request):
    news = News.objects.filter(is_published=True)
    return render(request, 'main/news.html', {'news': news})

def vacancies_list(request):
    vacancies = Vacancies.objects.filter(is_published=True)
    return render(request, 'main/vacancies.html', {'vacancies': vacancies})

def about(request):
    return render(request, 'main/about.html')

def catalog(request):
    return render(request, 'main/catalog.html')