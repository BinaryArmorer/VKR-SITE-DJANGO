from django.shortcuts import render, get_object_or_404
from .models import News, Vacancies, Catalog

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
    products = Catalog.objects.filter(is_published=True)
    return render(request, 'main/catalog.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Catalog, id=product_id, is_published=True)
    return render(request, 'main/product_detail.html', {'product': product})