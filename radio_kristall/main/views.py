from django.shortcuts import render
from .models import News, Vacancies

def index(request):
    # Главная страница - показываем последние 3 новости и вакансии
    latest_news = News.objects.filter(is_published=True)[:3]
    latest_vacancies = Vacancies.objects.filter(is_published=True)[:3]
    return render(request, 'main/index.html', {
        'latest_news': latest_news,
        'latest_vacancies': latest_vacancies,
    })

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