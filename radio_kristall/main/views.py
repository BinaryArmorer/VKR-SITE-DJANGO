from django.shortcuts import render
from .models import News, Vacancies

def index(request):
    # Главная страница - без новостей и вакансий
    return render(request, 'main/index.html')

def news_list(request):
    # Страница всех новостей
    news = News.objects.filter(is_published=True)
    return render(request, 'main/news.html', {'news': news})

def vacancies_list(request):
    # Страница всех вакансий
    vacancies = Vacancies.objects.filter(is_published=True)
    return render(request, 'main/vacancies.html', {'vacancies': vacancies})

def about(request):
    # Страница "О компании"
    return render(request, 'main/about.html')