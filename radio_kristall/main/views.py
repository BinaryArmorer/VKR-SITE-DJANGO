from django.shortcuts import render, get_object_or_404
from .models import News, Vacancies, Catalog


# Основные страницы
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')


# Страницы с базой данных
def news_list(request):
    news = News.objects.filter(is_published=True)
    return render(request, 'main/news.html', {'news': news})

def vacancies_list(request):
    vacancies = Vacancies.objects.filter(is_published=True)
    return render(request, 'main/vacancies.html', {'vacancies': vacancies})

def catalog(request):
    products = Catalog.objects.filter(is_published=True)
    return render(request, 'main/catalog.html', {'products': products})


# Страницы с подробнотсями для страниц с базой данных
def news_detail(request, news_id):
    news_item = get_object_or_404(News, news_id=news_id, is_published=True)
    return render(request, 'main/news_detail.html', {'news_item': news_item})

def vacancy_detail(request, vacancy_id):
    vacancy_item = get_object_or_404(Vacancies, vacancy_id=vacancy_id, is_published=True)
    return render(request, 'main/vacancy_detail.html', {'vacancy_item': vacancy_item})

def product_detail(request, product_id):
    product = get_object_or_404(Catalog, id=product_id, is_published=True)
    return render(request, 'main/product_detail.html', {'product': product})