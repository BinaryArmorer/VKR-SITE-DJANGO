from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('news/', views.news_list, name='news'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),      # ← новая строка
    path('vacancies/', views.vacancies_list, name='vacancies'),
    path('vacancies/<int:vacancy_id>/', views.vacancy_detail, name='vacancy_detail'),  # ← новая строка
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:product_id>/', views.product_detail, name='product_detail'),
]